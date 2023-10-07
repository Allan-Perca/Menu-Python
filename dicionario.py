import csv
from datetime import datetime


def carregar_usuarios():
    try:
        with open('usuarios.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='') as file:
        fieldnames = ["nome", "sobrenome", "email", "login", "senha"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(usuarios)

def loginCadastro():
    user = carregar_usuarios()
    print("\nEscolha uma das opções abaixo:\n")
    print("\t1 - Login")
    print("\t2 - Cadastro")
    l = input("\n\tDigite a opção escolhida\n\t> ")
    if l == '1':
        print("Tela de login")
        login = input("\n\tDigite seu login\n\t> ")
        senha = input("\n\tDigite sua senha\n\t> ")
        if validar_login(login, senha, user):
            print("Login bem-sucedido!")
        else:
            print("Login ou senha incorretos.")
    elif l == '2':
        print("Tela de cadastro")
        nome = input("\n\tQual o seu nome?\n\t> ").title()
        sobrenome = input("\n\tQual o seu sobrenome?\n\t> ").title()
        email = input("\n\tInforme seu email para login\n\t> ")
        login = input("\n\tDigite seu login\n\t> ")
        senha = input("\n\tEscolha sua senha\n\t> ")
        usuario = {"nome": nome, "sobrenome": sobrenome, "email": email, "login": login, "senha": senha}
        user.append(usuario)
        salvar_usuarios(user)
        print("\tDados do usuário cadastrado:\n\t> Nome: {} {}\n\t> Email: {}\n\t> Senha: {}".format(nome, sobrenome, email, senha))
    else:
        print("Tente novamente")
        loginCadastro()

def validar_login(login, senha, usuarios):
    for usuario in usuarios:
        if usuario["login"] == login and usuario["senha"] == senha:
            return True
    return False

def dados_cadastro():
    user = carregar_usuarios()
    for u in user:
        nome = u["nome"] if u["nome"] else "N/A"
        sobrenome = u["sobrenome"] if u["sobrenome"] else "N/A"
        email = u["email"] if u["email"] else "N/A"
        login = u["login"] if u["login"] else "N/A"
        senha = u["senha"] if u["senha"] else "N/A"
        print("Nome:      {:<20}".format(nome))
        print("Sobrenome: {:<20}".format(sobrenome))
        print("Email:     {:<30}".format(email))
        print("Login:     {:<30}".format(login))
        print("Senha:     {:<30}".format(senha))
        print("\nEscolha uma das opções abaixo:\n")
        print("\t1 - Alterar")
        print("\t2 - Sair")
        op = input("\n\tDigite a opção escolhida\n\t> ")
        if op == '1':
            while True:
                print("\nEscolha uma das opções abaixo para alterar:\n")
                print("\t1 - Nome e Sobrenome")
                print("\t2 - Email")
                print("\t3 - Login")
                print("\t4 - Senha")
                print("\t5 - Sair")
                op_alt = input("\n\tDigite a opção escolhida\n\t> ")
                if op_alt == '1':
                    nv_nome = input("\n\tDigite o nome\n\t>  ").title()
                    nv_sobrenome = input("\n\tDigite o sobrenome\n\t> ").title()
                    u["nome"] = nv_nome
                    u["sobrenome"] = nv_sobrenome
                    print("Nome e Sobrenome alterados com sucesso.")
                    descricao = f"Cadastro alterado - Nome: {nv_nome}, Sobrenome: {nv_sobrenome}"
                    registrar_historico(descricao)
                elif op_alt == '2':
                    nv_email = input("\n\tDigite o email\n\t> ")
                    u["email"] = nv_email
                    print("Email alterado com sucesso.")
                    descricao = f"Cadastro alterado - Email: {nv_email}"
                    registrar_historico(descricao)
                elif op_alt == '3':
                    nv_login = input("\n\tDigite o login\n\t> ")
                    u["login"] = nv_login
                    print("Login alterado com sucesso.")
                    descricao = f"Cadastro alterado - Login: {nv_login}"
                    registrar_historico(descricao)
                elif op_alt == '4':
                    nv_senha = input("\n\tDigite a senha\n\t> ")
                    u["senha"] = nv_senha
                    print("Senha alterada com sucesso.")
                    descricao = f"Cadastro alterado - Senha: {nv_senha}"
                    registrar_historico(descricao)
                elif op_alt == '5':
                    salvar_usuarios(user)
                    break
                
def carregar_bikes():
    try:
        with open('bikes.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def salvar_bikes(bikes):
    with open('bikes.csv', mode='w', newline='') as file:
        fieldnames = ["apelido", "marca", "modelo", "aro"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(bikes)

def cadastro_bike(bikes):
    marca = input("\tQual a marca da bicicleta?\n\t> ").title()
    modelo = input("\tQual o modelo da bicicleta?\n\t> ").title()
    aro = input("\tQual o aro (tamanho) da bicicleta?\n\t> ")
    apelido = input("\tDe um apelido para essa bike:\n\t> ").upper()
    bike = {"marca": marca, "modelo": modelo, "aro": aro, "apelido": apelido}
    print("\tDados da bicicleta:\n\t> Apelido: {}\n\t> Marca: {}\n\t> Modelo: {}\n\t> Aro: {}".format(apelido, marca, modelo, aro))
    bikes.append(bike)  
    salvar_bikes(bikes) 
    print("Bicicleta cadastrada com sucesso.")
    descricao = f"Bicicleta cadastrada - Apelido: {apelido}, Marca: {marca}, Modelo: {modelo}, Aro: {aro}"
    registrar_historico(descricao)

def minhas_bikes():
    bikes = carregar_bikes()
    if not bikes:
        print("\nVocê não possui bicicletas cadastradas.\n")
        return
    print("\nSuas bicicletas cadastradas:\n")
    for index, bike in enumerate(bikes, start=1):
        print(f"{index} - Apelido: {bike['apelido']}, Marca: {bike['marca']}, Modelo: {bike['modelo']}")

def alterar_bikes(bikes):
    minhas_bikes()
    print("\n\tDigite 1 para sair para o menu ou")
    busca_bikes = input("\tDigite o apelido da bicicleta que deseja alterar\n\t> ").upper()
    for b in bikes:
        if busca_bikes == b["apelido"]:
            print("Bicicleta encontrada: ")
            print("\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(b["apelido"], b["marca"], b["modelo"], b["aro"]))
            print("\nO que gostaria de fazer com a bicicleta:\n")
            print("\t1 - Alterar")
            print("\t2 - Excluir")
            print("\t3 - Voltar ao menu principal")
            op_busca_bike = input("\n\tDigite a opção escolhida\n\t> ")
            if op_busca_bike == '1':
                nv_marca = input("\tQual a marca da bicicleta?\n\t> ").title()
                nv_modelo = input("\tQual o modelo da bicicleta?\n\t> ").title()
                nv_aro = input("\tQual o aro (tamanho) da bicicleta?\n\t> ")
                nv_apelido = input("\tDe um apelido para essa bike:\n\t> ").upper()
                b["marca"] = nv_marca
                b["modelo"] = nv_modelo
                b["aro"] = nv_aro
                b["apelido"] = nv_apelido
                salvar_bikes(bikes)
                print("Dados alterados com sucesso.")
                descricao = f"Bicicleta alterada - Apelido: {nv_apelido}, Marca: {nv_marca}, Modelo: {nv_modelo}, Aro: {nv_aro}"
                registrar_historico(descricao)
            elif op_busca_bike == '2':
                remover_bicicleta(b["apelido"])
                descricao = f"Bicicleta removida - Apelido: {b['apelido']}, Marca: {b['marca']}, Modelo: {b['modelo']}, Aro: {b['aro']}"
                registrar_historico(descricao)
            elif op_busca_bike == '3':
                None

def remover_bicicleta(apelido):
    bikes = carregar_bikes()  
    nova_lista_bikes = [b for b in bikes if b["apelido"] != apelido]
    salvar_bikes(nova_lista_bikes) 

def apagar_bike(bikes):
    minhas_bikes()
    apelido = input("\nDigite o apelido da bicicleta que deseja apagar:\n> ").upper()
    for bike in bikes:
        if bike["apelido"] == apelido:
            remover_bicicleta(apelido)
            print("Bicicleta apagada com sucesso.")
            salvar_bikes(bikes)
            break
    else:
        print("Bicicleta não encontrada.")

def seguros_disponiveis():
    print("1 - Urbana:\n\t- Cobertura basica\n\t- Acidentes pessoais individual\n\t- Subtração da bike\n\t- Garantia Internacional.\n")
    print("2 - Performance:\n\t- Cobertura basica\n\t- Acidentes pessoais individual\n\t- Subtração da bike\n\t- Garantia Internacional\n\t- Bike bagagem.\n")
    print("3 - Mountain bike:\n\t- Cobertura basica\n\t- Acidentes pessoais individual\n\t- Subtração da bike\n\t- Garantia Internacional\n\t- Bike bagagem.\n")

def seguro_urbana():
    print("\nUrbana:\n")
    print("\tCobertura basica: Garante os danos decorrentes da tentativa de subtração, incêndio, acidentes decorrentes de causa externa ou causados à bicicleta por acidente com o veículo transportador.\n")
    print("\tAcidentes pessoais individual: Garante a indenização aos beneficiários legais em caso de invalidez permanente total, parcial ou morte.\n")
    print("\tSubtração da bike*: Garante a cobertura/ressarcimento total, cometida ao segurado ou no local de guarda da bike.\n")
    print("\tGarantia Internacional: Garante o pagamento da indenização por perdas e danos materiais ocorridos em território internacional.\n")
    print("Observações:\n")
    print("\t*Não haverá cobertura quando tratar-se de subtração parcial.\n")

def seguro_performance():
    print("\nPerformance:\n")
    print("\tCobertura basica: Garante os danos decorrentes da tentativa de subtração, incêndio, acidentes decorrentes de causa externa ou causados à bicicleta por acidente com o veículo transportador.\n")
    print("\tAcidentes pessoais individual: Garante a indenização aos beneficiários legais em caso de invalidez permanente total, parcial ou morte.\n")
    print("\tSubtração da bike*: Garante a cobertura/ressarcimento total, cometida ao segurado ou no local de guarda da bike.\n")
    print("\tGarantia Internacional: Garante o pagamento da indenização por perdas e danos materiais ocorridos em território internacional.\n")
    print("\tBike bagagem**: Garante quando há ameaça direta ou uso de violência contra o segurado ou arrombamento do local onde a bicicleta estiver guardada.\n")
    print("Observações:\n")
    print("\t*Não haverá cobertura quando tratar-se de subtração parcial.\n")
    print("\t**Para efeito dessa cobertura entende-se como bagagem: a bicicleta segurada e mala utilizada para transporte da bicicleta, comprovadamente sob a responsabilidade da cia aérea ou rodoviária. Período de cobertura: durante o trajeto de ida e volta de viagem realizada pelo segurado.\n")

def seguro_mountain():
    print("\nMountain bike:\n")
    print("\tCobertura basica: Garante os danos decorrentes da tentativa de subtração, incêndio, acidentes decorrentes de causa externa ou causados à bicicleta por acidente com o veículo transportador.\n")
    print("\tAcidentes pessoais individual: Garante os danos decorrentes da tentativa de subtração, incêndio, acidentes decorrentes de causa externa ou causados à bicicleta por acidente com o veículo transportador.\n")
    print("\tSubtração da bike*: Garante a cobertura/ressarcimento total, cometida ao segurado ou no local de guarda da bike.\n")
    print("\tGarantia Internacional: Garante o pagamento da indenização por perdas e danos materiais ocorridos em território internacional.\n")
    print("\tBike bagagem**: Garante o extravio da bicicleta, quando em viagens aéreas e/ou rodoviárias.\n")
    print("Observações:\n")
    print("\t*Não haverá cobertura quando tratar-se de subtração parcial.\n")
    print("\t**Para efeito dessa cobertura entende-se como bagagem: a bicicleta segurada e mala utilizada para transporte da bicicleta, comprovadamente sob a responsabilidade da cia aérea ou rodoviária. Período de cobertura: durante o trajeto de ida e volta de viagem realizada pelo segurado.\n")

def seguros_info():
    while True:
        print("Para qual seguro deseja mais informações?\n")
        print("\t1 - Urbana")
        print("\t2 - Performance")
        print("\t3 - Mountain bike")
        print("\t4 - Sair")
        opc_seg = int(input("\n\tDigite a opção escolhida\n\t> "))
        if opc_seg == 1:
            print("\n")
            seguro_urbana()
            print("\n")
        elif opc_seg == 2:
            print("\n")
            seguro_performance()
            print("\n")
        elif opc_seg == 3:
            print("\n")
            seguro_mountain()
            print("\n")
        elif opc_seg == 4:
            break

def carregar_seguros():
    try:
        with open('seguros.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def salvar_seguros(seguros):
    with open('seguros.csv', mode='w', newline='') as file:
        fieldnames = ["bicicleta", "tipo", "cobertura_basica", "acidentes_pessoais", "subtracao_bike", "garantia_internacional", "bike_bagagem"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(seguros)

def adquirir_seguro():
    print("Escolha um dos seguros disponíveis:\n")
    print("\t1 - Urbana")
    print("\t2 - Performance")
    print("\t3 - Mountain bike")
    print("\t4 - Retornar ao menu principal")
    escolha = input("\nDigite a opção escolhida\n> ")
    if escolha == '1':
        adquirir_seguro_urbana()
    elif escolha == '2':
        adquirir_seguro_performance()
    elif escolha == '3':
        adquirir_seguro_mountain()
    elif escolha == '4':
        return
    else:
        print("\nOpção inválida. Tente novamente.\n")

def adquirir_seguro_urbana():
    print("\nDeseja adquirir este seguro?\n")
    seguro_urbana()
    print("\nEscolha uma das opções abaixo:\n")
    print("\t1 - Confirmar")
    print("\t2 - Retornar ao menu principal")
    confirma = input("\nDigite a opção escolhida\n> ")
    if confirma == '1':
        print("\nPara qual bicicleta é o seguro?\n")
        minhas_bikes()
        print("\nDigite o apelido da bicicleta ou Digite 1 para retornar ao menu principal:")
        busca_bike = input("\n> ").upper()
        if busca_bike == '1':
            return
        else:
            for bike in carregar_bikes():
                if busca_bike == bike["apelido"]:
                    print("\nDeseja adquirir o seguro para esta bicicleta?")
                    print("Escolha uma das opções abaixo:\n")
                    print("\t1 - Confirmar")
                    print("\t2 - Retornar ao menu principal")
                    confirma_busca = input("\nDigite a opção escolhida\n> ")
                    if confirma_busca == '1':
                        ap_seguro = bike["apelido"]
                        s_urb = {"bicicleta": ap_seguro, "tipo": "Urbana", "cobertura_basica": "Cobertura basica", "acidentes_pessoais": "Acidentes pessoais individual", "subtracao_bike": "Subtração da bike", "garantia_internacional": "Garantia Internacional", "bike_bagagem": ""}
                        salvar_seguros(s_urb)
                        print("\nSeguro adquirido com sucesso.")
                        descricao = f"Seguro adquirido - Apelido: {ap_seguro}, 'tipo': 'Urbana', 'cobertura_basica': 'Cobertura basica', 'acidentes_pessoais': 'Acidentes pessoais individual', 'subtracao_bike': 'Subtração da bike', 'garantia_internacional': 'Garantia Internacional', 'bike_bagagem': ''"
                        registrar_historico(descricao)
                    elif confirma_busca == '2':
                        return
                    else:
                        print("\nComando inválido. Tente novamente.\n")
    elif confirma == '2':
        return
    else:
        print("\nComando inválido. Tente novamente.\n")

def adquirir_seguro_performance():
    print("\nDeseja adquirir este seguro?\n")
    seguro_performance()
    print("\nEscolha uma das opções abaixo:\n")
    print("\t1 - Confirmar")
    print("\t2 - Retornar ao menu principal")
    confirma = input("\nDigite a opção escolhida\n> ")
    if confirma == '1':
        print("\nPara qual bicicleta é o seguro?\n")
        minhas_bikes()
        print("\nDigite o apelido da bicicleta ou Digite 1 para retornar ao menu principal:")
        busca_bike = input("\n> ").upper()
        if busca_bike == '1':
            return
        else:
            for bike in carregar_bikes():
                if busca_bike == bike["apelido"]:
                    print("\nDeseja adquirir o seguro para esta bicicleta?")
                    print("Escolha uma das opções abaixo:\n")
                    print("\t1 - Confirmar")
                    print("\t2 - Retornar ao menu principal")
                    confirma_busca = input("\nDigite a opção escolhida\n> ")
                    if confirma_busca == '1':
                        ap_seguro = bike["apelido"]
                        s_perf = {"bicicleta": ap_seguro, "tipo": "Performance", "cobertura_basica": "Cobertura basica", "acidentes_pessoais": "Acidentes pessoais individual", "subtracao_bike": "Subtração da bike", "garantia_internacional": "", "bike_bagagem": "Bike Bagagem"}
                        salvar_seguros(s_perf)
                        print("\nSeguro adquirido com sucesso.")
                        descricao = f"Seguro adquirido - Apelido: {ap_seguro}, 'tipo': 'Performance', 'cobertura_basica': 'Cobertura basica', 'acidentes_pessoais': 'Acidentes pessoais individual', 'subtracao_bike': 'Subtração da bike', 'garantia_internacional': '', 'bike_bagagem': 'Bike Bagagem'"
                        registrar_historico(descricao)
                    elif confirma_busca == '2':
                        return
                    else:
                        print("\nComando inválido. Tente novamente.\n")
    elif confirma == '2':
        return
    else:
        print("\nComando inválido. Tente novamente.\n")

def adquirir_seguro_mountain():
    print("\nDeseja adquirir este seguro?\n")
    seguro_mountain()
    print("\nEscolha uma das opções abaixo:\n")
    print("\t1 - Confirmar")
    print("\t2 - Retornar ao menu principal")
    confirma = input("\nDigite a opção escolhida\n> ")
    if confirma == '1':
        print("\nPara qual bicicleta é o seguro?\n")
        minhas_bikes()
        print("\nDigite o apelido da bicicleta ou Digite 1 para retornar ao menu principal:")
        busca_bike = input("\n> ").upper()
        if busca_bike == '1':
            return
        else:
            for bike in carregar_bikes():
                if busca_bike == bike["apelido"]:
                    print("\nDeseja adquirir o seguro para esta bicicleta?")
                    print("Escolha uma das opções abaixo:\n")
                    print("\t1 - Confirmar")
                    print("\t2 - Retornar ao menu principal")
                    confirma_busca = input("\nDigite a opção escolhida\n> ")
                    if confirma_busca == '1':
                        ap_seguro = bike["apelido"]
                        s_mountain = {"bicicleta": ap_seguro, "tipo": "Mountain Bike", "cobertura_basica": "Cobertura basica", "acidentes_pessoais": "", "subtracao_bike": "Subtração da bike", "garantia_internacional": "Garantia Internacional", "bike_bagagem": ""}
                        salvar_seguros(s_mountain)
                        print("\nSeguro adquirido com sucesso.")
                        descricao = f"Seguro adquirido - Apelido: {ap_seguro}, 'tipo': 'Mountain Bike', 'cobertura_basica': 'Cobertura basica', 'acidentes_pessoais': '', 'subtracao_bike': 'Subtração da bike', 'garantia_internacional': 'Garantia Internacional', 'bike_bagagem': ''"
                        registrar_historico(descricao)
                    elif confirma_busca == '2':
                        return
                    else:
                        print("\nComando inválido. Tente novamente.\n")
    elif confirma == '2':
        return
    else:
        print("\nComando inválido. Tente novamente.\n")

def meus_seguros():
    seguros = carregar_seguros()
    if not seguros:
        print("\nVocê não possui seguros cadastrados.\n")
        return
    bikes = carregar_bikes()
    if not bikes:
        print("\nVocê não possui bicicletas cadastradas.\n")
        return
    print("\nSeus seguros cadastrados:\n")
    for i, seguro in enumerate(seguros):
        for bike in bikes:
            if seguro["bicicleta"] == bike["apelido"]:
                print(f"{i + 1}. Bicicleta: {bike['apelido']}")
                print(f"   Tipo de seguro: {seguro['tipo']}")
                print(f"   Cobertura Básica: {seguro['cobertura_basica']}")
                print(f"   Acidentes Pessoais: {seguro['acidentes_pessoais']}")
                print(f"   Subtração da Bike: {seguro['subtracao_bike']}")
                print(f"   Garantia Internacional: {seguro['garantia_internacional']}")
                print(f"   Bike Bagagem: {seguro['bike_bagagem']}")
                print("\n")
    print("1 - Apagar seguro")
    print("2 - Sair")
    apagar = int(input("> "))
    if apagar == 1:
        opcao = input("Digite o número do seguro que deseja apagar (ou 'S' para sair): ").strip()
        if opcao.lower() == 's':
            return
        try:
            opcao = int(opcao) - 1
            if 0 <= opcao < len(seguros):
                seguro_removido = seguros[opcao]
                apelido_bike = seguro_removido["bicicleta"]
                remover_seguro(apelido_bike) 
                print(f"Seguro para a bicicleta {seguro_removido['bicicleta']} foi apagado.")
                descricao = f"Seguro removido - Bicicleta: {seguro_removido['bicicleta']}, Tipo: {seguro_removido['tipo']}, Cobertura Básica: {seguro_removido['cobertura_basica']}, Acidentes Pessoais: {seguro_removido['acidentes_pessoais']}, Subtração da Bike: {seguro_removido['subtracao_bike']}, Garantia Internacional: {seguro_removido['garantia_internacional']}, Bike Bagagem: {seguro_removido['bike_bagagem']}"
                registrar_historico(descricao)
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Tente novamente.")
    elif apagar == 2:
        return

def remover_seguro(apelido_bike):
    seguros = carregar_seguros()
    nova_lista_seguros = [seguro for seguro in seguros if seguro["bicicleta"] != apelido_bike]
    salvar_seguros(nova_lista_seguros)

def registrar_historico(descricao):
    agora = datetime.now()
    data_hora = agora.strftime("%d-%m-%y %H:%M:%S")
    with open('historico.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data_hora, descricao])

def ordenar_por_data_hora(evento):
    return datetime.strptime(evento['data_hora'], '%d-%m-%y %H:%M:%S')

def ler_historico():
    try:
        with open('historico.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            historico = list(reader)
        historico.sort(key=ordenar_por_data_hora)
        print("\nHistórico de Atividades:\n")
        print("{:<20}  {:<60}".format("Data e Hora", "Descrição"))
        for evento in historico:
            data_hora = evento['data_hora']
            descricao = evento['descricao']
            print("{:<20}  {:<60}".format(data_hora, descricao))
    except FileNotFoundError:
        print("O arquivo de histórico ainda não existe ou foi excluído.")

def integrantes():
    print("{:^60}".format("<<< Challenge 2023 - #3 Sprint >>>"))
    print("\nIntegrantes:\n")
    print("\t{:<30} {:^5} {:>5}".format("Allan Percario", "-", "RM99903"))
    print("\t{:<30} {:^5} {:>5}".format("Helena Cristina Rocha Medeiros", "-", "RM551873"))
    print("\t{:<30} {:^5} {:>5}".format("Lívia Freitas Ferreira", "-", "RM99892"))
    print("\t{:<30} {:^5} {:>5}".format("Luiza Nunes de Jesus", "-", "RM99768"))
    print("\t{:<30} {:^5} {:>5}".format("Tayná Alves Rodrigues", "-", "RM97589"))
    print("\nTurma: 1TDSPM")