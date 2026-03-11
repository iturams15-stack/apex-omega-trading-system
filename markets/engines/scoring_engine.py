def calculate_score(data):

    score = 0

    if data["macro_bias"]:
        score += 15

    if data["stochastic"]:
        score += 10

    if data["smt"]:
        score += 12

    if data["irl_sweep"]:
        score += 15

    if data["displacement"]:
        score += 10

    if data["fvg"]:
        score += 10

    if data["session"]:
        score += 8

    if data["liquidity_trap"]:
        score += 15

    return score
