def calcula_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media  # Retorna o valor da média

# Corrigindo o nome da função chamada
print('Média:', calcula_media(10, 20, 30, 40))  # Chama a função correta e imprime a média

# Definindo uma função normal
def somar_3(x):
    return x + 3

# Usando uma função lambda para somar 3
somar = lambda x: x + 3

print('Somando 3 a um número:', somar(5))  # Exibe o resultado de somar 3 a 5
