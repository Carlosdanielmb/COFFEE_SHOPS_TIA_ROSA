import os
import pandas as pd
from datetime import datetime

def exibir_nome_do_programa(): 
    '''Essa função é responsável por exibir o nome do programa '''
    print('''
░█████╗░░█████╗░███████╗███████╗███████╗███████╗  ░██████╗██╗░░██╗░█████╗░██████╗░░██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝  ██╔════╝██║░░██║██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║█████╗░░█████╗░░█████╗░░█████╗░░  ╚█████╗░███████║██║░░██║██████╔╝╚█████╗░
██║░░██╗██║░░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══╝░░  ░╚═══██╗██╔══██║██║░░██║██╔═══╝░░╚═══██╗
╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░███████╗███████╗  ██████╔╝██║░░██║╚█████╔╝██║░░░░░██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚══════╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═════╝░

████████╗██╗░█████╗░  ██████╗░░█████╗░░██████╗░█████╗░
╚══██╔══╝██║██╔══██╗  ██╔══██╗██╔══██╗██╔════╝██╔══██╗
░░░██║░░░██║███████║  ██████╔╝██║░░██║╚█████╗░███████║
░░░██║░░░██║██╔══██║  ██╔══██╗██║░░██║░╚═══██╗██╔══██║
░░░██║░░░██║██║░░██║  ██║░░██║╚█████╔╝██████╔╝██║░░██║
░░░╚═╝░░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░╚═╝''')

def exibir_opcoes():
    '''Exibe as opções disponíveis no menu principal '''
    print(90*"-")
    print()
    print('1.Produtos')
    print('2.Pedidos')
    print('3.Clientes')
    print('4.Sair\n')

def sair():
    '''É responsável por limpar o terminal e finalizar o programa
    Output:
    -Exibe a mensagem de Finalização para o usuário
    '''
    os.system('cls')
    print('Saindo do programa\n')

