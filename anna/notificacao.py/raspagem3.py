from selenium import webdriver # O Controle principal do navegador
from selenium.webdriver.chrome.service import Service # Gerencia o Serviço de driver no Windows
from webdriver_manager.chrome import ChromeDriverManager # Faz Download automatico do Driver Correto
from selenium.webdriver.common.by import By # Permite Localizar os elementos por ID, Classe ou Xpath
import time

# Estrutura
# Configuração Automática: O Service vai baixar o driver compatível sozinho

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#DEFINE um tempo de espera padrão (se a internet estiver lenta, aguarde 10s)

navegador.implicitly_wait(10)

print("Acessando um site alvo")
navegador.get("https://g1.globo.com")
time.sleep(10)

print("Buscando o Alvo no site ...")

# logo = navegador.find_element(By.XPATH,"/html/body/header/div/div/div/a")

endereco = "/html/body/div[2]/main/div[3]/div[2]/div[1]/h1"
manchete = navegador.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div[2]/div[1]/h1")
manchete = globo.text


print("O Texto extraido foi: ",manchete)