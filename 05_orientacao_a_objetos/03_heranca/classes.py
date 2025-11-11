# Class PAI////////
class Pessoa:
    def __init__(self, email, telefone):
        self.email = email
        self.telefone
    def exibir_dados(self):
        print(f"email: {self.email}")
        print(f"telefone: {self.telefone}")

class PessoaFisica(Pessoa): # Class FILHA///////
    def __init__(self, nome, cpf, idade, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__inti__(email=email, telefone=telefone)
    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"cpf: {self.cpf}")
        print(f"idade: {self.idade}")
        super().__init__
        

class PessoaJuritica(Pessoa): # Class FILHA//////
    def __init__(self, nome_fantasia, cnpj, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, telefone=telefone)

    def exibir_dados(self):
        print(f"nome da empresa: {self.nome_fantasia}")
        print(f"cnpj: {self.cnpj}")
        super().exibir_dados()
    