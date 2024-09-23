senha = ""
while senha != "12345":
    senha = input("Digite a senha: ")
    if senha == "12345":
        print("Acesso concedido!")
    else:
        print("Senha incorreta, tente novamente.")