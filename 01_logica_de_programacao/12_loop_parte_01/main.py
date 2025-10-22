# tratamento de exceçao
try:
    # entrada de dados
    numero = int(input("informe um numero inteiro: ").strip())

# laço de repetiçao
    while numero >= 0:
     print(numero)
    numero -= 1
except:
  print("nao foi possivel executar o contador.") 