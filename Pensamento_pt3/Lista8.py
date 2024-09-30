# Peça ao usuário para digitar uma sequência de 10 números. Em seguida, crie duas listas a partir desta sequência: uma contendo os números pares e outra contendo os números ímpares
pares = []
impares = []

for i in range(11):
    usuario = int(input("Digite um numero:"))
    if usuario % 2 == 0:
        pares.append(usuario)
    else:
        impares.append(usuario)
        
print ("Numeros pares:", pares)
print ("Numeros impares:", impares)
