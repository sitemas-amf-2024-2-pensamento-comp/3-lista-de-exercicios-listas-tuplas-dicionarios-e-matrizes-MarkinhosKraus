# Escreva uma função chamada fibonacci que receba um número n e retorne uma lista contendo os n primeiros números da sequência de Fibonacci. A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.
def fibonacci(n):
    fibo = []
    a, b = 0, 1
    for i in range(n):
        fibo.append(a)
        a, b = b, a + b
    return fibo

n = int(input("Digite um numero: "))
print (fibonacci(n))