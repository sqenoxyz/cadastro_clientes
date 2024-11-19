print('Cadastro de Clientes')

cadastrar = str(input('Deseja cadastrar um cliente ?(S/N)'))
nome = str(input('Digite seu nome: '))
cpf = str(input('Digite o cpf do cliente: '))
endereco = str(input('Digite o endereço do cliente: '))
data_nasc = str(input('Digite a data de nascimento do cliente: '))
cliente_tipo = str(input('Digite o tipo do cliente(PF/PJ)'))

if cadastrar == 'S':
    with open('Lista_Clientes.csv', 'a', encoding='utf8') as arquivo:
        arquivo.write(f'Nome: {nome}, CPF: {cpf}, Endereço: {endereco}, Data de Nascimento: {data_nasc}, Tipo de Cliente: {cliente_tipo}\n')
        print('Cliente cadastrado com sucesso!')