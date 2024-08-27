# Função que realiza o cadastro dos livros
def cadastrar_livro(id):

    print('-' * 41)
    print('-' * 9, 'MENU CADASTRAR LIVRO', '-' * 10)
    print('-' * 41)
    
    print(f'ID do livro: {id}')
    nome_livro = input('Por favor, entre com o nome do livro: ')
    autor = input('Por favor, entre com o autor do livro: ')
    editora = input('Por favor, entre com a editora do livro: ')

    livro = {'ID':id, 'Nome do Livro':nome_livro, 'Autor':autor, 'Editora':editora}

    global lista_livro
    
    lista_livro.append(livro) # Adiciona o novo livro cadastrado a lista

# Função que realiza as consultas dos livros
def consultar_livro():
    
    while True:

        print('-' * 41)
        print('-' * 9, 'MENU CONSULTAR LIVROS', '-' * 9)
        print('-' * 41)
        print('1 - Consultar todos livros')
        print('2 - Consultar por ID')
        print('3 - Consultar por autor')
        print('4 - Retornar ao menu')

        consulta = int(input('>>'))

        if consulta == 1:
            print(lista_livro)

        elif consulta == 2:
            consulta_id = int(input('Entre com o ID do livro: '))
            
            for livro in lista_livro:
            
                if livro ['ID'] == consulta_id:
                    print(livro)
                else:
                    ('ID errado ou não existe')
        
        elif consulta == 3:
            consulta_autor = input('Entre com o autor: ')
        
            for livro in lista_livro:
        
                if livro ['Autor'] == consulta_autor:
                    print(livro)
        
        elif consulta == 4:
            break
        
        else:
            print('Erro. Tente novamente')

# Função que remove livros
def remover_livro():
    print('-' * 41)
    remover_livro = int(input('Digite o ID do livro a ser removido: '))
    for livro in lista_livro:
        if livro ['ID'] == remover_livro:
            lista_livro.remove(livro)

lista_livro = [] # Lista com os dicionarios contendo as informações dos livros
id_global = 0 # Variavel que é incrementada a cada livro novo cadastrado

while True: # Inicio laço de repetição

    # Menu principal
    print('Bem-vindo a Livraria do Leonardo Pinheiro')
    print('-' * 41)
    print('-' * 12, 'MENU PRINCIPAL', '-' * 13)
    print('-' * 41)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')

    escolha_usuario = int(input('>>'))

    # if para validar a opção do usuario
    if escolha_usuario == 1:
        id_global += 1
        cadastrar_livro(id_global)
    elif escolha_usuario == 2:
        consultar_livro()
    elif escolha_usuario == 3:
        remover_livro()
    elif escolha_usuario == 4:
        break