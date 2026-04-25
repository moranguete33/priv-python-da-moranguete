# autor: anna

# codigo sem funcoes

# calculadora sem funcoes

# valor1 = float(input('Digite o primeiro valor: '))
# valor2 = float(input('Digite o segundo valor: '))

# soma = valor1 + valor2
# subtracao = valor1 - valor2
# multiplicacao = valor1 * valor2
# divisao = valor1 / valor2

# print(f'O resultado da soma é: {soma}')
# print(f'O resultado da subtração é: {subtracao}')
# print(f'O resultado da multiplicação é: {multiplicacao}')
# print(f'O resultado da divisão é: {divisao}')


# codigo com funcoes

# variáveis para armazenar os valores
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

# Criando a função para realizar os cálculos
def calculos(a, b):
    soma=valor1+valor2
    subtracao=valor1-valor2
    mutiplicacao=valor1*valor2
    divisao=valor1/valor2

    print("O resultado da soma é: ",soma)
    print("O resultado da subtração é: ",subtracao)
    print("O resultado da mutiplicação é: ",mutiplicacao)
    print("O resultado da divisão é: ",divisao)


# Chamando a função
calculos(valor1, valor2)