#tempo segundos
N = int(input())

horas = N//3600
r = N%3600

minutos = r//60

segundos = r%60

print(str(horas)+':'+str(minutos)+':'+str(segundos))