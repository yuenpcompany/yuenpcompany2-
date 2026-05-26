import random

def gen_pass(p):
    e = "+-/*!&$#?=@<>123456789"
    r = ""
    for i in range(p):
        r += random.choice(e)
    return r

def flip_coin():
    return random.choice(["орел", "решка"])
