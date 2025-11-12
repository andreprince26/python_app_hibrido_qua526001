from classes import Pessoa

def main():
    usuario = Pessoa(nome="", cpf="")

    usuario.nome = input("informe seu Nome: ").strip().title()
    usuario.cpf = input("infporme seu CPF: ").strip()

    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
                   
if __name__ == "__main__":
    main()