# area de um quadrado 

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

# Área do quadrado
lado = float(input("Digite o valor do lado do quadrado: "))
area_quadrado = lado ** 2
print("Área do quadrado:", area_quadrado)


