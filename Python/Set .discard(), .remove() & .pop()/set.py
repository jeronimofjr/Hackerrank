x = int(input())
elementos = set(map(int, input().split()))

for i in range(int(input())):
    comando = input().split()
    if comando[0] == 'pop':
        elementos.pop()
    elif comando[0] == 'remove':
        elementos.remove(int(comando[1]))
    else:
        elementos.discard(int(comando[1]))

print(sum(elementos))
