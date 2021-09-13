amount_integers = int(input())
integers = input().split()

print(all([int(i) > 0 for i in integers]) and any([i[0] == i[-1] for i in integers]))
