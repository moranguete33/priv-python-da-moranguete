frutas = ["maçã", "banana", "laranja", "uva", "manga"]
#          0        1         2         3       4


# pegar do indice 1 ate o 3

# Pegar do índice 1 até o 3 (o 3 NÃO entra!)
print(frutas[1:3])     # ['banana', 'laranja']

# Pegar do começo até o índice 2
print(frutas[:2])      # ['maçã', 'banana']

# Pegar do índice 2 até o final
print(frutas[2:])      # ['laranja', 'uva', 'manga']

# Pegar TUDO (cópia completa!)
print(frutas[:])       # ['maçã', 'banana', 'laranja', 'uva', 'manga']