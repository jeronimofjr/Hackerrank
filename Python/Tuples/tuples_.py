if __name__ == '__main__':
    n = raw_input()
    integer_list = raw_input()
    integer_list = integer_list.split()
    lista = []
    for i in range(int(n)):
        lista.append(int(integer_list[i]))
    tupla = tuple(lista)
    print(hash(tupla))
