#  autor: anna
# projeto: trabalhando com índices
# programa que le cinco numeros e armazena em uma lista e depois
# solicite ao usuário que escolha um número a mostrar

numeros = [0] * 5
x = 0

# leitura dos números
while x < 5:
    numeros[x] = int(input(f"Número {x + 1}: "))
    x += 1

# escolha do usuário
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))

    if escolhido == 0:
        break

    if 1 <= escolhido <= 5:
        print(f"Você escolheu o número: {numeros[escolhido - 1]}")
    else:
        print("Posição inválida!")
