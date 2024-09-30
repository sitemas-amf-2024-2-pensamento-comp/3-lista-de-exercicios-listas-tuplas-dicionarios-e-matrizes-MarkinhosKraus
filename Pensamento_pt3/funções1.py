# Escreva uma função chamada maior_numero que receba uma lista de números como parâmetro e retorne o maior número da lista. Teste a função com diferentes listas de números.
def maior_numero():
    lista_num = []
    for i in range(5):
        try:
            usuario = int(input("Digite um numero:"))
            lista_num.append(usuario)
        except ValueError:
            print ("Erro. . .")

    if lista_num:   
        maior_num = max(lista_num)

    else:
        return None
    
    return maior_num

resultado = maior_numero()

print (resultado)
