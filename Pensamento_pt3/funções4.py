# Escreva uma função chamada numeros_pares que receba uma lista de números e retorne uma nova lista contendo apenas os números pares da lista original.
def numeros_pares():
    lista_num = []
    lista_descartada = []
    for i in range(6):
        usuario = int(input("Digite um numero:"))
        if usuario % 2 == 0:
            lista_num.append(usuario)
        else:
            lista_descartada.append(usuario)
    return lista_num

pares = numeros_pares()

print ("Numeros pares são:", pares)