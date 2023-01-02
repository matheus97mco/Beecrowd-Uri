x = int(input())
a = 0

if 1<= x and x<= 1000:
    while a < x:
        a += 1
        if a%2 != 0:
            print(a)
