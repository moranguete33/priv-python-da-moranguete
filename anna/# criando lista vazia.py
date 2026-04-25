# criando lista vazia
lista = []

# criando lista com a funao List()
lista_com_funcao = list ()
# lista de valores heterogeneos
aleatorio = [2, "a", 5.44, True]

# calculo media usando listas
notas = [6, 7, 5, 8, 9]
soma = 0 
x = 0

while x < 5: 
    notas[x] = float(input(f'Nota (x):'))
    soma += notas[x]
    x += 1

x = 0 

while x < 5:
    print(f'nota {x}: {notas[x]: .2f}')
    x += 1

    print(f"media: {soma / 5: . 2f}")