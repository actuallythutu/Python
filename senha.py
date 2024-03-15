while True:
    senha = input("Crie aqui a sua senha:\n")
    if not senha:
        print("Este campo precisa ser preenchido")
    else:
        print("Senha gravada com sucesso!")
        while True:
            confere = input("\nDigite a senha criada.\n")
            if (confere == senha):
                print("Bem-vindo(a) ao sistema")
                exit()
            else:
                print("Senha incorreta!")