# btc-data-api

A Python-based API for retrieving BTC/USDT historical data, calculating technical indicators (e.g., EMA, SMA), and serving enriched results via endpoints. Powered by BigQuery and deployable on Google Cloud Platform.

## Features

- **Historical Crypto Data**: Retrieve historical data for BTC/USDT, ETH/USDT, BNB/USDT, and more.
- **Technical Indicators**: Calculate a wide range of indicators, including SMA, EMA, MACD, RSI, Bollinger Bands, and many others.
- **Customizable Outputs**: Filter or include specific data columns, calculate indicators for specified periods, and adjust results dynamically.
- **Cloud Integration**: Built on BigQuery and designed for deployment on Google Cloud Platform.
- **Extensible**: Easily add new indicators and data sources.

---

## Prerequisites

1. **Google Cloud Account**: Set up a Google Cloud account and create a BigQuery project.
2. **Python**: Ensure Python 3.8 or newer is installed.
3. **Mamba**: Install [Mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) (requires Miniforge).

---

## Setup

### Environment Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/btc-data-api.git
   cd btc-data-api
   ```

2. Create and activate the environment:

   ```bash
   scripts/set_up
   # or manually:
   mamba env create -f environment.yml
   mamba activate btc-backtesting-env
   ```

3. Install required Google Cloud SDK components:

   ```bash
   gcloud auth application-default login
   ```

4. Configure your BigQuery connection by creating a `database_config.cfg` file in the `config/` directory:

   ```ini
   [DATABASE]
   project_id = your_project_id
   dataset = your_dataset_name
   table = your_table_name
   ```

---

### Notes for Mac Users

If you're on macOS, update your Bash version for compatibility:

1. Install the latest version of Bash:

   ```bash
   brew install bash
   ```

2. Add it to your list of shells:

   ```bash
   sudo sh -c 'echo /opt/homebrew/bin/bash >> /etc/shells'
   ```

3. Change your default shell:

   ```bash
   chsh -s /opt/homebrew/bin/bash
   ```

---

### Environment Management

- **Activate the environment**:

  ```bash
  mamba activate btc-backtesting-env
  ```

- **Update the environment**:

  ```bash
  scripts/update
  # or manually:
  mamba env update -f environment.yml --prune
  ```

- **Deactivate the environment**:

  ```bash
  mamba deactivate
  ```

---

## Running the API Locally

Start the development server locally:

```bash
scripts/run_dev
```

The server will be accessible at `http://127.0.0.1:8000`.

---

## API Documentation

Visit the `/doc` endpoint for comprehensive API documentation:

```bash
http://127.0.0.1:8000/doc
```

The API includes endpoints for:

- **Historical Data Retrieval**: `/data/btcusdt`, `/data/ethusdt`, `/data/bnbusdt`
- **Technical Indicators**: `/indicators/{indicator_name}` for detailed information on each indicator.
- **Customizable Responses**: Use query parameters to add/remove columns, calculate specific indicators, and filter results.

---

## Deployment

1. Ensure the `gcloud` CLI is installed and authenticated:

   ```bash
   gcloud auth login
   gcloud auth application-default login
   ```

2. Deploy the app to Google Cloud Run or App Engine:

   ```bash
   gcloud run deploy
   ```

---

## Indicators Supported

The following indicators are supported:

- **Trend Indicators**: SMA, EMA, MACD
- **Momentum Indicators**: RSI, ROC, Momentum
- **Volatility Indicators**: ATR, Bollinger Bands
- **Volume Indicators**: OBV, CMF, A/D Line
- **Others**: Donchian Channels, Keltner Channels, Pivot Points, VWAP

For details on how to use each indicator, refer to the `/indicators` endpoint.

---

### Notes for Improvement

If you'd like to enhance the documentation further or include additional deployment instructions, feel free to suggest or contribute directly.
