import pandas as pd

class CalculateIndicators:
    """
    A utility class for calculating various financial indicators.
    """
    # def __init__(self):
    #     self._finalize_dataframe = self._finalize_dataframe

    def _finalize_dataframe(self, df):
        """Replace invalid values and return JSON-like data."""
        df.replace([float('inf'), float('-inf')], float('nan'), inplace=True)
        df.fillna(0, inplace=True)
        return df.to_dict(orient="records")

    def drop_column(self, columns, data):
        """
        Drop a column from the data.

        Args:
            column (list[str]): The column name to drop.
            data (list): JSON-like data containing the column to drop.

        Returns:
            list: Data without the specified column.
        """
        df = pd.DataFrame(data)
        df.drop(columns, axis=1, inplace=True)
        return self._finalize_dataframe(df)

    def sma(self, period, data):
        """
        Calculate Simple Moving Average (SMA) for the given period.

        Args:
            period (int): The period for SMA calculation.
            data (list): The JSON-like data (list of dictionaries) containing 'Close' prices.

        Returns:
            list: Data enriched with SMA values.
        """
        df = pd.DataFrame(data)
        df[f"SMA_{period}"] = df['Close'].rolling(window=period).mean()
        return self._finalize_dataframe(df)

    def ema(self, period, data):
        """
        Calculate Exponential Moving Average (EMA) for the given period.

        Args:
            period (int): The period for EMA calculation.
            data (list): The JSON-like data (list of dictionaries) containing 'Close' prices.

        Returns:
            list: Data enriched with EMA values.
        """
        df = pd.DataFrame(data)
        df[f"EMA_{period}"] = df['Close'].ewm(span=period).mean()
        return self._finalize_dataframe(df)

    def roc(self, period, data):
        """
        Calculate Rate of Change (ROC) for the given period.

        Args:
            period (int): The period for ROC calculation.
            data (list): The JSON-like data (list of dictionaries) containing 'Close' prices.

        Returns:
            list: Data enriched with ROC values.
        """
        df = pd.DataFrame(data)
        df[f"ROC_{period}"] = df['Close'].pct_change(periods=period) * 100
        return self._finalize_dataframe(df)

    def rsi(self, period, data):
        """
        Calculate Relative Strength Index (RSI) for the given period.

        Args:
            period (int): The period for RSI calculation.
            data (list): The JSON-like data (list of dictionaries) containing 'Close' prices.

        Returns:
            list: Data enriched with RSI values.
        """
        df = pd.DataFrame(data)
        delta = df['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        rs = avg_gain / avg_loss
        df[f"RSI_{period}"] = 100 - (100 / (1 + rs))
        return self._finalize_dataframe(df)

    def wil(self, period, data):
        """
        Calculate Williams %R for the given period.

        Args:
            period (int): The period for Williams %R calculation.
            data (list): The JSON-like data (list of dictionaries) containing 'High', 'Low', and 'Close' prices.

        Returns:
            list: Data enriched with Williams %R values.
        """
        df = pd.DataFrame(data)
        high_roll = df['High'].rolling(window=period).max()
        low_roll = df['Low'].rolling(window=period).min()
        df[f"WIL_{period}"] = ((high_roll - df['Close']) / (high_roll - low_roll)) * -100
        return self._finalize_dataframe(df)

    def atr(self, period, data):
        """
        Calculate Average True Range (ATR) for the given period.

        Args:
            period (int): The period for ATR calculation.
            data (list): The JSON-like data (list of dictionaries) containing 'High', 'Low', and 'Close' prices.

        Returns:
            list: Data enriched with ATR values.
        """
        df = pd.DataFrame(data)
        df['TR'] = df[['High', 'Low', 'Close']].apply(
            lambda row: max(
                row['High'] - row['Low'],
                abs(row['High'] - row['Close']),
                abs(row['Low'] - row['Close'])
            ),
            axis=1
        )
        df[f"ATR_{period}"] = df['TR'].rolling(window=period).mean()
        return self._finalize_dataframe(df)

    def mom(self, period, data):
        """
        Calculate Momentum (MOM) for the given period.

        Args:
            period (int): The period for MOM calculation.
            data (list): The JSON-like data (list of dictionaries) containing 'Close' prices.

        Returns:
            list: Data enriched with MOM values.
        """
        df = pd.DataFrame(data)
        df[f"MOM_{period}"] = df['Close'] - df['Close'].shift(period)
        return self._finalize_dataframe(df)

    def so(self, period, data):
        """
        Calculate Stochastic Oscillator (%K) for the given period.

        Args:
            period (int): The period for SO calculation.
            data (list): The JSON-like data (list of dictionaries) containing 'High', 'Low', and 'Close' prices.

        Returns:
            list: Data enriched with %K values.
        """
        df = pd.DataFrame(data)
        df['Lowest Low'] = df['Low'].rolling(window=period).min()
        df['Highest High'] = df['High'].rolling(window=period).max()
        df[f"SO_%K_{period}"] = ((df['Close'] - df['Lowest Low']) / (df['Highest High'] - df['Lowest Low'])) * 100
        df.drop(['Lowest Low', 'Highest High'], axis=1, inplace=True)
        return self._finalize_dataframe(df)

    def tr(self, data):
        """
        Calculate True Range (TR) for the data.

        Args:
            data (list): The JSON-like data (list of dictionaries) containing 'High', 'Low', and 'Close' prices.

        Returns:
            list: Data enriched with TR values.
        """
        df = pd.DataFrame(data)
        df['Previous Close'] = df['Close'].shift(1)
        df['TR'] = df[['High', 'Low', 'Close', 'Previous Close']].apply(
            lambda row: max(
                row['High'] - row['Low'],
                abs(row['High'] - row['Previous Close']),
                abs(row['Low'] - row['Previous Close'])
            ),
            axis=1
        )
        df.drop(['Previous Close'], axis=1, inplace=True)
        return self._finalize_dataframe(df)

    def macd(self, short_period, long_period, signal_period, data):
        """
        Calculate MACD and Signal Line.

        Args:
            short_period (int): The short EMA period (e.g., 12).
            long_period (int): The long EMA period (e.g., 26).
            signal_period (int): The signal line EMA period (e.g., 9).
            data (list): JSON-like data containing 'Close' prices.

        Returns:
            list: Data enriched with MACD Line and Signal Line.
        """
        df = pd.DataFrame(data)
        df['EMA_short'] = df['Close'].ewm(span=short_period, adjust=False).mean()
        df['EMA_long'] = df['Close'].ewm(span=long_period, adjust=False).mean()
        df['MACD_Line'] = df['EMA_short'] - df['EMA_long']
        df['Signal_Line'] = df['MACD_Line'].ewm(span=signal_period, adjust=False).mean()
        df.drop(['EMA_short', 'EMA_long'], axis=1, inplace=True)
        df[f"MACD_Line_{short_period}_{long_period}"] = df['MACD_Line']
        df[f"Signal_Line_{signal_period}"] = df['Signal_Line']
        df.drop(['MACD_Line', 'Signal_Line'], axis=1, inplace=True)
        df.replace([float('inf'), float('-inf')], float('nan'), inplace=True)
        df.fillna(0, inplace=True)
        return self._finalize_dataframe(df)


    def bb(self, period, data):
        """
        Calculate Bollinger Bands.

        Args:
            period (int): The period for the SMA (e.g., 20).
            data (list): JSON-like data containing 'Close' prices.

        Returns:
            list: Data enriched with Bollinger Bands (Upper, Middle, Lower).
        """
        df = pd.DataFrame(data)
        df[f"Middle_Band_{period}"] = df['Close'].rolling(window=period).mean()
        df['Standard_Deviation'] = df['Close'].rolling(window=period).std()
        df[f"Upper_Band_{period}"] = df[f"Middle_Band_{period}"] + (2 * df['Standard_Deviation'])
        df[f"Lower_Band_{period}"] = df[f"Middle_Band_{period}"] - (2 * df['Standard_Deviation'])
        df.drop(['Standard_Deviation'], axis=1, inplace=True)
        return self._finalize_dataframe(df)

    def cmo(self, period, data):
        """
        Calculate Chande Momentum Oscillator (CMO) for the given period.

        Args:
            period (int): The period for CMO calculation.
            data (list): JSON-like data containing 'Close' prices.

        Returns:
            list: Data enriched with CMO values.
        """
        df = pd.DataFrame(data)
        delta = df['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        sum_gain = gain.rolling(window=period).sum()
        sum_loss = loss.rolling(window=period).sum()

        df[f"CMO_{period}"] = ((sum_gain - sum_loss) / (sum_gain + sum_loss)) * 100
        return self._finalize_dataframe(df)

    def obv(self, data):
        """
        Calculate On-Balance Volume (OBV).

        Args:
            data (list): JSON-like data containing 'Close' and 'Volume' prices.

        Returns:
            list: Data enriched with OBV values.
        """
        df = pd.DataFrame(data)
        df['OBV'] = 0  # Initialize OBV column
        for i in range(1, len(df)):
            if df.loc[i, 'Close'] > df.loc[i - 1, 'Close']:
                df.loc[i, 'OBV'] = df.loc[i - 1, 'OBV'] + df.loc[i, 'Volume']
            elif df.loc[i, 'Close'] < df.loc[i - 1, 'Close']:
                df.loc[i, 'OBV'] = df.loc[i - 1, 'OBV'] - df.loc[i, 'Volume']
            else:
                df.loc[i, 'OBV'] = df.loc[i - 1, 'OBV']
        return self._finalize_dataframe(df)

    def dc(self, period, data):
        """
        Calculate Donchian Channels.

        Args:
            period (int): The period for Donchian Channels calculation.
            data (list): JSON-like data containing 'High' and 'Low' prices.

        Returns:
            list: Data enriched with Donchian Channel values (Upper, Lower).
        """
        df = pd.DataFrame(data)
        df[f"Donchian_Upper_{period}"] = df['High'].rolling(window=period).max()
        df[f"Donchian_Lower_{period}"] = df['Low'].rolling(window=period).min()
        df[f"Donchian_Mid_{period}"] = (df[f"Donchian_Upper_{period}"] + df[f"Donchian_Lower_{period}"]) / 2
        return self._finalize_dataframe(df)


    def al(self, data):
        """
        Calculate Accumulation/Distribution Line (A/D Line).

        Args:
            data (list): JSON-like data containing 'High', 'Low', 'Close', and 'Volume'.

        Returns:
            list: Data enriched with A/D Line values.
        """
        df = pd.DataFrame(data)
        df['Money_Flow_Multiplier'] = ((df['Close'] - df['Low']) - (df['High'] - df['Close'])) / (df['High'] - df['Low'])
        df['Money_Flow_Volume'] = df['Money_Flow_Multiplier'] * df['Volume']
        df['AD_Line'] = df['Money_Flow_Volume'].cumsum()
        df.drop(['Money_Flow_Multiplier', 'Money_Flow_Volume'], axis=1, inplace=True)  # Clean up temporary columns
        return self._finalize_dataframe(df)

    def cmf(self, period, data):
        """
        Calculate Chaikin Money Flow (CMF).

        Args:
            period (int): The period for CMF calculation.
            data (list): JSON-like data containing 'High', 'Low', 'Close', and 'Volume'.

        Returns:
            list: Data enriched with CMF values.
        """
        df = pd.DataFrame(data)
        df['Money_Flow_Multiplier'] = ((df['Close'] - df['Low']) - (df['High'] - df['Close'])) / (df['High'] - df['Low'])
        df['Money_Flow_Volume'] = df['Money_Flow_Multiplier'] * df['Volume']
        df[f"CMF_{period}"] = df['Money_Flow_Volume'].rolling(window=period).sum() / df['Volume'].rolling(window=period).sum()
        df.drop(['Money_Flow_Multiplier', 'Money_Flow_Volume'], axis=1, inplace=True)  # Clean up temporary columns
        return self._finalize_dataframe(df)


    def ic(self, data):
        """
        Calculate Ichimoku Cloud components.

        Args:
            data (list): JSON-like data with 'High', 'Low', and 'Close' prices.

        Returns:
            list: Data enriched with Ichimoku Cloud components.
        """
        df = pd.DataFrame(data)
        df['Tenkan_sen'] = (df['High'].rolling(window=9).max() + df['Low'].rolling(window=9).min()) / 2
        df['Kijun_sen'] = (df['High'].rolling(window=26).max() + df['Low'].rolling(window=26).min()) / 2
        df['Senkou_Span_A'] = ((df['Tenkan_sen'] + df['Kijun_sen']) / 2).shift(26)
        df['Senkou_Span_B'] = (df['High'].rolling(window=52).max() + df['Low'].rolling(window=52).min()) / 2
        df['Chikou_Span'] = df['Close'].shift(-26)
        return self._finalize_dataframe(df)

    def pp(self, data):
        """
        Calculate Pivot Points, support, and resistance levels.

        Args:
            data (list): JSON-like data with 'High', 'Low', and 'Close' prices.

        Returns:
            list: Data enriched with Pivot Points and support/resistance levels.
        """
        df = pd.DataFrame(data)
        df['Pivot'] = (df['High'] + df['Low'] + df['Close']) / 3
        df['Support_1'] = 2 * df['Pivot'] - df['High']
        df['Resistance_1'] = 2 * df['Pivot'] - df['Low']
        df['Support_2'] = df['Pivot'] - (df['High'] - df['Low'])
        df['Resistance_2'] = df['Pivot'] + (df['High'] - df['Low'])
        return self._finalize_dataframe(df)

    def cci(self, period, data):
        """
        Calculate Commodity Channel Index (CCI).

        Args:
            period (int): The period for CCI calculation.
            data (list): JSON-like data with 'High', 'Low', and 'Close' prices.

        Returns:
            list: Data enriched with CCI values.
        """
        df = pd.DataFrame(data)
        df['Typical_Price'] = (df['High'] + df['Low'] + df['Close']) / 3
        df['SMA_TP'] = df['Typical_Price'].rolling(window=period).mean()
        df['Mean_Deviation'] = df['Typical_Price'].rolling(window=period).apply(lambda x: abs(x - x.mean()).mean(), raw=True)
        df[f"CCI_{period}"] = (df['Typical_Price'] - df['SMA_TP']) / (0.015 * df['Mean_Deviation'])
        return self._finalize_dataframe(df)

    def adx(self, period, data):
        """
        Calculate Average Directional Index (ADX).

        Args:
            period (int): The period for ADX calculation.
            data (list): JSON-like data with 'High', 'Low', and 'Close' prices.

        Returns:
            list: Data enriched with ADX values.
        """
        df = pd.DataFrame(data)
        df['TR'] = df[['High', 'Low', 'Close']].apply(
            lambda row: max(row['High'] - row['Low'], abs(row['High'] - row['Close']), abs(row['Low'] - row['Close'])),
            axis=1
        )
        df['+DM'] = df['High'].diff().where((df['High'].diff() > df['Low'].diff()) & (df['High'].diff() > 0), 0)
        df['-DM'] = -df['Low'].diff().where((df['Low'].diff() > df['High'].diff()) & (df['Low'].diff() > 0), 0)
        df['+DI'] = 100 * (df['+DM'].rolling(window=period).mean() / df['TR'].rolling(window=period).mean())
        df['-DI'] = 100 * (df['-DM'].rolling(window=period).mean() / df['TR'].rolling(window=period).mean())
        df['DX'] = 100 * abs(df['+DI'] - df['-DI']) / (df['+DI'] + df['-DI'])
        df[f"ADX_{period}"] = df['DX'].rolling(window=period).mean()
        df.drop(['TR', '+DM', '-DM', '+DI', '-DI', 'DX'], axis=1, inplace=True)
        return self._finalize_dataframe(df)

    def kc(self, period, data):
        """
        Calculate Keltner Channels.

        Args:
            period (int): The period for Keltner Channels calculation.
            data (list): JSON-like data with 'High', 'Low', and 'Close' prices.

        Returns:
            list: Data enriched with Keltner Channels values.
        """
        df = pd.DataFrame(data)
        df['Middle_Band'] = df['Close'].rolling(window=period).mean()
        df['ATR'] = df[['High', 'Low', 'Close']].apply(
            lambda row: max(row['High'] - row['Low'], abs(row['High'] - row['Close']), abs(row['Low'] - row['Close'])),
            axis=1
        ).rolling(window=period).mean()
        df['Upper_Band'] = df['Middle_Band'] + (2 * df['ATR'])
        df['Lower_Band'] = df['Middle_Band'] - (2 * df['ATR'])
        return self._finalize_dataframe(df)

    def vwap(self, data):
        """
        Calculate Volume-Weighted Average Price (VWAP).

        Args:
            data (list): JSON-like data with 'High', 'Low', 'Close', and 'Volume'.

        Returns:
            list: Data enriched with VWAP values.
        """
        df = pd.DataFrame(data)
        df['Typical_Price'] = (df['High'] + df['Low'] + df['Close']) / 3
        df['Cumulative_TP_Volume'] = (df['Typical_Price'] * df['Volume']).cumsum()
        df['Cumulative_Volume'] = df['Volume'].cumsum()
        df['VWAP'] = df['Cumulative_TP_Volume'] / df['Cumulative_Volume']
        return self._finalize_dataframe(df)
