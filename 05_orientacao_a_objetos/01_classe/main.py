# classe///////
class Pessoa:

    # construtor/////
    def __init__(self,nome, cpf, email,  idade):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"e-mail: {self.email}")
        print(f"Idade: {self.idade} anos")
        

# algoritimo principal objeto///////
if __name__ == "__main__":
    #instancia a classe
    usuario = Pessoa(nome="", cpf="", email="", idade=0)

    # entrada de dados//////
    usuario.nome = input("informe o nome: ").strip().title()
    usuario.cpf = input("informe o cpf: ").strip()
    usuario.email = input("informe o email: ").strip().lower()
    usuario.idade =  int(input("informe o idade: ").strip().strip())

    # saida de dados
    usuario.exibir_dados()


