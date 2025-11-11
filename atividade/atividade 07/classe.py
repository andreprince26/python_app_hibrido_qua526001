# biblioteca

# class
class Conta:
    # consultor cria o objeto
    def __init__(self, titular, cpf, agencia, n_conta, saldo):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.n_conta = n_conta
        self.saldo = saldo
    
    def consulta_dados(self):
        print(f"nome do titular da conta: {self.titular}")
        print(f"cpf do titular da conta: {self.cpf}")
        print(f"agencia da conta: {self.agencia}")
        print(f"numero da conta: {self.n_conta}")
        print(f"saldo do titular da conta: {self.saldo:.2f}") # (2.f) e arrendonda pra duas casa decimal
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            return "saque nao permitido."
        
        

