x = 1 
p = 0
i = 0
pos = 0
neg = 0

while x < 6:
    x += 1
    n = int(input())
    if (n%2 == 0):
        p += 1
    elif (n%2 != 0):
        i += 1
        
    if (n > 0):
        pos += 1
    elif (n < 0):
        neg += 1
print(p,'valor(es) par(es)')
print(i,'valor(es) impar(es)')
print(pos,'valor(es) positivo(s)')
print(neg,'valor(es) negativo(s)')