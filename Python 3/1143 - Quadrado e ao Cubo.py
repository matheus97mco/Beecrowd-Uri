import math

N = int(input())
cont = 0 
a = b = c = 0

if N > 1 and N < 1000:
    while cont < N:
        cont +=1
        a += 1
        b = a**2
        c = a**3 
        print(a, b, c)
    