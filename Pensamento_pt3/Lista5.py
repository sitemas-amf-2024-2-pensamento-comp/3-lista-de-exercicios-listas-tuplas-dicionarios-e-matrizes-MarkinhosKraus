# Peça ao usuário para digitar uma sequência de 10 números. Após, procure o maior e o menor número e apresente na tela
lista_num = []

for i in range(11):
    num = int(input("Digite um numero:"))

    if num > 0:
        lista_num.append(num)
    else:
        print ("Numero invalido")
        break
        
if lista_num:
    maior_num = max(lista_num)
    menor_num = min(lista_num)
    print (lista_num)
    print ("Menor numero é:", menor_num, "\nMaior numero é:", maior_num)
else:
    print ("Erro. . .")