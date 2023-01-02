A,B = input().split()
A,B = int(A), int(B)

if A>B:
    T_A = 24-A
    T = T_A + B 
    print('O JOGO DUROU',T,'HORA(S)')
elif B>A:
    T = B - A
    print('O JOGO DUROU',T,'HORA(S)')
else:
    T = 24
    print('O JOGO DUROU',T,'HORA(S)')