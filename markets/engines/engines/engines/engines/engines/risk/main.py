from flask import Flask,request
import requests

from engines import scoring_engine
from engines import liquidity_map
from engines import learning_engine
from risk import risk_manager

app=Flask(__name__)

DISCORD_WEBHOOK="PASTE_WEBHOOK"

@app.route("/webhook",methods=["POST"])

def webhook():

    data=request.json

    score=scoring_engine.calculate_score(data)

    bias,liq_score=liquidity_map.build_liquidity_map(
        data["price"],
        data["levels"]
    )

    score+=liq_score

    stop,tp1,tp2,tp3=risk_manager.generate_trade_levels(
        data["price"],
        data["direction"]
    )

    if score>=60:

        message=f"""
APEX OMEGA SIGNAL

PAIR: {data['pair']}
DIRECTION: {data['direction']}

ENTRY: {data['price']}

STOP LOSS: {stop}

TP1: {tp1}
TP2: {tp2}
TP3: {tp3}

SCORE: {score}
"""

        requests.post(DISCORD_WEBHOOK,json={"content":message})

        learning_engine.log_trade(data)

    return {"status":"ok"}

app.run(host="0.0.0.0",port=10000)
