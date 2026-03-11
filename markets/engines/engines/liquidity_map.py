def build_liquidity_map(price,levels):

    above=[l for l in levels if l>price]
    below=[l for l in levels if l<price]

    if len(above)>len(below):
        return "bullish",10

    if len(below)>len(above):
        return "bearish",10

    return "neutral",0
