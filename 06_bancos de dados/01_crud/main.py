from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker # orm banco de dados////

from entidades import criar_tb_pessoa
from modulo import limpar


def main():
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base) # engine cria coluna e linha/////
    Session = sessionmaker(bind=engine)
    session = Session() # cria uma sessao apara o banco de dados////

    limpar()
    # TODO: fazer o CRUD

    session.close()

if __name__ == "__main__":
    main()