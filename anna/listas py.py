# autor: anna
# projeto copia de listas 

# em python, as listas sao um recurso muito poderoso, mas todo poder 
# trás responsabilidades, vamos ver um efeito colateral ao copiar
# uma lista

L = [1, 2, 3, 4, 5]

V = L 

print("essa é a lista L: " , L)
print("essa é a lista V: " , V)

V[0] = 6

print("essa é a lista V: " , V)
print("essa é a lista L: " , L)

L = [1, 2, 3, 4, 5]
V = L [:]
V[0] = 6 

print("essa é a lista V: " , V)
print("essa é a lista L: " , L)