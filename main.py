# STRANGE ATTRACTORS

import random
import matplotlib.pyplot as plt


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXY"

generateString = lambda n: "".join( [random.choice(LETTERS) for i in range(n)])

letterToNumber = lambda x: 0.1*(LETTERS.index(x) - 12)

def nextVal( x, y, params ):
    a,b,c,d,e,f = params
    return a + b*x + c*x*x + d*x*y + e*y + f*y*y

def generateAttractor( string = None, np = 10000000, init = (0.,0.) ):
    if string is None:
        string = generateString(12)
    print(string)
    xparams = list(map(letterToNumber, string[:6]))
    yparams = list(map(letterToNumber, string[6:]))

    out = [init]
    x,y = init
    for i in range(np):
        x,y = nextVal(x,y,xparams), nextVal(x,y,yparams)
        out.append((x,y))
        if abs(x) > 1.e20:
            return None
    return out

def plot(points):
    x,y = [p[0] for p in points], [p[1] for p in points]
    plt.plot(x,y,'b.', markersize = 1)
    plt.show()

def go():
    ok = False
    while not ok:
        out = generateAttractor()
        if out is not None:
            ok = True
    
    plot(out)

go()
