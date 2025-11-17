# entidade e um atributo  
from sqlalchemy import Column, String, Integer, Date

# funçao que cria o banco de dados e as entidade
def criar_tb_pessoa(engine, Base):
    # tratamento de exceçao
    try:
        class Pessoa(Base):
            __tablename__ = "pessoa"

            # atributos
            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            nascimento = Column(Date, nullable=False)
            email = Column(String, nullable=False, unique=True)
            genero = Column(String, nullable=True)
        
        Base.metadata.create_all(engine)

        return Pessoa
    except Exception as e:
        print(f"nao foi possivel conectar o banco de dados. {e}.")