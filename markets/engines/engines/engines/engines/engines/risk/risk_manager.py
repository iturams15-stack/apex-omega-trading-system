def generate_trade_levels(price,direction):

    if direction=="BUY":

        stop=price-0.0020

        tp1=price+(price-stop)*2
        tp2=price+(price-stop)*4
        tp3=price+(price-stop)*8

    else:

        stop=price+0.0020

        tp1=price-(stop-price)*2
        tp2=price-(stop-price)*4
        tp3=price-(stop-price)*8

    return stop,tp1,tp2,tp3
