from dataclasses import dataclass

# classes/////////
@dataclass
class Pessoa:
    # atributos ///////// set e get//////
    nome: str
    idade: int
    altura: float

# metodos
    def __str__(self):
        return f"Nome: {self.nome}\nidade: {len(self)}\nAltura: {self.altura}"
    
    def __len__(self):
        return self.idade
    
    def verificar_maioridade(self):
        return "é maior de idade" if len(self) >= 18 else " é menor de idade"



