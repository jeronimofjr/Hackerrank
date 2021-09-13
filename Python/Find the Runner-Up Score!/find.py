n = int(input())
array = input().split()

def converter(lista):
    return [int(x) for x in lista]

array = converter(array)

array.sort()
array.reverse()

qtd = array.count(max(array))
maior = max(array[qtd:])

print(maior)