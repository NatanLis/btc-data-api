from fastapi import APIRouter

router = APIRouter(
    prefix="/indicators",
    tags=["indicators"]
)

indicators_info = [
    {
        "name": "Simple Moving Average (SMA)",
        "description": "Calculates the average of a selected range of prices over a specified number of periods.",
        "parameters": ["period"]
    },
    {
        "name": "Exponential Moving Average (EMA)",
        "description": "Gives more weight to recent prices to make it more responsive to new information.",
        "parameters": ["period"]
    },
    {
        "name": "Rate of Change (ROC)",
        "description": "Measures the percentage change in price between the current price and the price a certain number of periods ago.",
        "parameters": ["period"]
    },
    {
        "name": "Relative Strength Index (RSI)",
        "description": "Measures the speed and change of price movements to identify overbought or oversold conditions.",
        "parameters": ["period"]
    },
    {
        "name": "Williams %R (WIL)",
        "description": "Identifies overbought and oversold levels by comparing the closing price to the high-low range over a specific period.",
        "parameters": ["period"]
    },
    {
        "name": "Average True Range (ATR)",
        "description": "Measures market volatility by calculating the average range between high and low prices over a specified period.",
        "parameters": ["period"]
    },
    {
        "name": "Momentum (MOM)",
        "description": "Measures the rate of change in closing prices over a specified period.",
        "parameters": ["period"]
    },
    {
        "name": "Stochastic Oscillator (%K) (SO)",
        "description": "Determines momentum by comparing the closing price to a range of prices over a certain period.",
        "parameters": ["period"]
    },
    {
        "name": "True Range (TR)",
        "description": "Calculates the maximum of the current high-low range or the range from the previous close.",
        "parameters": []
    },
    {
        "name": "Moving Average Convergence Divergence (MACD)",
        "description": "Shows the relationship between two EMAs and a signal line to identify trends and reversals.",
        "parameters": ["short_period", "long_period", "signal_period"]
    },
    {
        "name": "Bollinger Bands (BB)",
        "description": "Plots upper and lower bands around a moving average based on standard deviation to indicate volatility.",
        "parameters": ["period"]
    },
    {
        "name": "Chande Momentum Oscillator (CMO)",
        "description": "Measures momentum by comparing the sum of recent gains to the sum of recent losses.",
        "parameters": ["period"]
    },
    {
        "name": "On-Balance Volume (OBV)",
        "description": "Measures buying and selling pressure as a cumulative volume indicator.",
        "parameters": []
    },
    {
        "name": "Donchian Channels (DC)",
        "description": "Plots the highest high and lowest low over a specific period to indicate trends.",
        "parameters": ["period"]
    },
    {
        "name": "Accumulation/Distribution Line (A/D Line)",
        "description": "Uses price and volume to assess supply and demand for a stock.",
        "parameters": []
    },
    {
        "name": "Chaikin Money Flow (CMF)",
        "description": "Combines price and volume to measure the flow of money into or out of an asset over a specific period.",
        "parameters": ["period"]
    },
    {
        "name": "Ichimoku Cloud (IC)",
        "description": "Combines multiple averages and plots them to indicate support, resistance, and trend direction.",
        "parameters": []
    },
    {
        "name": "Pivot Points (PP)",
        "description": "Identifies support and resistance levels based on the previous period's prices.",
        "parameters": []
    },
    {
        "name": "Commodity Channel Index (CCI)",
        "description": "Identifies overbought and oversold levels based on the deviation from the average price.",
        "parameters": ["period"]
    },
    {
        "name": "Average Directional Index (ADX)",
        "description": "Measures the strength of a trend, regardless of direction.",
        "parameters": ["period"]
    },
    {
        "name": "Keltner Channels (KC)",
        "description": "Plots bands around a moving average using ATR to indicate volatility.",
        "parameters": ["period"]
    },
    {
        "name": "Volume-Weighted Average Price (VWAP)",
        "description": "Calculates the average price of an asset weighted by volume, commonly used intraday.",
        "parameters": []
    }
]

@router.get("/")
async def get_indicators_info():
    """
    Get the list of indicators with their descriptions and parameters.
    """
    return {"indicators": indicators_info}

@router.get("/SMA", summary="Get advanced information about the Simple Moving Average (SMA)")
@router.get("/sma")
async def get_sma_info():
    return {
        "name": "Simple Moving Average (SMA)",
        "description": "Calculates the average of a selected range of prices over a specified number of periods.",
        "formula": "SMA = (Sum of closing prices over N periods) / N",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods for the SMA."}
        ],
        "usage": [
            "Identify trends: A rising SMA indicates an uptrend, while a falling SMA indicates a downtrend.",
            "Support and resistance levels."
        ]
    }

