import os

from classes import Parque

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    ingresso = Parque(nome="", idade=0, peso=0.0)

    ingresso.nome = input("informe o nome: ").strip().title()
    ingresso.idade = int(input("informe o idade: ").strip())
    ingresso.peso = float(input("informe o peso em kg: ").strip().replace(",","."))

    limpar()

    while True:
        print("1 - categoria infantil")
        print("2 - categoria juvenil")
        print("3 - categoria adulto")
        print("4 - sair do programa")
        opcao = input("opçao desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                print(ingresso.entrada_infantil())
                continue
            case "2":
                print(ingresso.entrada_juvenil())
                continue
            case "3":
                print(ingresso.entrada_adulto())
                continue
            case "4":
                print("programa encerrado.")
                break
            case _:
                print("opçao invalida.")
                continue
        

if __name__ == "__main__":
    main()