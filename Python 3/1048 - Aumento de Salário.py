salario = float(input())

if salario >= 0 and salario <= 400.00:
    novo = salario + (salario * 0.15)
    reajuste = novo - salario
    p = 15
    
elif salario >= 400.01 and salario <= 800.00:
    novo = salario + (salario * 0.12)
    reajuste = novo - salario
    p = 12
    
elif salario >= 800.01 and salario <= 1200.00:
    novo = salario + (salario * 0.10)
    reajuste = novo - salario
    p = 10
    
elif salario >= 1200.01 and salario <= 2000.00:
    novo = salario + (salario * 0.07)
    reajuste = novo - salario
    p = 7
    
elif salario > 2000.00:
    novo = salario + (salario * 0.04)
    reajuste = novo - salario
    p = 4
    
print('Novo salario: %.2f'%novo)
print('Reajuste ganho: %.2f'%reajuste)
print('Em percentual:',p,'%')
    
    
    
    