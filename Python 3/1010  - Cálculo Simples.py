c1,n1,v1 = input().split()
c2,n2,v2 = input().split()

c1,n1,c2,n2 = int(c1),int(n1),int(c2),int(n2)
v1,v2 = float(v1),float(v2)

total1 = n1*v1
total2 = n2*v2

total = total1+total2

print('VALOR A PAGAR: R$ %.2f'%total)