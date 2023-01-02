n = int(input())
x = 1
if n < 10000:
    while x < 10001:
        x += 1
        if x%n == 2:
            print(x)  
            
            
