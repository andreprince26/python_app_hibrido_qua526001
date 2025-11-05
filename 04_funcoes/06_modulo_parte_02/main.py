# funçao principal
def main():
    # entrada de dados
    nome = input("informe seu nome: ").strip().title()
    idade = int(input("informe sua idade:").strip())

# operador ternario
    resultado = "e maior de idade." if idade >= 18 else  "e menor de idade."

# saida de dados
    print (f"{nome} {resultado}")

    # protege algoritmo princial
if __name__ == "__main__":
    main()



