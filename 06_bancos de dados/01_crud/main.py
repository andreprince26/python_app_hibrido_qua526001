from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker # orm banco de dados////

from entidades import criar_tb_pessoa
from modulo import limpar, cadastrar, listar, atualizar


def main():
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base) # engine cria coluna e linha/////
    Session = sessionmaker(bind=engine)
    session = Session() # cria uma sessao apara o banco de dados////

    limpar()
    while True:
        print(f"{'-'*20} crud da cobra {'-'*20}\n")
        print("0 - sair do programa")
        print("1 - cadastrar nova pessoa")
        print("2 - listar pessoas cadastradas\n")
        print("3 - atualizar dados")
        opcao = input("opçao desejada: ").strip()
        limpar()
        match opcao:
            case "0":
                print("programa encerrado.")
                break
            case "1":
                print(cadastrar(session, Pessoa))
                continue
            case "2":
                listar(session, Pessoa)
                continue
            case "3":
                print(atualizar(session, Pessoa))
                continue
            case _:
                print("opçao invalida.")
                continue
    

    session.close()

if __name__ == "__main__":
    main()