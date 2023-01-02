x = 1 #repetição
a = 0 #incrementador pra positivos
m = 0.0 #incrementador pra media

while x < 7:
    x += 1
    n = float(input())
    if n > 0:
        a += 1
        m += n 
        media = m/a
print(a,'valores positivos')
print('%.1f'%media)    
    
    