def escolher_opcao():
    '''Essa função é responsável por perguntar qual a opção desejada pelo usuário, verificar se essa opção é válida, caso seja válida, encaminhar a resposta para a função que cada opção tem.Caso inválida, encaminha para a função responsável pelos erros. 
    Input:
    -recebe a opção escolhida pelo usuário
    Output:
    -Executa a opção desejada pelo usuário'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) 
        match opcao_escolhida :
            case 1:
                menu_produtos()

            case 2:
                menu_pedidos()
            case 3:
                menu_clientes()
            case 4:
                sair()
    except ValueError:
        print('Opção inválida! Digite um número entre 1 e 4.')
        opcao_invalida()

'''Produtos'''

def menu_produtos():
    '''Essa função é responsável por exibir o menu de produtos e as opções disponíveis para o usuário'''

    exibir_subtitulos('Menu de Produtos')

    '''Exibe as opções disponíveis no menu de produtos '''
    print('1.Cadastrar novo produto')
    print('2.Exibir produtos')
    print('3.Voltar para o menu principal')
    print()
    escolher_opcao_menu_produtos()

def escolher_opcao_menu_produtos():
    '''Essa função é responsável por perguntar qual a opção desejada pelo usuário, verificar se essa opção é válida,caso seja válida, encaminhar a resposta para a função que cada opção tem.Caso inválida, encaminha para a função responsável pelos erros. 
    Input:
    -recebe a opção escolhida pelo usuário
    Output:
    -Executa a opção desejada pelo usuário'''
    try:
        opcao_escolhida_produtos = int(input('Escolha uma opção: ')) 
        match opcao_escolhida_produtos:

            case 1:
                print('Cadastrar novo produto')
                cadastrar_novo_produto()
            case 2:
                print('Exibir produtos')
                exibir_produtos()

            case 3:
                print('Voltar para o menu principal')
                voltar_ao_menu_principal()
                
    except:
        opcao_invalida()

def cadastrar_novo_produto():
    """Cadastra um novo produto (Adicionando ao arquivo csv)"""
    exibir_subtitulos('Cadastrando Novo Produto')
    nome_novo_produto = input('Digite o nome do produto: ')
    valor_novo_produto = input('Digite o valor do produto: ')
    ingredientes_novo_produto = input('Digite os ingredientes do produto: ')
    try:
        valor_novo_produto = float(valor_novo_produto.replace(',' , '.')) 
    except ValueError:
        print("Valor inválido. Certifique-se de usar números.")
        return

    try:
        # Tenta ler o arquivo CSV existente para buscar o último ID
        df_existente = pd.read_csv('base_produtos.csv', sep=';')
        if 'id_produto' in df_existente.columns and not df_existente.empty:
            novo_id = int(df_existente['id_produto'].max()) + 1
        else:
            novo_id = 1
        novo_produto = pd.DataFrame({'id_produto': [novo_id], 'produto': [nome_novo_produto], 'valor': [valor_novo_produto], 'ingredientes': [ingredientes_novo_produto]})
        df_completo = pd.concat([df_existente, novo_produto], ignore_index=True)
        df_completo.to_csv('base_produtos.csv', index=False, sep=';')
        print(f"Produto '{nome_novo_produto}' adicionado com sucesso!")
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo com o produto e id 1
        novo_produto = pd.DataFrame({'id_produto': [1], 'produto': [nome_novo_produto], 'valor': [valor_novo_produto], 'ingredientes': [ingredientes_novo_produto]})
        novo_produto.to_csv('base_produtos.csv', index=False, sep=';')
        print(f"Arquivo 'base_produtos.csv' não encontrado. Produto '{nome_novo_produto}' criado!")
    except Exception as e:
        print(f"Ocorreu um erro ao adicionar o novo produto: {e}")
    voltar_ao_menu_principal()

def exibir_produtos():
    '''Essa função é responsável por exibir os produtos cadastrados no arquivo csv'''
    exibir_subtitulos('Lista de Produtos cadastrados:')
    df_produtos = pd.read_csv('base_produtos.csv', sep=';')
    print(df_produtos[['id_produto', 'produto', 'valor', 'ingredientes']].to_string(index=False))
    print()
    print(95*"-")
    resposta_sair = input("Para voltar ao menu de produtos, pressione 'ENTER'.Ou qualquer outra tecla para voltar ao menu principal: ")
    if resposta_sair == '':
        menu_produtos()
    else:
        print(" Voltando ao menu principal.")
        voltar_ao_menu_principal()

'''Pedidos'''

def menu_pedidos():
    # Função para exibir o menu de pedidos, permitir ao usuário escolher uma opção e chamar a função correspondente
    while True:
        os.system("cls")
        exibir_subtitulos("Menu de Pedidos")
        print("1. Novo Pedido")
        print("2. Exibir Pedidos")
        print("3. Alterar Status do Pedido")
        print("4. Cancelar Pedido")
        print("5. Voltar para o menu principal")
        print()
        opcao_escolhida_pedidos  = input("Escolha uma opção: ")

        if opcao_escolhida_pedidos == "1":
            novo_pedido()
        elif opcao_escolhida_pedidos == "2":
            exibir_pedidos()
        elif opcao_escolhida_pedidos == "3":
            alterar_status_pedido()
        elif opcao_escolhida_pedidos == "4":
            cancelar_pedido()
       
        elif opcao_escolhida_pedidos == "5":
            voltar_ao_menu_principal()
        else:
            print("Opção inválida.")
            opcao_invalida()

def novo_pedido():
    # Função para criar um novo pedido, solicitar o CPF do cliente, selecionar produtos e enviar os dados para a função salvar_pedido
    os.system("cls")
    exibir_subtitulos("Novo Pedido")

    # 1. Selecionar Cliente
    df_clientes = pd.read_csv("base_clientes.csv", sep=";", dtype={"cpf": str})
    df_clientes["cpf"] = df_clientes["cpf"].astype(str).str.strip().str.zfill(11)
    print("Clientes Cadastrados:")
    print(df_clientes[["cliente", "cpf"]])

    while True:
        cpf_cliente = input("Digite o CPF do cliente: ").strip().zfill(11)
        if not cpf_cliente.isdigit() or len(cpf_cliente) != 11:
            print("CPF inválido. Digite apenas números (11 dígitos).")
            continue

        cliente_encontrado = df_clientes[df_clientes["cpf"] == cpf_cliente]

        if not cliente_encontrado.empty:
            cliente = cliente_encontrado.iloc[0]
            break
        else:
            print("Cliente não encontrado. Verifique o CPF.")
            voltar_ao_menu_principal()
            return
        
    # 2. Selecionar Produtos
    df_produtos = pd.read_csv("base_produtos.csv", sep=";")
    print("\nProdutos Disponíveis:")
    # Exibe nome e valor para seleção
    print(df_produtos[["produto", "valor"]])  

    produtos_pedido = []
    total_pedido = 0.0
    while True:
        id_produto = input("Digite o ID do produto (ou 'fim' para terminar): ")
        if id_produto.lower() == "fim":
            break
        quantidade = int(input(f"Digite a quantidade de {id_produto}: "))
        produto = df_produtos[df_produtos["id"] == id_produto].iloc[0]
        produtos_pedido.append({"produto": produto["produto"], "quantidade": quantidade, "valor_unitario": produto["valor"]})
        total_pedido += produto["valor"] * quantidade

    # 3.  Resumo do Pedido
    print("\nResumo do Pedido:")
    print(f"Cliente: {cliente['cliente']} (CPF: {cliente['cpf']})")
    for item in produtos_pedido:
        print(f"  - {item['produto']} x {item['quantidade']} = R$ {item['valor_unitario'] * item['quantidade']:.2f}")
    print(f"Total do Pedido: R$ {total_pedido:.2f}")

    # 4.  Confirmação e Salvamento
    while True:
        confirmar = input("Confirmar pedido? (S/N): ").strip().upper()
        if confirmar == "S":
            agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            pedido = {
                "cliente_cpf": cliente["cpf"],
                "data_hora": agora,
                "itens": produtos_pedido,
                "total": total_pedido,
                "status": "Em Preparo"
            }
            salvar_pedido(pedido)
            print("Pedido registrado com sucesso!")
            break
        elif confirmar == "N":
            print("Pedido cancelado.")
            break
        else:
            print("Opção inválida. Digite apenas S para sim ou N para não.")
        continue

def salvar_pedido(pedido):
    '''Função responsável por salvar o novo pedido no arquivo CSV.'''
    try:
        df_pedidos = pd.read_csv("base_pedidos.csv", sep=";")
        novo_id = df_pedidos["id_pedido"].max() + 1
        pedido["id_pedido"] = novo_id
        df_novo_pedido = pd.DataFrame([pedido])
        df_completo = pd.concat([df_pedidos, df_novo_pedido], ignore_index=True)
        df_completo.to_csv("base_pedidos.csv", sep=";", index=False)
    except FileNotFoundError:
        pedido["id_pedido"] = 1
        df_novo_pedido = pd.DataFrame([pedido])
        df_novo_pedido.to_csv("base_pedidos.csv", sep=";", index=False)

def exibir_pedidos():
    '''Função responsável por exibir os pedidos registrados.'''
    os.system("cls")
    exibir_subtitulos("Exibir Pedidos")
    try:
        df_pedidos = pd.read_csv("base_pedidos.csv", sep=";")
        if df_pedidos.empty:  # Verifica se o DataFrame está vazio
            print("Não há pedidos registrados.")
        else:
            print(df_pedidos[['id_pedido', 'cliente_cpf', 'data_hora', 'itens', 'total', 'status']].to_string(index=False))
            # Se precisar converter a coluna 'itens' de volta para lista:
            # df_pedidos['itens'] = df_pedidos['itens'].apply(ast.literal_eval)
    except FileNotFoundError:
        print("Ainda não há pedidos registrados.")
    except pd.errors.EmptyDataError:  # Captura erro se o arquivo CSV estiver vazio
        print("Não há pedidos registrados.")
    except Exception as e:  # Captura outros erros inesperados
        print(f"Ocorreu um erro ao exibir os pedidos: {e}")
        voltar_ao_menu_principal()

    # Após exibir os pedidos, pergunta se o usuário deseja voltar ao menu de clientes ou ao menu principal
    print(90*"-")
    resposta_sair = input("Para voltar ao menu de clientes, pressione 'ENTER'.Ou qualquer outra tecla para voltar ao menu principal: ")
    if resposta_sair == '':
        menu_clientes()
    else:
        print(" Voltando ao menu principal.")
        voltar_ao_menu_principal()

def alterar_status_pedido():
    '''Função responsável por alterar o status de um pedido existente.'''
    os.system("cls")
    exibir_subtitulos("Alterar Status do Pedido")
    try:
        df_pedidos = pd.read_csv("base_pedidos.csv", sep=";")
        print("Pedidos Registrados:")
        print(df_pedidos[['id_pedido', 'cliente_cpf', 'data_hora', 'itens', 'total', 'status']].to_string(index=False))
        print()
        print(100*"-")
        print()
        id_alterar = int(input("Digite o ID do pedido para alterar o status: "))
        if id_alterar in df_pedidos["id_pedido"].values:
            print("Escolha o novo status:")
            print("1 - Concluído")
            print("2 - Cancelado")
            opcao_status = input("Digite o número do novo status: ")
            if opcao_status == "1":
                df_pedidos.loc[df_pedidos["id_pedido"] == id_alterar, "status"] = "Concluído"
                print("Status alterado para Concluído!")
            elif opcao_status == "2":
                df_pedidos.loc[df_pedidos["id_pedido"] == id_alterar, "status"] = "Cancelado"
                print("Status alterado para Cancelado!")
            else:
                print("Opção de status inválida.")
                return
            df_pedidos.to_csv("base_pedidos.csv", sep=";", index=False)
        else:
            print("Pedido não encontrado.")
    except FileNotFoundError:
        print("Ainda não há pedidos registrados.")
    except ValueError:
        print("ID de pedido inválido.")
        menu_pedidos()
    voltar_ao_menu_principal()

def cancelar_pedido():
    '''Função responsável por cancelar um pedido existente.'''
    os.system("cls")
    exibir_subtitulos("Cancelar Pedido")
    try:
        df_pedidos = pd.read_csv("base_pedidos.csv", sep=";")
        print("Pedidos Registrados:")
        print(df_pedidos[['id_pedido', 'cliente_cpf', 'data_hora', 'itens', 'total', 'status']].to_string(index=False))
        print()
        print(100*"-")
        print()

        id_cancelar = int(input("Digite o ID do pedido a cancelar: "))
        if id_cancelar in df_pedidos["id_pedido"].values:
            df_pedidos.loc[df_pedidos["id_pedido"] == id_cancelar, "status"] = "Cancelado"
            df_pedidos.to_csv("base_pedidos.csv", sep=";", index=False)
            print("Pedido cancelado com sucesso!")
        else:
            print("Pedido não encontrado.")
    except FileNotFoundError:
        print("Ainda não há pedidos registrados.")
    except ValueError:
        print("ID de pedido inválido.")
        menu_pedidos()



'''Clientes'''

def menu_clientes():
    '''Essa função é responsável por exibir o menu de clientes e as opções disponíveis para o usuário'''
    exibir_subtitulos('Menu de Clientes')

    print('1.Cadastrar novo cliente')
    print('2.Exibir clientes')
    print('3.Voltar para o menu principal')
    print()
    escolher_opcao_menu_clientes()

def escolher_opcao_menu_clientes():
    '''Essa função é responsável por perguntar qual a opção desejada pelo usuário, verificar se essa opção é válida,caso seja válida, encaminhar a resposta para a função que cada opção tem.Caso inválida, encaminha para a função responsável pelos erros. 
    Input:
    -recebe a opção escolhida pelo usuário
    Output:
    -Executa a opção desejada pelo usuário'''
    try:
        opcao_escolhida_menu_clientes = int(input('Escolha uma opção: ')) 
        match opcao_escolhida_menu_clientes:

            case 1:
                cadastrar_novo_cliente()
            case 2:
                exibir_clientes()

            case 3:
                voltar_ao_menu_principal()
                
    except:
        opcao_invalida()

def cadastrar_novo_cliente():
    '''Essa função é responsável por cadastrar um novo cliente, adicionando ao arquivo csv
    Input:
    -Recebe os dados do cliente
    Output:
    -Adiciona o cliente ao arquivo csv'''
    exibir_subtitulos('Cadastrando Novo Cliente')

    # Recebe o nome do novo cliente
    nome_novo_cliente = input('Digite o nome do cliente: ')

    #Recebe o cpf do novo cliente 
    cpf_novo_cliente = input('Digite o CPF do cliente,digite apenas números:')

    # Verifica se o CPF contém apenas números
    if not cpf_novo_cliente.isdigit():
        print("CPF inválido.Digite apenas números.")
        return
    # Verifica se o CPF tem 11 dígitos
    if len(cpf_novo_cliente) != 11:
        print("CPF inválido. O CPF deve ter 11 dígitos.")
        return
    
    data_nascimento_novo_cliente = input('Digite a data de nascimento do cliente com o Formato dd/mm/aaaa: ')
    
    novo_cliente = pd.DataFrame({'cliente': [nome_novo_cliente], 'cpf': [cpf_novo_cliente], 'data_nascimento': [data_nascimento_novo_cliente]})

    try:
        # Tenta ler o arquivo CSV existente
        df_existente = pd.read_csv('base_clientes.csv', sep=';')
        # Concatena o DataFrame existente com o novo cliente
        df_completo = pd.concat([df_existente, novo_cliente], ignore_index=True)
        # Escreve de volta para o CSV, sem o índice
        df_completo.to_csv('base_clientes.csv', index=False, sep=';')
        print(f"Cliente '{nome_novo_cliente}' adicionado com sucesso!")
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo com o cliente
        novo_cliente.to_csv('base_clientes.csv', index=False, sep=';')
        print(f"Arquivo '{'base_clientes.csv'}' não encontrado. Cliente '{nome_novo_cliente}' criado!")
    except Exception as e:
        print(f"Ocorreu um erro ao adicionar o novo cliente: {e}")
    voltar_ao_menu_principal()

def exibir_clientes():
    '''Essa função é responsável por exibir os clientes cadastrados no arquivo csv'''
    exibir_subtitulos('Lista de Clientes cadastrados:')
    try:
        # Tenta ler o arquivo CSV existente
        df_clientes = pd.read_csv('base_clientes.csv', sep=';')
    except FileNotFoundError:
        print("Ainda não há clientes cadastrados.")
        voltar_ao_menu_principal()
        return

    # Garante que o CPF seja tratado como string e tenha 11 dígitos
    df_clientes['cpf'] = df_clientes['cpf'].str.zfill(11)
    print(df_clientes[['cliente', 'cpf', 'data_nascimento']].to_string(index=False))
    print()
    print(80*"-")
    print()
    resposta_sair = input("Para voltar ao menu de clientes, pressione 'ENTER'.Ou qualquer outra tecla para voltar ao menu principal: ")
    if resposta_sair == '':
        menu_clientes()
    else:
        print(" Voltando ao menu principal.")
        voltar_ao_menu_principal()   


'''Funções de apoio'''

def exibir_subtitulos (texto):
    '''Essa função é responsável por limpar o terminal, exibir o subtítulo da opção escolhida pelo usuário'''
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''Essa função é responsável por voltar à tela inicial do programa 
    Input:
    -Pede para o usuário confirmar a volta pra tela inicial
    Output:
    -Retorna ao menu principal
    '''
    
    input('Clique "ENTER" para voltar ao menu inicial\n')
    main()

def opcao_invalida():
    '''Essa função é acionada quando há algum erro na solicitação do usuário 
    e aciona a função de retorno à tela inicial
    Output:
    -Exibe uma mensagem de erro para o usuário
    '''
    print('Opção inválida!')
    voltar_ao_menu_principal()
    
def  main():
    '''Essa função é responsável por limpar o terminal,exibir o nome do programa, exibir as opções e exibir a mensagem na qual o usuário irá informar a opção desejada'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__' :
    main()