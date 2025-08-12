# Crypto DCA App

A lightweight **Streamlit** app to simulate **Dollar-Cost Averaging (DCA)** into a crypto asset, with an optional **RSI filter**.  
The app will plot an equity curve, show drawdowns, and export contribution logs.

> **Status:** scaffold — v0.1 coming soon (UI in place, logic landing next).

---

## 🚀 Features (planned)
- DCA schedule: **Weekly / Monthly** with custom amount per period  
- **RSI filter** (buy only when RSI < threshold)  
- Equity curve & **max drawdown** chart  
- Contribution table with totals; **export CSV**  
- Works **offline** with a bundled sample CSV (no API key required)

---

## 🧰 Tech Stack
- **Streamlit** (UI)  
- **Python**: `pandas`, `numpy`, `matplotlib`  
- (Optional later) Price ingestion via `yfinance` or exchange APIs

---

## 📦 Getting Started

### 1) Clone & enter the project
```bash
git clone https://github.com/<your-username>/crypto-dca-app.git
cd crypto-dca-app
