def palindromo(lista, lista_invertida):
    resultados = [lista == lista_invertida for lista, lista_invertida in zip(lista, lista_invertida)]
    return resultados

texto = ["ovo", "snivy", "ata"]
texto_invertido = [palavra[::-1] for palavra in texto]

# Verificação
resultados = palindromo(texto, texto_invertido)
for palavra, resultado in zip(texto, resultados):
    print(f"{palavra} palíndromo: {resultado}")

