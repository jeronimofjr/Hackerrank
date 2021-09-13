from collections import Counter

shoes_qtd = int(input())
shoes = Counter(map(int, input().split()))
customers = int(input())

money = 0
for i in range(customers):
    number, price = map(int, input().split())
    if shoes[number]:
        money += price
        shoes[number] -= 1

print(money)