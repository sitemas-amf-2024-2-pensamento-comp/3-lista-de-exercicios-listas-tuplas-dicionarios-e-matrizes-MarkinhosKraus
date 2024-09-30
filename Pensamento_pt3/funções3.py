# Escreva uma função chamada contar_elementos que receba uma lista e um elemento como parâmetros e retorne a quantidade de vezes que o elemento aparece na lista.
def conta_elementos():
    lista_elemento = []
    for i in range(6):
        try:
            usuario = int(input("Digite um numero:"))
            lista_elemento.append(usuario)
        except ValueError:
            print ("Erro . . .")
    if lista_elemento:
        numero_mais_repetido = max(set(lista_elemento), key=lista_elemento.count)
        quantidade_repeticoes = lista_elemento.count(numero_mais_repetido)
        print(f"O número mais repetido é {numero_mais_repetido} e aparece {quantidade_repeticoes} vez(es).")
    else:
        print("Nenhum número foi digitado.")

    return lista_elemento 

lista_numeros = conta_elementos()
