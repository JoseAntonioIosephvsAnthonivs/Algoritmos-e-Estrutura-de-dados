def binary_search(lista,n_desejado):
    p1 = 0 #ponteiro 1, começa na esquerda
    p2 = len(lista) -1 #ponteiro 2, começa na direita
    passos = 0 #contador de passos

    while p1 < p2: #'enquanto o p1 for menor que o p2' pois quando p1 for igual a p2 acaba o algoritmo
        passos += 1 #acrescimo nos passos
        meio = int((p1+p2)/2) #meio do array
        
        if n_desejado not in lista: #se o valor n for entre 0 a 10
            print('Valor não encontrado. Digite um número entre 0 a 10')
            return

        if lista[meio] < n_desejado: # se o meio do array for menor que o numero desejado
            p1 = meio + 1 #p1 avança 1 posição após o meio
        elif lista[meio] > n_desejado: #se o meio for maior 
            p2 = meio # - 1
        else: #numero encontrado
            print(f'O número desejado foi o {n_desejado}, achado em: {passos} passos.')
            return n_desejado #numero encontrado

    return -1

try: #digitando um numero entre 0 a 10:
    n = int(input('Digite o número que deseja buscar(0 a 10): '))
    numeros = [0,1,2,3,4,5,6,7,8,9,10,11] #array com um dos números a ser buscado
    binary_search(numeros,n)

except ValueError: # se for digitado outro tipo de caractere
    print('Valor não encontrado. Digite um número entre 0 a 10.')
