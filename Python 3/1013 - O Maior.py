A,B,C = input().split()
A,B,C = int(A), int(B), int(C)

maiorAB = (A+B+abs(A-B))/2
maiorAB_C = (maiorAB+C+abs(maiorAB-C))/2

print(int(maiorAB_C),'eh o maior')

