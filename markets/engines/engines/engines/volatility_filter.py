import numpy as np

def volatility_score(atr):

    current=atr[-1]
    avg=np.mean(atr[-20:])

    if current>avg*1.2:
        return 10

    if current>avg:
        return 5

    return 0
