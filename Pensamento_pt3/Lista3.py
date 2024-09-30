# Crie uma lista chamada temperaturas com os valores [30, 22, 25, 28, 31, 27, 29]. Aumente todas as temperaturas menores que 25 em 5 graus
temp = [30, 22, 25, 28, 31, 27, 29]

for i in range(len(temp)):
    if temp[i] < 25:
        temp[i] += 5

print (temp)