
# banco.py
import os

from classe import Conta

def limpar():
    os.system("cls" if os.name == "nt" else "clear")
              
def main():
    limpar()

    cc = Conta(titular="", cpf="", agencia="1234-5", n_conta="12345-6", saldo=0)
    
    cc.titular = input("informe o nome do titular: ").strip().title()
    cc.cpf = input("informe o cpf do titular: ").strip()

    limpar()

    while True: # laço de repeticao menu
        print("1. consultar dados")
        print("2. Depositar valor")
        print("3. sacar valor")
        print("4.  sair do programa")
        opcao = input("opçao desejada: ").strip()

        match opcao:
            case "1":
                cc.consulta_dados()
                continue
            case "2":
                valor = float(input("informe o valor do depositor: R$").strip().replace(",","."))
                print(f"depositor efetuado com sucesso. saldo atual: R${cc.depositar(valor):.2f}")
                continue
            case "3":
                valor = float(input("informe o valor do saque: ").strip().replace(",","."))
                print(f"valor sacado: R$ {cc.sacar(valor)}")
                continue
            case "4":
                print("programa encerrado")
                break
            case _:
                print("opçao invalida.")
                continue
        
if __name__ == "__main__":
    main()
        















        