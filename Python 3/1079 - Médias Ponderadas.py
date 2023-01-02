n = int(input())
x = 0

while x < n:
    x += 1
    a,b,c = input().split()
    a,b,c = float(a),float(b),float(c)
    media = (a*2 + b*3 + c*5)/10
    print ('%.1f'%media)
    