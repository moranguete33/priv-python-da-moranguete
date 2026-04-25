# autor: anna

# lista de notas
notas = [0] * 7  # cria lista com 7 posições

soma = 0 
x = 0

# entrada das 7 notas
while x < 7: 
    notas[x] = float(input(f'Nota {x}: '))
    soma += notas[x]
    x += 1

x = 0 

# exibição das notas
while x < 7:
    print(f'Nota {x}: {notas[x]:.2f}')
    x += 1

# cálculo da média
print(f"Média: {soma / 7:.2f}")