@router.get("/EMA", summary="Get advanced information about the Exponential Moving Average (EMA)")
@router.get("/ema")
async def get_ema_info():
    return {
        "name": "Exponential Moving Average (EMA)",
        "description": "Places greater weight on recent prices to respond to changes more quickly than SMA.",
        "formula": "EMA = Price_t * (2 / (1 + N)) + EMA_y * (1 - (2 / (1 + N)))",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods for the EMA."}
        ],
        "usage": [
            "React more sensitively to price changes.",
            "Identify short-term trends."
        ]
    }

@router.get("/ROC", summary="Get advanced information about the Rate of Change (ROC)")
@router.get("/roc")
async def get_roc_info():
    return {
        "name": "Rate of Change (ROC)",
        "description": "Measures the percentage change in price over a specified number of periods.",
        "formula": "ROC = ((Close_t - Close_(t-N)) / Close_(t-N)) * 100",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods to calculate the ROC."}
        ],
        "usage": [
            "Identify overbought and oversold conditions.",
            "Spot momentum changes."
        ]
    }

@router.get("/RSI", summary="Get advanced information about the Relative Strength Index (RSI)")
@router.get("/rsi")
async def get_rsi_info():
    return {
        "name": "Relative Strength Index (RSI)",
        "description": "Measures the speed and magnitude of price movements to identify overbought or oversold conditions.",
        "formula": "RSI = 100 - (100 / (1 + (Average Gain / Average Loss)))",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods for the RSI calculation."}
        ],
        "usage": [
            "Identify overbought (>70) and oversold (<30) levels.",
            "Spot divergences to predict reversals."
        ]
    }

@router.get("/WIL", summary="Get advanced information about the Williams %R (WIL)")
@router.get("/wil")
async def get_wil_info():
    return {
        "name": "Williams %R (WIL)",
        "description": "Compares the closing price to the high-low range over a specified period.",
        "formula": "WIL = (Highest High - Close) / (Highest High - Lowest Low) * -100",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods to calculate Williams %R."}
        ],
        "usage": [
            "Identify overbought (<-20) and oversold (<-80) levels.",
            "Spot reversals in momentum."
        ]
    }

@router.get("/ATR", summary="Get advanced information about the Average True Range (ATR)")
@router.get("/atr")
async def get_atr_info():
    return {
        "name": "Average True Range (ATR)",
        "description": "Measures market volatility by taking the average of true ranges over a specified period.",
        "formula": "ATR = (Previous ATR * (n-1) + Current TR) / n",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods to calculate ATR."}
        ],
        "usage": [
            "Gauge market volatility.",
            "Set stop-loss levels."
        ]
    }

@router.get("/MOM", summary="Get advanced information about Momentum (MOM)")
@router.get("/mom")
async def get_mom_info():
    return {
        "name": "Momentum (MOM)",
        "description": "Measures the rate of price change over a specified period.",
        "formula": "MOM = Close_t - Close_(t-N)",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods to calculate Momentum."}
        ],
        "usage": [
            "Identify the speed of price movement.",
            "Spot bullish or bearish momentum trends."
        ]
    }

@router.get("/SO", summary="Get advanced information about the Stochastic Oscillator (%K)")
@router.get("/so")
async def get_so_info():
    return {
        "name": "Stochastic Oscillator (%K)",
        "description": "Compares the closing price to the high-low range over a specified number of periods.",
        "formula": "SO_%K = ((Close - Lowest Low) / (Highest High - Lowest Low)) * 100",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods to calculate %K."}
        ],
        "usage": [
            "Identify overbought (>80) and oversold (<20) levels.",
            "Spot potential trend reversals."
        ]
    }

@router.get("/TR", summary="Get advanced information about True Range (TR)")
@router.get("/tr")
async def get_tr_info():
    return {
        "name": "True Range (TR)",
        "description": "Measures market volatility using the range between the high, low, and previous close prices.",
        "formula": "TR = max(High - Low, abs(High - Previous Close), abs(Low - Previous Close))",
        "parameters": [
            {"name": "None", "type": "N/A", "description": "No additional parameters are required for TR."}
        ],
        "usage": [
            "Gauge daily market volatility.",
            "Set stop-loss levels based on volatility."
        ]
    }

