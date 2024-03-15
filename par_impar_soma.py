while True:
    n1 = int(input("Digite o primeiro número:\n"))
    n2 = int(input("Digite o segundo número:\n"))

    exibe_numeros=f"O primeiro número digitado foi {n1} e o segundo número digitado foi {n2}"
    print(exibe_numeros)


    confirma = input("Confirma que os números estão corretos? (Digite 'Sim' para prosseguir e 'Não' para voltar)\n")

    if (confirma == "Sim"):
        s1 = n1+n2

        if (s1 % 2 == 0):
            par = f'O resultado da soma é {s1} e o número é par'
            print(par)
        else:
            impar = f'O resultado da soma é {s1} e o número é ímpar'
            print(impar)
        while True:
            sair = input("Deseja testar o programa novamente? (Digite 'Sim' para voltar ao início e 'Sair' para sair)\n")
            if (sair == 'Sim'):
                break
            elif (sair == 'Sair'):
                exit()
            else:
                print("\nDigite uma opção válida\n")
    elif (confirma == "Não"):
        print("Digite os números novamente")
    else:
        print("Digite uma opção válida")