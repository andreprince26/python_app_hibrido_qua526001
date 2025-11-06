# biblioteca 
import os

# classe pessoa//////
class Pessoa:
    # atributos da classe/////
    nome = "andre"
    idade = 40
    email = "andreprince.com"

    # metodo ou funçao e uma açao//////
    def exibir_dados(self):  # cria metodo sem parametro sempre tem q colocar(self) e (def)/////
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"email: {self.email}")

if __name__ == "__main__":
    # instancia a classe (cria novo objeto)
    usuario = Pessoa()
    
# limpar console////////
    os.system("cls" if os.name == "nt" else "clear")

    # saida de dados//////////
    usuario.exibir_dados()

