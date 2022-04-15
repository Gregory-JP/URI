import math

def calc_acceleration(v, t):
    if(t == 0):
        return 0
    return v/t

def calc_distance(v0, t, a):
    return v0*(2*t)+(a*math.pow(2*t, 2))/2

while True:
    try:
        v, t = [int(x) for x in input().split()]
        #a = calc_acceleration(v, t)
        #print(calc_distance(v, t, a))
        print(v*t*2)
    except EOFError:
        break