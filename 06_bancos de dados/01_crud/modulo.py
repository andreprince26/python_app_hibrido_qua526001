
import os
from datetime import datetime

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') 
    
def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        genero = input("Informe o gênero: ").strip()
        data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ").strip()
        data_nascimento  = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        email = input("Informe o e-mail: ").strip().lower()
        
        # filtro atributo email das pessoas que possuem mesmo email informado       
        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all()  
        
        if email in [pessoa.email for pessoa in pessoas]:
            return "E-mail já cadastrado."
        else:
            nova_pessoa = Pessoa(
                nome=nome,
                genero=genero,
                data_nascimento=data_nascimento,
                email=email)
            
            # insert into pessoa
            
            session.add(nova_pessoa)
            session.commit()
            
            return f"Pessoa{nova_pessoa.nome} cadastrada com sucesso"    
    except Exception as e:
        print(f"Não foi possível cadastrar. {e}.") 
        
# read
def listar(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()
        
        print("Pessoas cadastradas:\n")
        
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Gênero: {pessoa.genero}")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
            print(f"\n{'-'*40}\n")
          
    except Exception as e:    
        print(f"Não foi possível listar. {e}.")


# update
def atualizar(session, Pessoa):
    id_pessoa = ""
    email = ""
    novo_nome = ""
    novo_email = ""
    nova_data_nascimento = ""
    novo_genero = ""

    try:
        print ("escolha o campo que deseja pesquisar: ")
        print("1 - id")
        print("2 - e-mail")
        print("3 - retornar")
        opcao = input("opçao desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                id_pessoa = input("informe o id: ").strip()
                pessoa = session.query(Pessoa).filtter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("informe o email: ").strip().lower()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
                return ""
            case _:
                return "opçao invalido."
        
        if pessoa:
            limpar()
            while True:
                print(f"id {pessoa.id_pessoa}")
                print("qual campo deseja alterar:\n")
                print(f"1 - nome: {pessoa.nome}")
                print(f"2 - email: {pessoa.email}")
                print(f"3 - data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
                print(f"4 - genero: {pessoa.genero}")
                print(f"5 - finalizar")
                campo = input("campo desejado: ").strip()
                limpar()
                match campo:
                    case "1":
                        novo_nome = input("informe o novo nome: ").strip().title()
                        continue
                    case "2":
                        novo_email = input("informe o novo email: ").strip().lower()
                        pessoas = session.query(pessoa).filter(Pessoa.email == novo_email).all()
                        if email in [pessoa.email for pessoa in pessoas]:
                            print("email ja cadastrado.")
                            continue
                    case "3":
                        nova_nascimento = input("informe a nova data de nascimento (dd/mm/aaaa): ").strip()
                        continue
                    case "4":
                        novo_genero = input("informe o novo genero: ").strip().lower()
                        continue
                    case "5":
                        
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        novo_nascimento = datetime.strftime (novo_nascimento, "%d/%m/%Y").date() if novo_nascimento != "" else pessoa.nascimento
                        novo_genero = novo_genero if novo_genero != "" else pessoa.genero
                        break
                    case _:
                        print("campo inexistente.")
                        continue
            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.nascimento = novo_nascimento
            pessoa.genero = novo_genero

            session.commit()

            return "dados atualizada com sucesso."
        else:
            return "Pessoa nao encontrada."
             
    except Exception as e:
        print(f"nao foi possivel alterar os dados. {e}.")





    

