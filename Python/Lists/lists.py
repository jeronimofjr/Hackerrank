def listas(n):
    lista = []
    for i in range(n):
        comando = input().split()
        if comando[0] == "insert":
            lista.insert(int(comando[1]), int(comando[2]))
        elif comando[0] == "print":
            print(lista)
        elif comando[0] == "remove":
            lista.remove(int(comando[1]))
        elif comando[0] == "append":
            lista.append(int(comando[1]))
        elif comando[0] == "sort":
            lista.sort()
        elif comando[0] == "pop":
            lista.pop()
        elif comando[0] == "reverse":
            lista.reverse()

n = int(input())
listas(n)