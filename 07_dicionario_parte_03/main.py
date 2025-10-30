# declaraçao de dicionario
veiculo = {
    'fabricante': "chevrolet",
    'modelo': "chevette",
    'ano': 1973,
    'cor': "branca",
    'placa': "DF-1973"
}

# exibir dados
for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")

    # usuario escolhe o campo que deseja mudar
while True:
    campo = input("informe o nome do campo que deseja alterar ou digite'sair para encerrar o programa: ").strip().lower()

    match campo:
        case "fabricante":
            veiculo['fabricante'] = input("informe o novo valor de 'fabricante'").strip()
        case "modelo":
            veiculo['modelo'] = input("informe o novo valor de 'modelo'").strip()              
        case "ano":
            veiculo['ano'] = int(input("informe o novo valor de 'ano'").strip())               
        case "cor":
            veiculo['cor'] = input("informe o novo valor de 'cor'").strip()              
        case "placa":
            veiculo['placa'] = input("informe o novo valor de 'placa'").strip()               
        case "sair":
            break                
        case _:
            print("valor invalido.")
            continue
            # mostra na tela os novos valores
    for chave in veiculo:
          print(f"{chave.capitalize()}: {veiculo[chave]}")
            

        



