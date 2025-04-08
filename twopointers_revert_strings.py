def revert(lista):
    p1,p2 = 0,0                                     #ponteiros
    lista_final = ''                                #lista que terá os elementos

    while p2 < len(lista):                          #percorrendo os elemetos da string menos o último
        if lista[p2] != ' ':                        #se onde p2 estiver for igual a espaço, continua percorrendo a string
            p2 += 1
        else:                                       #do contrario
            lista_final += lista[p1:p2 +1][::-1]    #inverte a palavra, pois chegou ao fim do texto/palavra
            p1 = p2                                 #deixa o p1 no início da próxima palavra, após uma inverção
            p2 +=1                                  #continua


    lista_final += ' '                              #adicionando o espaço entre os últimos elemetos 
    lista_final += lista[p1:p2 +1][::-1]            #e invertendo o último
    return lista_final[1:]

texto = ('snivy servine serperior')
print(revert(texto))