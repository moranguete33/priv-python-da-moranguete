import faker as apelido

falso_dado = apelido.Faker("pt_BR")

for _ in range(30): 

    nome = falso_dado.name()
    apelido.Faker.seed(1)
    print(f"telefone: {falso_dado.phone_number()}")
    print(f"endereço: {falso_dado.address()}")

