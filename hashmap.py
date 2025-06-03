#achar o primeiro charactere único
def first_uniq(texto: str) -> int:
    dicionario = {}
    for indice, charactere in enumerate(texto):
        if charactere not in dicionario:
            dicionario[charactere] = [indice, 1]
        else:
            dicionario[charactere][1] += 1
    
    for chave,valor in dicionario.items():
        if valor[1] == 1:
            print(f'o primeiro dígito não repetido é o: {chave} e está no índice: {valor[0]}')
            return valor[0]

digite = str(input('digite um texto: '))
first_uniq(digite)




