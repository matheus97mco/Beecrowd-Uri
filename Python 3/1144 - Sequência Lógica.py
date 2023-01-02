import math

N = int(input())
n = N*2
cont = 1 

a = b = c = 1
print(a,b,c)
a = a 
b = (a**2)+1
c = (a**3)+1
print(a,b,c)

if N > 1 and N < 1000:
    while cont < N:
        cont +=1
        a += 1
        b = a**2
        c = a**3 
        print(a, b, c)
        b = (a**2) + 1 
        c = (a**3) + 1 
        print(a, b, c)
        
    