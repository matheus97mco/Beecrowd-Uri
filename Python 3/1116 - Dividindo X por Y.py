N = int(input())
cont = 0 

while cont < N:
    x,y = input().split()
    x,y = float(x),float(y)
    cont+=1
    if y == 0:
        print('divisao impossivel')
    else:
        divisao = x / y
        print('%.1f'%divisao)