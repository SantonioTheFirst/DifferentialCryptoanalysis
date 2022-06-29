from HeysCipher import Heys
from random import randrange
from collections import Counter


def bruteforceDifference(difference):
    betas = []
    cipher = Heys(key=0x0)
    for text in range(2**16):
        X = cipher.round(text, 0x0)
        X_ = cipher.round(text ^ difference,0x0) 
        betas.append(X ^ X_)

    counter = Counter(betas)
    return counter

print(bruteforceDifference(1))