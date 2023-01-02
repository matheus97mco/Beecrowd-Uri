N = int(input())

if (0 < N) or (N < 1000000):
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
    
    N1 = r%2
    
    print(N)
    print(N100,'nota(s) de R$ 100,00')
    print(N50,'nota(s) de R$ 50,00')
    print(N20,'nota(s) de R$ 20,00')
    print(N10,'nota(s) de R$ 10,00')
    print(N5,'nota(s) de R$ 5,00')
    print(N2,'nota(s) de R$ 2,00')
    print(N1,'nota(s) de R$ 1,00')