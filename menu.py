from dicionario import *

print("Bem vindo a Porto Seguro Bike")
if __name__ == "__main__":
    loginCadastro()
    
while True :  
    
    print("\nMenu:")
    print("\nEscolha uma das opções abaixo:\n")
    print("\t1 - Minhas Bicicletas.")
    print("\t2 - Seguros Disponiveis.")
    print("\t3 - Meus Seguros.")
    print("\t4 - Vistoria.")
    print("\t5 - Historico.")
    print("\t6 - Dados do usuario.")
    print("\t7 - Desenvolvedores.")
    print("\t8 - Sair.")
       
    menu = input("\n\tDigite a opção escolhida\n\t> ")
    if menu == '1':
        bikes = carregar_bikes()
        while True:
            print("\nEscolha uma das opções abaixo:\n")
            print("\t1 - Cadastro de Bicicleta")
            print("\t2 - Minhas Bicicletas")
            print("\t3 - Alterar Bicicleta")
            print("\t4 - Apagar Bicicleta")
            print("\t5 - Sair")
            op = input("\n\tDigite a opção escolhida\n\t> ")
            if op == '1':
                cadastro_bike(bikes)
            elif op == '2':
                minhas_bikes()
            elif op == '3':
                alterar_bikes(bikes)
            elif op == '4':
                apagar_bike(bikes)
            elif op == '5':
                salvar_bikes(bikes)
                break
    elif menu == '2':
        while True:
            print("\nSeguros disponiveis.\n")
            seguros_disponiveis()
            print("\nEscolha uma das opções abaixo:\n")
            print("\t1 - Mais informações")
            print("\t2 - Adquirir novo seguro")
            print("\t3 - Voltar ao menu principal")
            info = input("\n\tDigite a opção escolhida\n\t> ")
            if info == '1':
                print("\nSeguros:\n")
                seguros_info()
            elif info == '2':
                print("\nAdquirir seguro:\n")
                adquirir_seguro()
                break
            elif info == '3':
                break
            else:
                print("\nComando invalido. Tente novamente.\n")
    elif menu == '3':
        print("\nMeus seguros\n")
        meus_seguros()
    elif menu == '4':
        print("Vistoria")
    elif menu == '5':
        print("\nHistorico\n")
        ler_historico()
    elif menu == '6':
        print("\nDados do usuario\n")
        dados_cadastro()
        print("\n")
    elif menu == '7':
        print("\n")
        integrantes()
        print("\n")
    elif menu == '8':
        print("\nAté logo!")
        break
    else:
        print("\nComando invalido. Tente novamente.\n")