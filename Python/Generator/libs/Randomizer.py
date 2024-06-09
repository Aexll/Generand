from random import randint,random
import colorsys
import numpy as np


voyelles    = ['a','e','i','o','u']
consonnes   = ['c','t','p','r','k','d','v','j','h','z','f','x','w','qu','s','g','h','l','m','n']

USED_NAMES = []



def RD_Name() -> str:

    name = ""
    flipflop = bool(randint(0,1))

    for i in range(randint(4,8)):
        if flipflop:
            name+=voyelles[randint(0,len(voyelles)-1)]
        else:
            name+=consonnes[randint(0,len(consonnes)-1)]
        flipflop = not flipflop
    
    if name in USED_NAMES:
        print("this name is already in use ! trying to find another one ...")
        return RD_Name()

    USED_NAMES.append(name)

    return name

def RD_Color() -> tuple:
    _linear_color = colorsys.hsv_to_rgb(random(),1,1)
    _byte_color = [0,0,0]
    _byte_color[0] = _linear_color[0] * 255 
    _byte_color[1] = _linear_color[1] * 255 
    _byte_color[2] = _linear_color[2] * 255 
    return _byte_color

def RD_Gausse(_min,_max,sigma=1) -> float:

    nb = (np.random.normal(5, sigma, 1)/10)[0]

    nb = _min + abs(_min-_max)*nb

    return nb

def RD_Exponent(_min:float,_max:float,simga:float=1,clamp:bool=False) -> float:

    nb = np.random.exponential(simga,100)

    # print(nb)

    a = []

    for i in nb:
        if clamp:
            a += [ min(_min+abs(_min-_max)*i,_max) ]
        else:
            a += [ _min+abs(_min-_max)*i ]
    
    # print(a)

    # print(a.count(0))
    # print(a.count(1))
    # print(a.count(2))
    # print(a.count(3))
    # print(a.count(4))
    # print(a.count(5))
    # print(a.count(6))

    return np.random.choice(a)


if __name__ == "__main__":

    import matplotlib.pyplot as plt
    

    nb = RD_Gausse(50,100,sigma=1.5)
    nbs = []
    nbs_name = []

    for i in range(100000):
        nbs += [RD_Gausse(0,100,sigma=1.5)]
        nbs_name += [i]
    # the histogram of the data
    n, bins, patches = plt.hist(nbs, 100, density=1, facecolor='g', alpha=0.75)


    plt.axis([0, 100, 0, 0.05])
    plt.grid(True)
    plt.show()

    print(sum(nbs)/1000)

    input()