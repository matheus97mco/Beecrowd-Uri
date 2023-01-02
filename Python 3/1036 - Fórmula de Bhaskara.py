import math

A,B,C =  input().split()
A,B,C = float(A), float(B), float(C)

delta = B*B - 4*A*C 

if (A==0) or (delta<0):
    print('Impossivel calcular')
else:
    R1 = (-B + math.sqrt(delta)) / (2*A)
    R2 = (-B - math.sqrt(delta)) / (2*A)
    print('R1 = %.5f'%R1)
    print('R2 = %.5f'%R2)