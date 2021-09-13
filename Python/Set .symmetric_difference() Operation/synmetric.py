
qtd_ingles = input()
ingles = set(input().split())
qtd_frances = input()
frances = set(input().split())

print(len(ingles.symmetric_difference(frances)))
