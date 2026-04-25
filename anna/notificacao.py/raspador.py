
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

navegador.get("https://google.com.br")
time.sleep(60)