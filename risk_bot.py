def check_risk(balance=1000, equity=980):
    print(f"Balance: ${balance}")
    print(f"Equity: ${equity}")

    if equity < balance * 0.95:
        print("RISK ALERT: Equity dropped 5%")
        return False

    print("Risk OK: Safe to trade")
    return True

if __name__ == "__main__":
    check_risk()

