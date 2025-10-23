# importaçao de biblioteca
import os

# loop
while True:
    # limpeza de console
    os.system("cls")

    # tratamento de exceçao
    try:
        nome = input ("Informa o nome: ").strip().title()
        email = input("Informe o e-mail: ").strip().lower()
        cpf = input("Informe o CPF: ").strip()

        # Limpeza de console
        os.system("cls")

        # saida de dados
        print(f"nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")

        # menu
        print("1 - inserir novos dados.")
        print("2 - sair do programa.") 

        opcao = input("Opçao desejada: ").strip()
        #verifica a opçao escolhida
        match opcao:
            case "1":
             continue
            case "2":
              print("programa encerrado.")
              break
            case _:
              print("opçao invalida.")
              break
    except:
        print("Nao foi possivel receber informaçoes.")