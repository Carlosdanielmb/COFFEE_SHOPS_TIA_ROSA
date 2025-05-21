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

### Estrutura dos arquivos

- `main.py`: Arquivo principal do sistema.
- `base_produtos.csv`: Base de dados dos produtos.
- `base_clientes.csv`: Base de dados dos clientes.
- `base_pedidos.csv`: Base de dados dos pedidos.


### *Arquivo main.py*
Este é arquivo principal, onde o código é executado.

| Funções Principais | Descrição | Parâmetro |
|---|---|---|
| exibir_nome_do_programa | Função responsável por exibir o nome do programa | Nenhum |
| exibir_opcoes | Função responsável por exibir as opções disponíveis no menu principal | Nenhum |
| sair | Função responsável por limpar o terminal e finalizar o programa | Nenhum |
| escolher_opcao | Função responsável por receber a opção escolhida pelo usuário e executa a opção desejada pelo usuário | Nenhum |
| menu_produtos| Função responsável por exibir o menu de produtos | Nenhum |
| escolher_opcao_menu_produtos| Função responsável por receber a opção escolhida pelo usuário e executa a opção desejada pelo usuário | Nenhum |
| cadastrar_novo_produto|Função responsável por cadastrar um novo produto (Adionando ao arquivo csv)| Nenhum |
| exibir_produtos|Função responsável por exibir os produtos cadastrados no sistema | Nenhum |
| menu_pedidos | Função responsável por exibir o menu de pedidos, permitir ao usuário escolher uma opção e chamar a função correspondente| Nenhum |
| novo_pedido | Função responsável por criar um novo pedido, solicitar o CPF do cliente, selecionar produtos e enviar os dados para a função salvar_pedido| Nenhum |
| salvar_pedido | Função responsável por salvar o novo pedido no arquivo CSV| pedido |
| exibir_pedidos |Função responsável por exibir os pedidos registrados | Nenhum |
| alterar_status_pedido | Função responsável por alterar o status de um pedido existente | Nenhum |
| cancelar_pedido | Função responsável por cancelar um pedido existente | Nenhum |
|menu_clientes| Função responsável por exibir o menu de clientes e as opções disponíveis para o usuário | Nenhum |
|escolher_opcao_menu_clientes| Função responsável por receber a opção escolhida pelo usuário e executa a opção desejada pelo usuário | Nenhum |
|cadastrar_novo_cliente|Função responsável por cadastrar um novo cliente (Adionando ao arquivo csv)| Nenhum |
|exibir_clientes|Função responsável por exibir os clientes cadastrados no sistema | Nenhum |


| Funções de apoio | Descrição | Parâmetro |
|---|---|---| 
| exibir_subtitulos | Função responsável por limpar o terminal, exibir o subtítulo da opção escolhida pelo usuário| texto |
| voltar_ao_menu_principal | Função responsável por voltar à tela inicial do programa | Nenhum |
| opcao_invalida | Essa função é responsável por tratar qualquer erro na solicitação do usuário | Nenhum |
| main | Essa função é responsável por limpar o terminal,exibir o nome do programa, exibir as opções e exibir a mensagem na qual o usuário irá informar a opção desejada | Nenhum |


## Exemplos de dados dos arquivos CSV

- Exemplo para `base_produtos.csv`:

| Coluna | Descrição |
|---|---|
| id_produto | Identificador único do produto|
| produto |	Nome do produto |
| valor	| Preço do produto (em reais) |
| ingredientes | Ingredientes que compõem o produto |

Exemplo de dados:

id_produto;produto;valor;ingredientes
1;Cafe sem acucar;1.5;Água quente e Po de Cafe Santa Clara
2;Cafe com acucar;2.0;Água quente acucar e Po de Cafe Santa Clara


- Exemplo para `base_clientes.csv`: 

| Coluna | Descrição |
|---|---|
| cliente |	Nome do cliente | 
| cpf | CPF do cliente (11 dígitos) |
| data_nascimento |	Data de nascimento (dd/mm/aaaa) |

Exemplo de dados:

cliente;cpf;data_nascimento
Aurora Silva;36985214708;09/04/2003
Benício Oliveira;01478523691;25/06/1976


- Exemplo para `base_pedidos.csv`:

| Coluna | Descrição |
|---|---|
| id_pedido | Identificador único do pedido |
| cliente_cpf |	CPF do cliente que fez o pedido |
| data_hora | Data e hora do pedido 
| itens | Itens do pedido (nome, quantidade, valor unitário) |
| total | Valor total do pedido |
| status | Status do pedido (Em preparo, Concluído, Cancelado) |

Exemplo de dados:

id_pedido;cliente_cpf;data_hora;itens;total;status
1;36985214708;27/10/2024 10:00;Produto: Café,Quantidade: 2,Valor Unitário: 5.0;13.0;Concluído
2;210987654-05;27/10/2024 11:00;Produto: Cappuccino,Quantidade: 1,Valor Unitário: 8.0;8.0;Em preparo
3;08123456789;27/10/2024 12:00;Produto: Bolo de Cenoura,Quantidade: 1,Valor Unitário: 15.0;15.0;Em preparo
4;74185296304;27/10/2024 13:00;Produto: Torta de Maçã,Quantidade: 1,Valor Unitário: 12.0;12.0;Cancelado

### Licença

Este projeto está licenciado sob a licença MIT.

### Autor:
Carlos Daniel Marques Brito

### Contato:
    Qualquer dúvida ou sugestões entre em contato pelo e-mail.
*- E-mail: marquescarlosdaniel78@gmail.com*
