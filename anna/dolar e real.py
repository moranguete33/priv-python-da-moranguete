# autor: anna

# conversão de real para dolar

def obter_valor_dolar():
    return float(input('Digite o valor do dólar hoje: '))

def obter_valor_real():
    return float(input('Qual o valor em real que deseja converter: '))

def converter_real_para_dolar(real, dolar):
    return real / dolar

def exibir_resultado(valor_convertido):
    print(f'Valor convertido para dólar U$: {valor_convertido:.2f}')


def main():
    dolar = obter_valor_dolar()
    real = obter_valor_real()
    conversao = converter_real_para_dolar(real, dolar)
    exibir_resultado(conversao)


# Executa o programa
main()
