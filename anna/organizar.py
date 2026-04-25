# autor: anna
# projeto renomear arquivos 

# importar ação do OS(sistema operacional - windows)
import os 

# pasta que desejo anallisar 
pasta = "arquivos" 

# listar arquivos das pastas 
lista_arquivos = os.listdir(pasta)

# loop dos arquivos
contador = 1 
for arquivo in lista_arquivos: 

# um arquivo tem nome e extensão
# separar o nome da extensão 
# boleto_a1327_2026.pdf
    nome, extensao = os.path.splitext(arquivo)

# geração do novo nome
    novo_nome = f"boleto_empresa_arquivo{contador: 03d}{extensao}"

# caminho do arquivo antigo
    caminho_antigo = os.path.join(pasta,arquivo)
# caminho do novo arquivo 
    caminho_novo = os.path.join(pasta,novo_nome)
# ação de renomear os arquivos
    os.rename(caminho_antigo, caminho_novo) 

# contador
# contador = contador + 1
    contador+= 1

# mensagem de sucesso 
print("\narquivos renomeados com sucesso!")