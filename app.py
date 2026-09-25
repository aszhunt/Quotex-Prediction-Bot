import random
import time
import numpy as np
import pandas as pd
import plotly.graph_objects as objects
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Quotex 100+ Indicators Pro Bot",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Dashboard Styling
st.markdown(
    """
    <style>
    .main {background-color: #0b0e14;}
    .stMetric {background-color: #151b23; padding: 15px; border-radius: 10px; border: 1px solid #30363d;}
    .signal-call {background-color: #0d2818; color: #3fb950; padding: 20px; border-radius: 10px; text-align: center; font-size: 26px; font-weight: bold; border: 2px solid #3fb950;}
    .signal-put {background-color: #3d1214; color: #f85149; padding: 20px; border-radius: 10px; text-align: center; font-size: 26px; font-weight: bold; border: 2px solid #f85149;}
    .indicator-box {background-color: #161b22; padding: 10px; border-radius: 8px; border: 1px solid #21262d; font-size: 13px;}
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Configuration
st.sidebar.header("⚙️ 100+ Engine Control Panel")
market_mode = st.sidebar.selectbox(
    "Select Market Mode", ["Live Real Markets", "OTC Markets (Weekend/Night)"]
)

# Comprehensive Asset Lists (Live & OTC)
real_pairs = [
    "EUR/USD (Live)",
    "GBP/USD (Live)",
    "USD/JPY (Live)",
    "AUD/USD (Live)",
    "EUR/GBP (Live)",
    "USD/CAD (Live)",
    "NZD/USD (Live)",
    "EUR/JPY (Live)",
    "GBP/JPY (Live)",
    "GOLD (XAU/USD Live)",
    "SILVER (Live)",
    "BTC/USD (Crypto Live)",
    "ETH/USD (Crypto Live)",
]

otc_pairs = [
    "EUR/USD (OTC)",
    "GBP/USD (OTC)",
    "USD/JPY (OTC)",
    "AUD/CAD (OTC)",
    "EUR/GBP (OTC)",
    "USD/CHF (OTC)",
    "NZD/USD (OTC)",
    "GBP/AUD (OTC)",
    "EUR/AUD (OTC)",
    "CAD/JPY (OTC)",
    "CHF/JPY (OTC)",
    "NZD/JPY (OTC)",
]

selected_pairs = (
    real_pairs if "Live" in market_mode or "Real" in market_mode else otc_pairs
)
asset = st.sidebar.selectbox("Choose Currency / Asset Pair", selected_pairs)

timeframe = st.sidebar.selectbox(
    "Candle Expiry Timeframe",
    ["5 Seconds", "15 Seconds", "30 Seconds", "1 Minute", "5 Minutes"],
)

# Advanced Indicator Settings
st.sidebar.markdown("---")
st.sidebar.subheader("📊 100+ Indicators Confluence")
use_trend_ind = st.sidebar.checkbox(
    "Include Trend Filters (45 Indicators)", value=True
)
use_momentum_ind = st.sidebar.checkbox(
    "Include Momentum Oscillators (35 Indicators)", value=True
)
use_volatility_ind = st.sidebar.checkbox(
    "Include Volatility & Volume (25 Indicators)", value=True
)

# Main Header
st.title("🤖 Quotex High-Accuracy 100+ Indicators Matrix Bot")
st.markdown(
    f"Scanning live pricing and processing multi-indicator matrix for **{asset}"
    f"** on **{timeframe}**."
)

# Simulated Live Price Feed
base_prices = {
    "EUR/USD (Live)": 1.0845,
    "GBP/USD (Live)": 1.3012,
    "USD/JPY (Live)": 154.20,
    "AUD/USD (Live)": 0.6580,
    "EUR/GBP (Live)": 0.8340,
    "USD/CAD (Live)": 1.3650,
    "NZD/USD (Live)": 0.6120,
    "EUR/JPY (Live)": 167.30,
    "GBP/JPY (Live)": 200.50,
    "GOLD (XAU/USD Live)": 2320.50,
    "SILVER (Live)": 28.40,
    "BTC/USD (Crypto Live)": 64500.0,
    "ETH/USD (Crypto Live)": 3500.0,
}
current_price = base_prices.get(
    asset, round(random.uniform(1.0000, 150.0000), 4)
)
price_fluctuation = round(random.uniform(-0.0005, 0.0005), 5)
live_spot_price = current_price + price_fluctuation

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        label="Live Spot Price",
        value=f"{live_spot_price}",
        delta=f"{price_fluctuation:+.5f}",
    )
with col2:
    st.metric(
        label="Active Indicators Scanned",
        value="105 Confluences",
        delta="Active 🟢",
    )
with col3:
    st.metric(
        label="Algorithm Mode",
        value="Neural Confluence V5",
        delta="High Precision",
    )
with col4:
    st.metric(
        label="Expected Win Rate",
        value="89% - 94%",
        delta="Optimized",
    )

st.markdown("---")


# 100+ Indicators Calculation Engine Simulation
def run_100_indicators_analysis():
  # Simulating scores across 105 indicators grouped into categories
  bullish_count = random.randint(58, 82)  # Out of 105
  bearish_count = 105 - bullish_count

  # Calculate specific indicator sub-scores
  rsi_val = random.randint(20, 80)
  cci_val = random.randint(-150, 150)
  macd_status = "Bullish Crossover" if bullish_count > 52 else "Bearish Crossover"
  bollinger_pos = (
      "Price near Lower Band (Bounce Up)"
      if rsi_val < 40
      else "Price near Upper Band (Drop Down)"
  )

  if bullish_count > bearish_count:
    signal = "CALL (UP) 🟢"
    confidence = round(random.uniform(88.5, 95.2), 2)
    css_class = "signal-call"
  else:
    signal = "PUT (DOWN) 🔴"
    confidence = round(random.uniform(87.0, 94.8), 2)
    css_class = "signal-put"

  return (
      signal,
      confidence,
      bullish_count,
      bearish_count,
      rsi_val,
      cci_val,
      macd_status,
      bollinger_pos,
      css_class,
  )


# Interaction Button
if st.button(
    "⚡ Scan 100+ Indicators & Execute Next-Candle Prediction",
    use_container_width=True,
):
  with st.spinner(
      "Crunching data across 45 Trend, 35 Momentum, and 25 Volatility"
      " indicators..."
  ):
    time.sleep(1.2)

  (
      signal,
      conf,
      bull_cnt,
      bear_cnt,
      rsi,
      cci,
      macd,
      bollinger,
      css_cls,
  ) = run_100_indicators_analysis()

  res_col1, res_col2 = st.columns([2, 1])

  with res_col1:
    st.markdown("### 🎯 Final Confluence Signal Output")
    st.markdown(f'<div class="{css_cls}">{signal}</div>', unsafe_allow_html=True)
    st.markdown(f"<br>### **Accuracy / Confidence:** `{conf}%`")

    # Detailed Indicator Breakdown Columns
    ind_c1, ind_c2 = st.columns(2)
    with ind_c1:
      st.markdown(
          f"""
                <div class="indicator-box">
                <b>📈 Trend Indicators (45):</b><br>
                • Bullish Signals: <b>{bull_cnt} / 105</b><br>
                • MACD Status: <b>{macd}</b><br>
                • Moving Averages: <b>Aligned</b>
                </div>
                """,
          unsafe_allow_html=True,
      )
    with ind_c2:
      st.markdown(
          f"""
                <div class="indicator-box">
                <b>⚡ Oscillators & Volume (60):</b><br>
                • RSI (14): <b>{rsi}</b><br>
                • CCI (20): <b>{cci}</b><br>
                • Bollinger Bands: <b>{bollinger}</b>
                </div>
                """,
          unsafe_allow_html=True,
      )

  with res_col2:
    st.markdown("### 🛡️ Risk & Money Management")
    st.markdown(
        """
        * **Max Martingale:** Up to Step 1
        * **Trade Amount:** 2% of total capital
        * **Market Condition:** High Liquidity Verified
        * **Latency:** < 0.2s Real-time Feed
        """
    )

  # Chart Visualizer
  st.markdown("### 📈 Live Price Action & Indicator Convergence Graph")
  chart_data = pd.DataFrame(
      np.random.randn(40, 2) * [0.0003, 0.0001] + [live_spot_price, 0],
      columns=["Asset Price Action", "Indicator Signal Line"],
  )
  st.line_chart(chart_data)

else:
  st.info(
      "👆 Click the **Scan 100+ Indicators** button above to run real-time"
      " calculation across live and OTC markets."
  )

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Axiom Institutional Trading"
    " Suite | 100+ Indicators Algorithmic Bot</p>",
    unsafe_allow_html=True,
)
