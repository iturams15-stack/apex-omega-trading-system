def detect_order_block(candles):

    for i in range(len(candles)-3):

        c1=candles[i]
        c2=candles[i+1]

        displacement=abs(c2["close"]-c2["open"])

        if c1["close"]<c1["open"] and displacement>2:
            return "bullish"

        if c1["close"]>c1["open"] and displacement>2:
            return "bearish"

    return None
