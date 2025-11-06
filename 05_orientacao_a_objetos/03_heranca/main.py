# bibliotecas
import os

# nossa biblioteca
from classes import PessoaFisica, PessoaJuritica

#funçao limpar tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

    #funcao principal
def main():
    usuario = PessoaFisica(nome="", cpf="", idade=0, email="", telefone="")
    empresa = PessoaJuritica(nome_fantasia="", cpf="", idade=0, email="", telefone="")

    limpar()
    while True:
def main ():
            case "1"
             print("1 - inserir dados do usuario")
            print("2 - inserir dados da empresa")
             print("3 - exibir dados do usuario")
            print("1 - exibir dados do usuario")
            print("5 - sair do programa")
        opcao = input("opçao desejada: ").strip()
        limpar()
        match opcao:
            case "1"
               usuario.nome = input("informe seu nome: ").strip().title
               usuario.cpf = input("informe seu nome: ").strip()
               usuario.idade = int(input("informe seu nome: ").strip())
               usuario.email = input("informe seu nome: ").strip().lower()
               
             contiune
def main():


if __name__ == "__main__":
    main()

