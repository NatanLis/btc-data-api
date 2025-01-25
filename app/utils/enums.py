from enum import Enum

class Columns(Enum):
  OPEN_TIME = "Open_time"
  OPEN = "Open"
  HIGH = "High"
  LOW = "Low"
  CLOSE = "Close"
  VOLUME = "Volume"
  CLOSE_TIME = "Close_time"
  QUOTE_ASSET_VOLUME = "Quote_Asset_Volume"
  NUMBER_OF_TRADES = "Number_of_Trades"
  TAKER_BUY_BASE_ASSET_VOLUME = "Taker_Buy_Base_Asset_Volume"
  TAKER_BUY_QUOTE_ASSET_VOLUME = "Taker_Buy_Quote_Asset_Volume"
