
x = int(input())

dic = {}
for i in range(x):
    a = input().split()
    dic[a[0]] = list(map(float, a[1:]))

print('{:.2f}'.format(sum(dic.get(input()))/3))
