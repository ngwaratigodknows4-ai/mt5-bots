# Termux MT5 Risk Toolkit 📱📊

Test MT5 risk logic on Android without Windows/PC. Built 100% in Termux.

### Problem this solves
MT5 Python package `MetaTrader5` doesn't install on Android. Most African traders can't test bots without a PC. 
This toolkit lets you test drawdown rules + CYTD tracking using fake data on your phone.

### Features
- **5% Drawdown Detector**: Alerts when equity drops 5%+ vs balance
- **CYTD Tracker**: See Cycle To Date % from Jan 1st balance  
- **Smart Risk Rules**: Auto reduces lot size when CYTD is red
- **Termux Ready**: No Windows/MT5 terminal needed

### 1-Minute Setup on Android
```bash
pkg install python git
git clone https://github.com/ngwaratigodknows4-ai/termux-mt5-risk-toolkit
cd termux-mt5-risk-toolkit
bash setup.sh
python risk_bot.py
