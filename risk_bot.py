import MetaTrader5 as mt5
import time

def check_risk():
    """Check account risk before trading"""
    if not mt5.initialize():
        print("MT5 failed to initialize")
        return False
    
    account = mt5.account_info()
    if account is None:
        print("No account info")
        return False
    
    balance = account.balance
    equity = account.equity
    
    print(f"Balance: ${balance}")
    print(f"Equity: ${equity}")
    
    if equity < balance * 0.95:
        print("RISK ALERT: Equity dropped 5%! Stop trading.")
        return False
    
    print("Risk OK: Safe to trade")
    return True

if __name__ == "__main__":
    check_risk()
    mt5.shutdown()
+
