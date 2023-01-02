x = y = 1
while x != 0 and y != 0:
    x,y = input().split()
    x,y = int(x),int(y)
    if x > 0 and y > 0:
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x > 0 and y < 0:
        print('quarto')