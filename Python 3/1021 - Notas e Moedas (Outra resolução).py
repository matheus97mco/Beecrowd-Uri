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
    print('%.f nota(s) de R$ 100.00'%N100)
    print('%.f nota(s) de R$ 50.00'%N50)
    print('%.f nota(s) de R$ 20.00'%N20)
    print('%.f nota(s) de R$ 10.00'%N10)
    print('%.f nota(s) de R$ 5.00'%N5)
    print('%.f nota(s) de R$ 2.00'%N2)
    
    print('MOEDAS:')
    print('%.f moeda(s) de R$ 1.00'%M1)
    print('%.f moeda(s) de R$ 0.50'%M50)
    print('%.f moeda(s) de R$ 0.25'%M25)
    print('%.f moeda(s) de R$ 0.10'%M10)
    print('%.f moeda(s) de R$ 0.05'%M5)
    print('%.f moeda(s) de R$ 0.01'%M01)