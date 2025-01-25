from datetime import datetime

from fastapi import APIRouter, Query
from typing import Optional, List

from fastapi.responses import JSONResponse
from google.cloud import bigquery
from config import load_config

from app.services import rowsAdapter, CalculateIndicators
from app.utils import Columns

router = APIRouter(
  prefix="/data",
  tags=["data"]
  )

config = load_config("database_config.cfg")
client = bigquery.Client()

@router.get("/btcusdt")
async def get_data(
  start: str,
  end: str,
  # timeframe: Optional[str] = None,

  tr: Optional[bool] =  Query(default=None),
  obv: Optional[bool] =  Query(default=None),
  al: Optional[bool] =  Query(default=None),
  ic: Optional[bool] =  Query(default=None),
  pp: Optional[bool] =  Query(default=None),
  vwap: Optional[bool] =  Query(default=None),

  macd: Optional[List[str]] = Query(default=None),

  ema: Optional[List[int]] = Query(default=None),
  sma: Optional[List[int]] = Query(default=None),
  roc: Optional[List[int]] = Query(default=None),
  rsi: Optional[List[int]] = Query(default=None),
  wil: Optional[List[int]] = Query(default=None),
  atr: Optional[List[int]] = Query(default=None),
  mom: Optional[List[int]] = Query(default=None),
  so: Optional[List[int]] = Query(default=None),
  bb: Optional[List[int]] = Query(default=None),
  cmo: Optional[List[int]] = Query(default=None),
  dc: Optional[List[int]] = Query(default=None),
  cmf: Optional[List[int]] = Query(default=None),
  cci: Optional[List[int]] = Query(default=None),
  adx: Optional[List[int]] = Query(default=None),
  kc: Optional[List[int]] = Query(default=None),

  drop_columns: Optional[List[Columns]] = Query(default=None),
  only_columns: Optional[List[Columns]] = Query(default=None),
  ):

  if drop_columns and only_columns:
    return JSONResponse(
      status_code=422,
      content={"error": "You can only provide either drop_columns or only_columns, not both."},
    )

  query = f"""
    SELECT *
    FROM `{config['DATABASE']['project_id']}.{config['DATABASE']['dataset']}.{config['DATABASE']['table']}`
    WHERE TIMESTAMP(Open_time) BETWEEN TIMESTAMP('{datetime.strptime(start, "%y-%m-%d")}') AND TIMESTAMP('{datetime.strptime(end, "%y-%m-%d")}')
    ORDER BY TIMESTAMP(Open_time) ASC
    """

  results = client.query_and_wait(query)
  rows = rowsAdapter(results)

  calculate_indicators = CalculateIndicators()

  # Periodic indicators mapping
  periodic_indicators = {
    "ema": ema,
    "sma": sma,
    "roc": roc,
    "rsi": rsi,
    "wil": wil,
    "atr": atr,
    "mom": mom,
    "so": so,
    "bb": bb,
    "cmo": cmo,
    "dc": dc,
    "cmf": cmf,
    "cci": cci,
    "adx": adx,
    "kc": kc,
  }

  # Non-periodic indicators mapping
  non_periodic_indicators = {
    "al": al,
    "tr": tr,
    "obv": obv,
    "ic": ic,
    "pp": pp,
    "vwap": vwap,
  }

  for indicator_name, periods in periodic_indicators.items():
    if periods:
      func = getattr(calculate_indicators, indicator_name)
      for period in periods:
        rows = func(period, rows)

  if macd:
    for period in macd:
      try:
        short_period, long_period, signal_period = map(int, period.split(','))
      except ValueError:
        return JSONResponse(
          status_code=422,
          content={"error": "Invalid format for MACD. Provide 'short,long,signal'."},
        )
      rows = calculate_indicators.macd(short_period, long_period, signal_period, rows)

  for indicator_name, enabled in non_periodic_indicators.items():
    if enabled:
      func = getattr(calculate_indicators, indicator_name)
      rows = func(rows)


# Filter columns
  if drop_columns:
    rows = calculate_indicators.drop_column(drop_columns, rows)

  if only_columns:
    columns_to_drop = [col.value for col in Columns if col not in only_columns]
    rows = calculate_indicators.drop_column(columns_to_drop, rows)

  return {"data": rows}


# <google.cloud.bigquery.table.RowIterator object at 0x169b01b90>
columns = [
  "Open_time",
  "Open",
  "High",
  "Low",
  "Close",
  "Volume",
  "Close_time",
  "Quote_Asset_Volume",
  "Number_of_Trades",
  "Taker_Buy_Base_Asset_Volume",
  "Taker_Buy_Quote_Asset_Volume"
]