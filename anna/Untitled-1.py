# autor: anna

# Função para encontrar o maior número
def maximo(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2

# Entrada dos números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = maximo(numero1, numero2)
print("O maior valor é:", resultado)

# Área do triângulo
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area_triangulo = (base * altura) / 2
print("Área do triângulo:", area_triangulo)