@router.get("/MACD", summary="Get advanced information about the Moving Average Convergence Divergence (MACD)")
@router.get("/macd")
async def get_macd_info():
    return {
        "name": "Moving Average Convergence Divergence (MACD)",
        "description": "A trend-following momentum indicator that shows the relationship between two moving averages.",
        "formula": "MACD Line = EMA(short) - EMA(long), Signal Line = EMA(MACD Line, signal_period)",
        "parameters": [
            {"name": "short_period", "type": "integer", "description": "Short-term EMA period (e.g., 12)."},
            {"name": "long_period", "type": "integer", "description": "Long-term EMA period (e.g., 26)."},
            {"name": "signal_period", "type": "integer", "description": "Signal line EMA period (e.g., 9)."}
        ],
        "usage": [
            "Identify bullish or bearish crossovers.",
            "Gauge momentum strength and reversals."
        ]
    }

@router.get("/BB", summary="Get advanced information about Bollinger Bands (BB)")
@router.get("/bb")
async def get_bb_info():
    return {
        "name": "Bollinger Bands (BB)",
        "description": "A volatility indicator that creates a band of three lines: an SMA in the middle and two standard deviations above and below it.",
        "formula": "Upper Band = SMA + (2 * Std Dev), Lower Band = SMA - (2 * Std Dev)",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods for the SMA (e.g., 20)."}
        ],
        "usage": [
            "Identify periods of high or low volatility.",
            "Spot overbought or oversold conditions when prices touch or cross the bands."
        ]
    }

@router.get("/CMO", summary="Get advanced information about the Chande Momentum Oscillator (CMO)")
@router.get("/cmo")
async def get_cmo_info():
    return {
        "name": "Chande Momentum Oscillator (CMO)",
        "description": "Measures momentum by calculating the difference between sum gains and sum losses over a period.",
        "formula": "CMO = ((Sum of Gains - Sum of Losses) / (Sum of Gains + Sum of Losses)) * 100",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods for the CMO calculation."}
        ],
        "usage": [
            "Identify overbought (>50) and oversold (<-50) conditions.",
            "Gauge the strength of momentum in the market."
        ]
    }

@router.get("/OBV", summary="Get advanced information about On-Balance Volume (OBV)")
@router.get("/obv")
async def get_obv_info():
    return {
        "name": "On-Balance Volume (OBV)",
        "description": "A volume-based indicator that predicts price changes by measuring cumulative buying and selling pressure.",
        "formula": (
            "OBV = Previous OBV + Volume (if Close > Previous Close)\n"
            "OBV = Previous OBV - Volume (if Close < Previous Close)\n"
            "OBV = Previous OBV (if Close = Previous Close)"
        ),
        "parameters": [
            {"name": "None", "type": "N/A", "description": "No additional parameters are required for OBV."}
        ],
        "usage": [
            "Identify potential trend reversals.",
            "Confirm price trends with volume trends."
        ]
    }

@router.get("/DC", summary="Get advanced information about Donchian Channels (DC)")
@router.get("/dc")
async def get_dc_info():
    return {
        "name": "Donchian Channels (DC)",
        "description": "A volatility indicator that plots the highest high and lowest low over a specific period.",
        "formula": "Upper Band = Highest High over N periods, Lower Band = Lowest Low over N periods",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods for calculating high and low bands."}
        ],
        "usage": [
            "Identify breakout levels.",
            "Spot trends and reversals."
        ]
    }

@router.get("/ADL", summary="Get advanced information about Accumulation/Distribution Line (A/D Line)")
@router.get("/adl")
async def get_adl_info():
    return {
        "name": "Accumulation/Distribution Line (A/D Line)",
        "description": "Measures the cumulative money flow into and out of a security.",
        "formula": (
            "Money Flow Multiplier = ((Close - Low) - (High - Close)) / (High - Low)\n"
            "Money Flow Volume = Money Flow Multiplier * Volume\n"
            "A/D Line = Previous A/D Line + Money Flow Volume"
        ),
        "parameters": [
            {"name": "None", "type": "N/A", "description": "No additional parameters are required for A/D Line."}
        ],
        "usage": [
            "Identify divergence between price and volume.",
            "Gauge the strength of trends."
        ]
    }

@router.get("/CMF", summary="Get advanced information about Chaikin Money Flow (CMF)")
@router.get("/cmf")
async def get_cmf_info():
    return {
        "name": "Chaikin Money Flow (CMF)",
        "description": "Measures the amount of money flow volume over a specific period to gauge buying and selling pressure.",
        "formula": "CMF = (Sum of Money Flow Volume over N periods) / (Sum of Volume over N periods)",
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods to calculate CMF."}
        ],
        "usage": [
            "Identify bullish (>0) or bearish (<0) trends.",
            "Spot potential trend reversals."
        ]
    }

