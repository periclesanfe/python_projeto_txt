file = open("teste.txt", "a", encoding='utf-8')


def cadastrar_cliente():
    cliente = []
    nome = input('Digite seu nome: ')
    cliente.append(f'Nome: {nome}\n')
    telefone = input('Informe seu telefone: ')
    cliente.append(f'Telefone: {telefone}\n')
    endereco = input('Informe seu endereço: ')
    cliente.append(f'Endereço: {endereco}\n')
    return ''.join(cliente)


def dados():
    lista_de_dados = []
    Fusiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Rend = 1
    fus = 0
    I_N = 0

    Pot = float(input('Insira a potência em W do seu equipamento: '))
    lista_de_dados.append(f'A potência do seu equipamento é aproximadamente: {round(Pot)}W\n')
    Inf = (input('Seu equipamento é um motor? [s/n]: ')).upper()

    if Inf == 'S':
        Rend = float(input('Informe o rendimento do seu motor:  '))

    lista_de_dados.append(f'O rendimento do seu motor é {Rend}\n')

    FP = float(input('Informe o fator de potência do seu equipamento: '))
    lista_de_dados.append(f'O Fator de Potência do seu equipamento é {FP}\n')
    V = int(input('Informe  tensão entre fase e neutro: '))
    lista_de_dados.append(f'A tensão do seu equipamento é de {V}V\n')

    Pot = Pot / (FP * Rend)

    condicao = True
    while condicao:
        N_F = input('Seu equipamento é monofásico, bifásco ou trifásico [M/B/T]: ').upper()

        if N_F == 'M':
            I_N = Pot / V
            condicao = False
        elif N_F == 'B':
            I_N = Pot / (V * (3 ** (1 / 2)))
            condicao = False
        elif N_F == 'T':
            I_N = Pot / (V * 3)
            condicao = False
        else:
            print('Numero de fase inválida!\n\n')
            condicao = True

    lista_de_dados.append(f'Sua corrente é de: {round(I_N, 2)}A\n')

    for i in range(len(Fusiveis)):
        if Fusiveis[i] >= I_N:
            fus = Fusiveis[i]
            break

    lista_de_dados.append(f'Seu fusível deve ser o {fus}A\n\n\n')
    return lista_de_dados


# Recadastro

lista_vazia = []
cadastrar = True
while cadastrar:

    file.writelines(cadastrar_cliente())
    file.writelines(dados())
    escolha = (input('Deseja cadastrar um novo cliente? [s/n]')).lower()
    if escolha == 'n':
        cadastrar = False
    else:
        file.writelines(lista_vazia)

# criar aquivo txt

file.close()
