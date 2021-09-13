string = input()

contador = 0
lista = []
i = 0

while i < len(string):
    aux = string[i]
    while i < len(string) and aux == string[i]:
        contador += 1
        i += 1
    lista.append((contador, int(aux)))
    contador = 0
print(*lista)