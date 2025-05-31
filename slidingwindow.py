# Problema a ser resolvido será: achar qual a maior largura de substring com no max 2 ocorrências de um caractere. 
# while de fora aumenta a substring(ponteiro da direita) e while de dentro reduz a substring (ponteiro da esquerda)
# ['b','c','b','b','b','c','b','a']
def sliding_window(self,texto: str) -> int:
    p1, p2 = 0
    maxi = 1
    contador = {}
    contador[texto[0]] = 1
    

    while p2 < len(texto) -1:
        p2 +=1
        if contador.get(texto[p2]):
            contador[texto[p2]] += 1
        else:
            contador[texto[p2]] = 1
        
        while contador[texto[p2]] == 3:
            contador[texto[p1]] -= 1
            p1 += 1
    
        maxi  = max(maxi, p2-p1+1)
    
    return maxi
    print(contador)
    
z = ['b','a','d','b','b','a','d','b','a','b','c','d','a','b']
print(sliding_window(z))

