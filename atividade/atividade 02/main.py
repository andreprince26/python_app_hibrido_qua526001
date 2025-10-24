import os # limpeza de tela
import time #contage regresiva

try: # so pra o programa nao quebra tem coloca except

    numero = int(input("digita um numero: ").strip())
    while numero >= 0:
        os.system("cls")  # limpa o console
        print(numero)
        time.sleep(4)
        numero -= 1 
        print("BOOOOMMMM!!!!")
except:
   print ("deu erro.") 


