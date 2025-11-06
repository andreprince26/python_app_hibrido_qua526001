# Class PAI////////
class Pessoa:
    def __init__(self, email, telefone):
        self.email = email
        self.telefone

class PessoaFisica(Pessoa): # Class FILHA///////
    def __init__(self, nome, cpf, idade, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__inti__(email=email, telefone=telefone)

class PessoaFisica(Pessoa): # Class FILHA//////
    def __init__(self, nome_fantasia, cnpj, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, telefone=telefone)
    