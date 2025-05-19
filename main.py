import os
import pandas as pd

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
                print('Menu de Produtos:')
                Menu_produtos()

            case 2:
                print('Pedidos')
                exibir_subtitulos('Menu de Pedidos')
                print('Infelizmente ainda não consegui implementar essa parte do sistema')
                print()
                voltar_ao_menu_principal()

            case 3:

                print('Clientes')
                Menu_Clientes()
            case 4:
                sair()
    except:
        opcao_invalida()


'''Clientes'''

def Menu_Clientes():
    exibir_subtitulos('Menu de Clientes')

    '''Exibe as opções disponíveis no menu de clientes '''
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
                print('Cadastrar novo cliente')
                cadastrar_novo_cliente()
            case 2:
                print('Exibir clientes')
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
    exibir_subtitulos('Lista de Clientes cadastrados:')

    df = pd.read_csv('base_clientes.csv', sep=';')
    print(df)


'''Produtos'''


def Menu_produtos():

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
    """Cadastra um novo produto (Adionando ao arquivo csv)"""
    exibir_subtitulos('Cadastrando Novo Produto')
    nome_novo_produto = input('Digite o nome do produto: ')
    valor_novo_produto = input('Digite o valor do produto: ')
    ingredientes_novo_produto = input('Digite os ingredientes do produto: ')
    try:
        #Verifica se tem vírgula e trata vírgula como separador decimal
        valor_novo_produto = float(valor_novo_produto.replace(',' , '.')) 
    except ValueError:
        print("Valor inválido. Certifique-se de usar números.")
        return

    novo_produto = pd.DataFrame({'produto': [nome_novo_produto], 'valor': [valor_novo_produto], 'ingredientes': [ingredientes_novo_produto]})

    try:
        # Tenta ler o arquivo CSV existente
        df_existente = pd.read_csv('base_produtos.csv', sep=';')
        # Concatena o DataFrame existente com o novo produto
        df_completo = pd.concat([df_existente, novo_produto], ignore_index=True)
        # Escreve de volta para o CSV, sem o índice
        df_completo.to_csv('base_produtos.csv', index=False, sep=';')
        print(f"Produto '{nome_novo_produto}' adicionado com sucesso!")
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo com o produto
        novo_produto.to_csv('base_produtos.csv', index=False, sep=';')
        print(f"Arquivo '{'base_produtos.csv'}' não encontrado. Produto '{nome_novo_produto}' criado!")
    except Exception as e:
        print(f"Ocorreu um erro ao adicionar o novo produto: {e}")
    voltar_ao_menu_principal()

def exibir_produtos():
    exibir_subtitulos('Lista de Produto cadastrados:')

    df = pd.read_csv('base_produtos.csv', sep=';')
    print(df)
    print()
    print(80*"-")
    print()
    voltar_ao_menu_principal()

    


def exibir_subtitulos (texto):
    '''Essa função é responsável por limpar o terminal, exibir o subtítulo da opção escolhida pelo usuário'''
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''Essa função é responsável por voltar à tela inicial do programa na tela
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