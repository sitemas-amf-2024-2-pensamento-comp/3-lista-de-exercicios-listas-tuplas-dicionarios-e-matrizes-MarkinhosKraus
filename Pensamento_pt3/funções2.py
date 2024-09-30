# Crie uma função chamada media que receba uma lista de números e retorne a média desses números. A média é calculada somando todos os números da lista e dividindo o total pelo número de elementos na lista.
def media():
    lista_num = []
    
    for i in range(6):
        try:
            usuario = int(input("Digite um numero:"))
            lista_num.append(usuario)
        except ValueError:
            print ("Erro. . .")
    if lista_num:
        media = sum(lista_num) / len(lista_num)
        return media
    else:
        return None
    
media = media ()

print ("A media dos alunos é:", media)
    