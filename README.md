# Consumer Goods Price Dynamics

A comprehensive analytics and forecasting tool for monitoring and predicting consumer goods price dynamics. This project uses machine learning models (SARIMAX, Random Forest, XGBoost, and LSTM) to analyze CPI data and forecast future trends across various categories like Food, Health, Transport, etc.

## Features

- **Exploratory Data Analysis (EDA):** Visualize CPI trends and distribution across different categories.
- **Forecasting:** Predict future price indices using advanced time series and machine learning models.
- **Model Comparison:** Compare predictions from multiple models (SARIMAX, RF, LSTM, XGBoost Stacked).
- **Interactive Dashboard:** Built with Streamlit for an easy-to-use user experience.
- **Progressive Web App (PWA):** Fully configured with a service worker (`sw.js`), web app manifest (`manifest.json`), and app icons for offline caching and installation support.
- **Clean Embedded & Standalone UI:** Streamlined interface with Streamlit watermarks, footer, and toolbar chrome hidden natively. The sidebar navigation remains fully responsive and accessible.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd "Consumer Goods Price Dynamics"
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

## Progressive Web App & Embedded View Details

### 1. PWA Configurations
Static file serving is enabled in the configuration file [.streamlit/config.toml](file:///c:/Users/chimb/Desktop/Consumer%20Goods%20Price%20Dynamics/.streamlit/config.toml):
```toml
[server]
enableStaticServing = true
```
This serves `manifest.json` and `sw.js` under the path `/app/static/` so the browser can discover and install the application as a standalone PWA.

### 2. Standalone URL & IFrame Embedding
* **Direct Access:** Opening the app directly (e.g. `http://localhost:8501`) redirects automatically to the `?embed=true` URL view to natively hide the footer, colored top decoration, and toolbar chrome.
* **Responsive Sidebar Control:** CSS overrides in both `app.py` and `app/config.py` keep the collapse/expand control button (`[data-testid="collapsedControl"]`) interactive and visible even when the header background is hidden.
* **Cross-Origin Framing & PWA Overrides:** The JavaScript runtime handles embedded cross-origin scopes gracefully. If the app is run on the same-origin parent context (such as Streamlit Community Cloud hosting pages), it dynamically overrides Streamlit's default page metadata (e.g., manifest, theme color, icons, and page title) with NairaPulse AI's custom branding metadata, ensuring that the PWA install option is associated with your custom application attributes rather than Streamlit's. When embedded inside a cross-origin iframe on an external domain, these operations degrade gracefully to local operations, preventing browser security errors.

## Project Structure

- `app/`: Contains the main Streamlit application, color configurations, UI pages, and page modules.
- `data/`: Cleaned datasets used for training and inference.
- `models/`: Trained model weights and scalers.
- `notebook/`: Jupyter notebooks for data analysis and model training.
- `output/`: Visualizations and results.
- `prediction/`: Forecasted results.
