class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome   # encapsular fazer dois __ na frente do nome ou algo do tipo
        self.__cpf = cpf
    
    # set envia
    # get recebe

    # metodos get pega o valor
    @property
    def nome(self):
        return self.__nome
    
    # metodo set indica o valor
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf (self, cpf):
        self.__cpf = cpf

     
