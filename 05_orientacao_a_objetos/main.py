from classes import Pessoa

def main():
    usuario = Pessoa(nome="", cpf="")

    usuario.nome = input("informe seu nome: ").strip().title()
    usuario.cpf = input("infporme seu cpf: ").strip()

    print(f"nome: {usuario.nome}")
    print(f"cpf: {usuario.cpf}")
                   
if __name__ == "__main__":
    main()