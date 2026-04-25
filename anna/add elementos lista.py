# Criando uma lista vazia
compras = []

# Adicionando itens um por um
compras.append("arroz")
compras.append("feijão")
compras.append("macarrão")

print(compras)  # ['arroz', 'feijão', 'macarrão']


# lista de compras

compras = [ ]
i = 0

print("usando o metodo append com While")

while i < 10:
    item = input("insira o item para salvar na lista de compras: ")
    compras.append(item)
    