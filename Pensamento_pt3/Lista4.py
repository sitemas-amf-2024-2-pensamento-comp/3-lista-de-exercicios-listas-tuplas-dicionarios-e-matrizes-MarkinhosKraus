# Peça ao usuário para digitar as idades de várias pessoas, até o usuário digitar o valor 0. Após, calcule a média das idades e apresente na tela.
lista_idade = []

while True:
    idades = int(input("Digite idades de pessoas:"))
    if idades > 0:
        lista_idade.append(idades)
    elif idades == 0:
        media = sum(lista_idade) / len(lista_idade)
        print (lista_idade)
        print (media)
        break