n = float(input())

if (0<=n) and (n<=25): #entre[0,25]
    print('Intervalo [0,25]')
elif (25<n) and (n<=50): #maior q 25 até 50(25,50] 
    print('Intervalo (25,50]')
elif (50<n) and (n<=75): #maior q 50 até 75(50,75] 
    print('Intervalo (50,75]')
elif (75<n) and (n<=100): #maior q 75 até 100(75,100]
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')