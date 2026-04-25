# Pergunta quantos alunos vieram
quantidade = int(input("Quantos alunos vieram hoje? "))

# Lista para armazenar os nomes
lista_presenca = []

# Loop para coletar os nomes
for i in range(quantidade):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    lista_presenca.append(nome)

# Mostra a lista final
print("\nLista de Presença:")
for aluno in lista_presenca:
    print(aluno)

