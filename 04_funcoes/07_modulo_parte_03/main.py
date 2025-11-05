# bibliotecas
from modulo import limpar, primeiro_grau, segundo_grau

def main():
    limpar()
    while True:     # laço de repetiçao
        print("0 - sair do progroma")
        print("1 - calcular equaçao do 1° grau")
        print("2 - calcular equaçao do 2º grau")
        opcao = input("opçao desejada: ").strip()
        match opcao:
            case "0":
                limpar()
                print("programa encerrado.")
            case "1":
                a = float(input("informe o valor de 'a': ").strip().replace(",","."))
                b = float(input("informe o valor de 'b': ").strip().replace(",","."))
                limpar()
                x = primeiro_grau(a, b)
                print(f"x = {x}")
                continue
            case "2":
                a = float(input("informe o valor de 'a': ").strip().replace(",","."))
                b = float(input("informe o valor de 'b': ").strip().replace(",","."))
                c = float(input("informe o valor de 'c': ").strip().replace(",","."))
                limpar()
                resultados = segundo_grau(a, b, c)
                for x in resultados:
                    print(f"x = {x}")
                    continue
            case _:
                limpar()
                print("opçao invalida.")
                continue

if __name__ == "__main__":
    main()
