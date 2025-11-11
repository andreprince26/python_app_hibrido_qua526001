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
def main ():    
    while True:
        
        print("1 - inserir dados do usuario")
        print("2 - inserir dados da empresa")
        print("3 - exibir dados do usuario")
        print("4 - exibir dados do usuario")
        print("5 - sair do programa")
        opcao = input("opçao desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                usuario.nome = input("informe seu nome: ").strip().title()
                usuario.cpf = input("informe seu cpf: ").strip()
                usuario.idade = int(input("informe seu idade: ").strip())
                usuario.email = input("informe seu email: ").strip().lower()
                usuario.telefone = input("informe seu telefone: ").strip()
                          
                limpar()
                continue
           
            case "2":
                empresa.name_fantasia = input("informe o nome da empresa:").strip().title()
                empresa.cnpj = ("informe o cnpj: ").strip()
                empresa. email = input("informe o e-mail da empresa: ").strip().lower()
                empresa.telefone = input("informe o telefone da empresa: ").strip()

                limpar()
                continue
            case"3":
                usuario.exibir_dados()
                continue
            case"4":
                  empresa.exibir_dados()
def main():
            



if __name__ == "__main__":
    main()

