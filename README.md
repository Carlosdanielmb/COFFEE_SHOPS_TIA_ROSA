# **Coffee Shops Tia Rosa**

## *AA- Atividade Ativa de Desenvolvimento em Python para a graduação de Engenharia de Software do Centro universitário IESB*
### Estudante: Carlos Daniel Marques Brito
#### Professor: Francisco Lima


### Descrição do projeto:
O Objetivo deste projeto é montar um sistema simples, para a empresa COFFEE SHOPS TIA ROSA, tendo em vista que os colaboradores  da empresa não tem um longo currículo de formação alinhado às atividades de tecnologia, ou seja ,sabem apenas o básico de tecnologia e como lidar com sistemas.O objetivo é criar um sistema simples, que atenda as necessidades da empresa, e que seja fácil de usar e entender.

### Situação-Problema:
O Coffee Shops Tia Rosa é uma cafeteria tradicional, conhecida por seu café artesanal e
ambiente acolhedor. Com o crescimento da concorrência e a digitalização acelerada do
mercado, a nova diretora, Maria, identificou diversas dificuldades operacionais e de divulgação
que afetam a experiência dos clientes e a eficiência da equipe. Entre os principais problemas
observados estão:
1. Ausência de um sistema de gestão interno:
Atualmente, todos os pedidos são feitos de forma manual, em papel. Isso gera
confusões nos horários de pico, aumenta o tempo de espera e dificulta o controle de
estoque e de vendas diárias.
2. Falta de organização no cardápio e nas informações dos produtos:
Muitos clientes têm dúvidas sobre os ingredientes dos itens, preços e promoções. A
falta de uma apresentação clara e acessível desses dados impacta negativamente na
tomada de decisão do consumidor.
3. Dificuldade na fidelização de clientes:
A cafeteria não possui um sistema de cadastro de clientes, o que inviabiliza a criação
de estratégias de fidelização, como promoções personalizadas ou programas de
pontos.
4. Equipe com baixa familiaridade com tecnologia:
Os colaboradores têm pouca ou nenhuma formação na área de informática. Isso exige
que qualquer solução tecnológica desenvolvida seja simples, intuitiva e eficiente.

### Objetivo Geral:
O objetivo geral deste projeto é desenvolver um sistema de gestão para a cafeteria Coffee Shops Tia Rosa, que permita otimizar o atendimento ao cliente, melhorar a organização interna e facilitar o controle de vendas e estoque. O sistema deve ser simples e intuitivo, levando em consideração a formação limitada dos colaboradores em tecnologia.


*Arquivos CSV:*
- **base_produtos.csv**: Contém informações sobre os produtos disponíveis na cafeteria, incluindo nome, valor e ingredientes.
- **base_clientes.csv**: Contém informações sobre os clientes cadastrados, incluindo nome, cpf e data de nascimento.


*Funções:*

```python
def exibir_nome_do_programa(): 
    """
    Função responsável por exibir o nome da empresa'Coffee Shops Tia Rosa' de uma forma personalizada.
    """
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
```

```python
def exibir_opcoes():
    '''Função responsável por exibir as opções disponíveis no menu principal.'''
    print(90*"-")
    '''Print responsável por criar um separador visual entre o nome da empresa e a primeira opção do menu principal.'''
    print()
    print('1.Produtos')
    print('2.Pedidos')
    print('3.Clientes')
    print('4.Sair\n')
```

```python
def sair():
    '''Essa função é responsável por limpar o terminal e finalizar o programa.
    Output:
    -Exibe a mensagem de Finalização para o usuário
    '''
    os.system('cls')
    print('Saindo do programa\n')
```

```python
def escolher_opcao():
    '''Essa função é responsável por perguntar qual a opção desejada pelo usuário, verificar se essa opção é válida(um número), caso seja válida, encaminhar a resposta para a função que cada opção possui. Caso inválida, encaminha para a função responsável pelos erros.
    Input:
    -Recebe a opção escolhida pelo usuário
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
            case 3:
                print('Clientes')
                Menu_Clientes()
            case 4:
                sair()
    except:
        opcao_invalida()
```

```python
def cadastrar_novo_cliente():
    '''Essa função é responsável por cadastrar um novo cliente, contendo nome, cpf e data de nascimento e adicionando ao arquivo csv
    Input:
    -Recebe os dados do cliente (nome, cpf e data de nascimento)
    -Verifica se o CPF contém apenas números e se tem 11 dígitos
    -Verifica se a data de nascimento está no formato correto
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

    # Recebe a data de nascimento do novo cliente
    data_nascimento_novo_cliente = input('Digite a data de nascimento do cliente com o Formato dd/mm/aaaa: ')

    novo_cliente = pd.DataFrame({'nome': [nome_novo_cliente], 'cpf': [cpf_novo_cliente], 'data_nascimento': [data_nascimento_novo_cliente]})

    try:
        # Tenta ler o arquivo CSV existente
        df_existente = pd.read_csv('base_clientes.csv', sep=';')

        # Concatena o DataFrame existente com o novo cliente
        df_completo = pd.concat([df_existente, novo_cliente], ignore_index=True)

        # Escreve de volta para o CSV, sem o índice
        df_completo.to_csv('base_clientes.csv', index=False, sep=';')

        # Exibe uma mensagem de sucesso
        print(f"Cliente '{nome_novo_cliente}' adicionado com sucesso!")
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo com o cliente
        novo_cliente.to_csv('base_clientes.csv', index=False, sep=';')

        # Exibe uma mensagem de sucesso
        print(f"Arquivo '{'base_clientes.csv'}' não encontrado. Cliente '{nome_novo_cliente}' criado!")
    except Exception as e:
        # Se ocorrer um erro, exibe uma mensagem de erro e chama a função para voltar ao menu principal
        print(f"Ocorreu um erro ao adicionar o novo cliente: {e}")
        voltar_ao_menu_principal()
```
