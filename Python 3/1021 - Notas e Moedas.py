N = float(input())

if (0 < N) and (N < 1000000):
#notas
    N100 = N//100
    r = N%100

    N50 = r//50
    r = r%50
    
    N20 = r//20
    r = r%20
    
    N10 = r//10
    r = r%10
    
    N5 = r//5
    r = r%5
    
    N2 = r//2
    r = r%2
#moedas    
    M1 = r//1
    r = r%1
    
    M50 = r//0.50
    r = r%0.50 
    
    M25 = r//0.25
    r = r%0.25 
    
    M10 = r//0.10
    r = r%0.10
    
    M5 = r//0.05
   
    M01 = r%0.05*100

    print('NOTAS:')
    print(int(N100),'nota(s) de R$ 100.00')
    print(int(N50),'nota(s) de R$ 50.00')
    print(int(N20),'nota(s) de R$ 20.00')
    print(int(N10),'nota(s) de R$ 10.00')
    print(int(N5),'nota(s) de R$ 5.00')
    print(int(N2),'nota(s) de R$ 2.00')
    
    print('MOEDAS:')
    print(int(M1),'moeda(s) de R$ 1.00')
    print(int(M50),'moeda(s) de R$ 0.50')
    print(int(M25),'moeda(s) de R$ 0.25')
    print(int(M10),'moeda(s) de R$ 0.10')
    print(int(M5),'moeda(s) de R$ 0.05')
    print(round(M01),'moeda(s) de R$ 0.01')