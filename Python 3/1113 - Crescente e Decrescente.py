x = 0
y = 1
while x != y:
    x,y = input().split()
    x,y = int(x),int(y)
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
        
