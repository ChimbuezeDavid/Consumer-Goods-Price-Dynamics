# Consumer Goods Price Dynamics

A comprehensive analytics and forecasting tool for monitoring and predicting consumer goods price dynamics. This project uses machine learning models (SARIMAX, Random Forest, XGBoost, and LSTM) to analyze CPI data and forecast future trends across various categories like Food, Health, Transport, etc.

## Features

- **Exploratory Data Analysis (EDA):** Visualize CPI trends and distribution across different categories.
- **Forecasting:** Predict future price indices using advanced time series and machine learning models.
- **Model Comparison:** Compare predictions from multiple models (SARIMAX, RF, LSTM, XGBoost Stacked).
- **Interactive Dashboard:** Built with Streamlit for an easy-to-use user experience.

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

## Project Structure

- `app/`: Contains the main Streamlit application and page modules.
- `data/`: Cleaned datasets used for training and inference.
- `models/`: Trained model weights and scalers.
- `notebook/`: Jupyter notebooks for data analysis and model training.
- `output/`: Visualizations and results.
- `prediction/`: Forecasted results.
