from HeysCipher import Heys
from random import randrange
from collections import Counter


def bruteforceDifference(difference: int) -> Counter:
    betas = []
    cipher = Heys(key=0x0)
    for text in range(2**16):
        X = cipher.round(text, 0x0)
        X_ = cipher.round(text ^ difference, 0x0) 
        betas.append(X ^ X_)

    counter = Counter(betas)
    return counter


def diffSearch(alpha: int, P: list[float], r: int = 6) -> None:
    L = [[]] * r
    L[0] = [tuple([alpha, 1.0])]
    for t in range(1,r):
        print(t)
        for (beta, p) in L[t - 1]:
            gammas = sorted([tuple([x[0], x[1] / 2**16]) for x in bruteforceDifference(beta).items()], key=lambda x: x[1], reverse=True)
            for (gamma, q) in gammas:
                L_t = L[t].copy()
                if gamma in [l[0] for l in L_t]:
                    pg = list(filter(lambda x : x[0] == gamma , L_t))[0][1]
                    L_t.remove((gamma, pg))
                    L_t.append((gamma, pg + (p * q)))
                else:
                    L_t.append(tuple([gamma, p * q]))
                L[t] = L_t.copy()
        # print(L)
        # exit()
        print(f'L[{t}] prob: {sum([x[1] for x in L[t]])}')
        print(f'L[{t}] len before: {len(L[t])}')
        L_t = L[t].copy()
        for (gamma, p) in L[t]:
            if p <= P[t]:
                L_t.remove((gamma, p))
        L[t] = L_t.copy()
        print(f'L[{t}] prob: {sum([x[1] for x in L[t]])}')
        for l in sorted(L[t],key= lambda x: x[1], reverse=True)[0:10]:
            print(l)
        print(f'L[{t}] len after: {len(L[t])}')
    
    print('\n')


    print('########')
    for t in range(len(L)):
        print(t)
        for l in sorted(L[t], key= lambda x : x[1], reverse=True)[0:10]:
            print(l)
        print('\n')

if __name__ == '__main__':
    # print(sorted([x for x in bruteforceDifference(1).items()], key=lambda x: x[1], reverse=True))


    alpha = 1
    #       1    2       3       4       5         6
    #P = [1, 0.1, 0.008, 0.0005, 0.0001, 0.00005, 3.8e-06]
    P = [1, 0.1, 0.0075, 0.001, 0.0002, 0.0001, 3.8e-06]

    diffSearch(alpha, P, 6)
