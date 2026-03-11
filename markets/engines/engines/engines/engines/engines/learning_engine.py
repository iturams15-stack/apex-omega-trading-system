import json

def log_trade(data):

    with open("trade_history.json","a") as f:
        f.write(json.dumps(data)+"\n")
