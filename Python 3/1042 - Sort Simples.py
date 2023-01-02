A,B,C = input().split()
A,B,C = int(A), int(B), int(C)

if A > B and A > C and B > C:
    print(C)
    print(B)
    print(A)
elif A > B and A > C and B < C:
    print(B)
    print(C)
    print(A)
elif B > A and B > C and A > C:
    print(C)
    print(A)
    print(B)
elif B > A and B > C and A < C:
    print(A)
    print(C)
    print(B)
elif C > A and C > B and A > B:
    print(B)
    print(A)
    print(C)
else:
    print(A)
    print(B)
    print(C)

print()    
print(A)
print(B)
print(C)