@router.get("/IC", summary="Get advanced information about Ichimoku Cloud (IC)")
@router.get("/ic")
async def get_ic_info():
    return {
        "name": "Ichimoku Cloud (IC)",
        "description": (
            "A versatile indicator that defines support, resistance, trend direction, and momentum. It consists of five lines: Tenkan-sen, Kijun-sen, Senkou Span A, "
            "Senkou Span B, and Chikou Span."
        ),
        "formula": (
            "Tenkan-sen = (Highest High + Lowest Low) / 2 (for the last 9 periods)\n"
            "Kijun-sen = (Highest High + Lowest Low) / 2 (for the last 26 periods)\n"
            "Senkou Span A = (Tenkan-sen + Kijun-sen) / 2 (plotted 26 periods ahead)\n"
            "Senkou Span B = (Highest High + Lowest Low) / 2 (for the last 52 periods, plotted 26 periods ahead)\n"
            "Chikou Span = Closing Price (plotted 26 periods behind)"
        ),
        "parameters": [
            {"name": "None", "type": "N/A", "description": "No additional parameters are required for IC."}
        ],
        "usage": [
            "Identify trend direction and strength.",
            "Spot dynamic support and resistance levels."
        ]
    }

@router.get("/PP", summary="Get advanced information about Pivot Points (PP)")
@router.get("/pp")
async def get_pp_info():
    return {
        "name": "Pivot Points (PP)",
        "description": "A price-based indicator that identifies potential support and resistance levels for intraday trading.",
        "formula": (
            "Pivot Point (PP) = (High + Low + Close) / 3\n"
            "Resistance 1 (R1) = (2 * PP) - Low\n"
            "Support 1 (S1) = (2 * PP) - High\n"
            "Resistance 2 (R2) = PP + (High - Low)\n"
            "Support 2 (S2) = PP - (High - Low)"
        ),
        "parameters": [
            {"name": "None", "type": "N/A", "description": "No additional parameters are required for PP."}
        ],
        "usage": [
            "Identify support and resistance levels.",
            "Plan potential entry and exit points."
        ]
    }

@router.get("/CCI", summary="Get advanced information about Commodity Channel Index (CCI)")
@router.get("/cci")
async def get_cci_info():
    return {
        "name": "Commodity Channel Index (CCI)",
        "description": "A momentum-based indicator that measures the deviation of price from its average price over a specified period.",
        "formula": (
            "CCI = (Typical Price - SMA of Typical Price) / (0.015 * Mean Deviation)\n"
            "Typical Price = (High + Low + Close) / 3"
        ),
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods to calculate CCI."}
        ],
        "usage": [
            "Identify overbought (>100) and oversold (<-100) conditions.",
            "Spot potential trend reversals."
        ]
    }

@router.get("/ADX", summary="Get advanced information about Average Directional Index (ADX)")
@router.get("/adx")
async def get_adx_info():
    return {
        "name": "Average Directional Index (ADX)",
        "description": "A trend strength indicator that measures the strength of a trend regardless of its direction.",
        "formula": (
            "ADX = 100 * EMA(DX, period)\n"
            "DX = (|+DI - -DI| / |+DI + -DI|) * 100\n"
            "+DI = (Smoothed +DM / ATR) * 100\n"
            "-DI = (Smoothed -DM / ATR) * 100"
        ),
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods to calculate ADX and related components."}
        ],
        "usage": [
            "Gauge the strength of a trend.",
            "Determine whether the market is trending (>25) or ranging (<25)."
        ]
    }

@router.get("/KC", summary="Get advanced information about Keltner Channels (KC)")
@router.get("/kc")
async def get_kc_info():
    return {
        "name": "Keltner Channels (KC)",
        "description": "A volatility-based envelope indicator that uses an EMA as the central line and bands based on ATR.",
        "formula": (
            "Middle Line = EMA(period)\n"
            "Upper Band = EMA(period) + (Multiplier * ATR)\n"
            "Lower Band = EMA(period) - (Multiplier * ATR)"
        ),
        "parameters": [
            {"name": "period", "type": "integer", "description": "Number of periods for the EMA and ATR calculation."},
            {"name": "multiplier", "type": "float", "description": "Multiplier for the ATR to define channel width (e.g., 2)."}
        ],
        "usage": [
            "Identify potential breakouts or reversals.",
            "Gauge market volatility and trends."
        ]
    }

@router.get("/VWAP", summary="Get advanced information about Volume-Weighted Average Price (VWAP)")
@router.get("/vwap")
async def get_vwap_info():
    return {
        "name": "Volume-Weighted Average Price (VWAP)",
        "description": "A trading benchmark that represents the average price weighted by total trading volume.",
        "formula": (
            "VWAP = Cumulative (Price * Volume) / Cumulative Volume"
        ),
        "parameters": [
            {"name": "None", "type": "N/A", "description": "No additional parameters are required for VWAP."}
        ],
        "usage": [
            "Determine intraday support and resistance levels.",
            "Evaluate trade executions relative to the market average."
        ]
    }
