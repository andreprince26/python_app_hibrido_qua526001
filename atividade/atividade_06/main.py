usuario = {
    'nome': "andre",
    'email': "andreprince@gmail",
    'telefone': "(61)9991-5555",
    'CPF': "444.555.222",
    'genero': "masculino"

}
# saida de dados

for chave in usuario:
    print(f"{chave.capitalize()}:{usuario[chave]}")

    # usuario escolhe o campo que deseja mudar
while True:
    campo = input("informe o nome do campo que deseja alterar ou digite'sair para encerrar o programa: ").strip().lower()

    match campo:
        case "nome":
            "usuario"['andre'] = input("informe o novo valor de 'andre'").strip()
        case "modelo":
            "usuario"['email'] = input("informe o novo valor de 'email'").strip()              
        case "ano":
            "usuario"['telefone'] = int(input("informe o novo valor de 'ano'").strip())               
        case "cor":
            "usuario"['CPF'] = input("informe o novo valor de 'CPF'").strip()              
        case "usuario":
            "usuario"['genero'] = input("informe o novo valor de 'genero'").strip()               
        case "sair":
            break                
        case _:
            print("valor invalido.")
            continue
            # mostra na tela os novos valores
    for chave in usuario:
          print(f"{chave.capitalize()}: {usuario[chave]}")
            










