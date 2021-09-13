x = int(input())

for i in range(x):
    a = int(input())
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    if len(A.intersection(B)) == len(A):
        print('True')
    else:
        print('False')
