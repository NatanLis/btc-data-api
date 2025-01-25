from fastapi import APIRouter

router = APIRouter(
    prefix="/documentation",
    tags=["documentation"],
)

@router.get("/")
async def root():
    """
    API Documentation Endpoint.

    Returns:
        dict: API documentation details including available data and implementation.
    """
    return {
        "documentation": {
            "title": "Crypto Indicators API Documentation",
            "description": (
                "This API allows users to fetch historical cryptocurrency data "
                "and calculate various financial indicators."
            ),
            "available_data": ["BTCUSDT", "ETHUSDT", "BNBUSDT"],
            "endpoints": {
                "/": "Welcome message.",
                "/data": "Fetch historical data with optional indicator calculations. Parameters: start, end, timeframe, and multiple indicators (e.g., ema, sma, roc).",
                "/indicators": "List all available indicators with their descriptions and usage.",
                "/indicators/{indicator}": (
                    "Detailed information about a specific indicator, including formula, usage, and example."
                ),
                "/documentation": "API documentation (this endpoint).",
            },
            "indicators": {
                "available_indicators": [
                    "SMA - Simple Moving Average",
                    "EMA - Exponential Moving Average",
                    "ROC - Rate of Change",
                    "RSI - Relative Strength Index",
                    "WIL - Williams %R",
                    "ATR - Average True Range",
                    "MOM - Momentum",
                    "SO - Stochastic Oscillator",
                    "TR - True Range",
                    "MACD - Moving Average Convergence Divergence",
                    "BB - Bollinger Bands",
                    "CMO - Chande Momentum Oscillator",
                    "OBV - On-Balance Volume",
                    "DC - Donchian Channels",
                    "A/D Line - Accumulation/Distribution Line",
                    "CMF - Chaikin Money Flow",
                    "IC - Ichimoku Cloud",
                    "PP - Pivot Points",
                    "CCI - Commodity Channel Index",
                    "ADX - Average Directional Index",
                    "KC - Keltner Channels",
                    "VWAP - Volume-Weighted Average Price",
                ],
                "indicator_usage": (
                    "Each indicator can be calculated by providing its parameters. "
                    "For example, to calculate SMA for a specific period, pass `sma=20` "
                    "as a query parameter in the /data endpoint."
                ),
            },
            "implementation_details": {
                "data_source": "Historical cryptocurrency data from BigQuery.",
                "data_format": (
                    "JSON-like structure, each row representing a candlestick "
                    "with fields like Open, High, Low, Close, Volume, etc."
                ),
                "indicator_calculations": (
                    "Indicators are calculated dynamically using pandas for efficient processing."
                ),
                "filtering": {
                    "only_columns": (
                        "Optional parameter to filter data by specific columns. "
                        "Example: only_columns=['Open', 'Close', 'Volume']."
                    ),
                    "drop_columns": (
                        "Optional parameter to exclude specific columns. "
                        "Example: drop_columns=['Quote_Asset_Volume', 'Number_of_Trades']."
                    ),
                },
            },
            "examples": {
                "fetch_data_with_ema": (
                    "/data?start=2024-01-01&end=2024-01-10&ema=21&sma=50"
                ),
                "list_indicators": "/indicators",
                "get_indicator_details": "/indicators/sma",
            },
        }
    }
