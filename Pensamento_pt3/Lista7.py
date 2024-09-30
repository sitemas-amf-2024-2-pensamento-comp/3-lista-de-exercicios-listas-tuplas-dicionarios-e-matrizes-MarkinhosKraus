# Peça ao usuário para digitar duas sequências de 5 números e armazene-as em duas listas distintas. Em seguida, faça um programa que procure os elementos comuns entre elas e os junte em uma terceira lista.
lista1 = []
lista2 = []

for i in range(6):
    usuario = int(input("Digite um numero:"))
    lista1.append(usuario)

for i in range(6):
    usuario = int(input("Digite um numero:"))
    lista2.append(usuario)

lista_comum = [num for num in lista1 if num in lista2]

print("Primeira lista:", lista1)
print("Segunda lista:", lista2)
print("Elementos comuns:", lista_comum)