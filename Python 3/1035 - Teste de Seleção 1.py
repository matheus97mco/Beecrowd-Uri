A,B,C,D =  input().split()
A,B,C,D = int(A), int(B), int(C), int(D)

soma_CD = C+D
soma_AB = A+B

if (B > C) and (D > A) and (soma_CD > soma_AB) and ( C > 0) and (D > 0) and (A%2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')