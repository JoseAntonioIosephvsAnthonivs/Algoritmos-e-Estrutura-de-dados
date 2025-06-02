def binary_search(lista, n_desejado, p1, p2):
    while p1 <= p2:  # abranje até o último elemento
        meio = (p1 + p2) // 2
        if lista[meio] < n_desejado:
            p1 = meio + 1
        elif lista[meio] > n_desejado:
            p2 = meio - 1  # impede loop infinito
        else:
            return meio  # retorno do proprio indice, em caso de ser igual ao numero desejado
    return -1  # número fora da lista

def exponential_search(fila, numero_d):
    if fila[0] == numero_d:
        return 0 # sucesso, não há erro
    tamanho = len(fila) # variavel com tamanho da fila
    np2 = 1 #novo ponteiro2

    while np2 < tamanho and fila[np2] < numero_d:
        p1 = np2     #ou p1 = np2 // 2 # e o novo ponteiro1 pega o valor antigo do novo ponteiro2  

        np2 *= 2 # o novo ponteiro2 será dobrando enquanto for menor que o tamanho da fila e  for menor que o num desejado

    p2 = min(np2, tamanho - 1)
    return binary_search(fila,numero_d, p1, p2)


fila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numero_d = int(input('Digite o número desejado: '))
indice = exponential_search(fila, numero_d)

if indice != -1: # caso o numero procurado esteja na lista:
    print(f'Número achado no índice: {indice}')
else: # caso o numero procurado não esteja na lista:
    print('Número não encontrado.')
