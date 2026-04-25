# autor : anna 
# projeto: fazer funcao que indica que e numero par

numero = int(input(' insira um numero '))

def ehpar (numero): 
    print ('o numero digitado é par? \n', numero % 2 == 0)
    

ehpar (numero)

def par_ou_impar (valor) :
    #if valor % 2 == 0:
    if ehpar(valor):
     print('o numero é par')
    else:
     print('o numero é impar')

par_ou_impar(numero)
