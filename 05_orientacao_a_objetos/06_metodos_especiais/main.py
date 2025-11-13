import os

from classes import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    pessoa = Pessoa(nome="", idade=0, genero="", telefone="")

    pessoa.nome = input("informe o nome: ").strip().title()
    pessoa.idade = int(input("informe o idade: ").strip())
    pessoa.genero = input("informe o genero: ").strip().lower()
    pessoa.telefone = input("informe o telefone: ").strip()

    # saida de dados/////
    print(pessoa)
    print(f"idade: {len(pessoa)}")

if __name__ == "__main__":
    main()