Este programa é um sistema simples de gerenciamento de uma biblioteca, que permite ao usuário cadastrar, consultar e remover livros. 

Aqui está uma descrição passo a passo do que o programa faz.

Função cadastrar_livro(id):

Descrição: Esta função é usada para cadastrar novos livros na biblioteca.

Parâmetros: Recebe um parâmetro id, que é o identificador único do livro.

Funcionamento.

Exibe um menu de cadastro.

Solicita ao usuário que insira o nome do livro, o autor e a editora.

Cria um dicionário (livro) com os dados fornecidos e o id do livro.

Adiciona o dicionário à lista global lista_livro, que armazena todos os livros cadastrados.

Função consultar_livro():

Descrição: Permite consultar os livros cadastrados na biblioteca.

Funcionamento.

Exibe um menu com opções de consulta: todos os livros, livros por ID, livros por autor ou voltar ao menu principal. Dependendo da opção selecionada pelo usuário:

Consultar todos os livros: Exibe todos os livros cadastrados.

Consultar por ID: Solicita o ID do livro e exibe o livro correspondente, se encontrado.

Consultar por autor: Solicita o nome do autor e exibe todos os livros escritos por ele.

Retornar ao menu: Sai da função e volta ao menu principal.

Se o usuário escolhe uma opção inválida, exibe uma mensagem de erro e solicita nova entrada.

Função remover_livro():

Descrição: Remove um livro da biblioteca.

Funcionamento.

Solicita o ID do livro a ser removido. Procura o livro na lista lista_livro pelo ID, se encontrado, remove o livro da lista.

Lista Global lista_livro.

Descrição: Armazena todos os livros cadastrados como dicionários.

Variável Global id_global:

Descrição: Usada para gerar IDs únicos para cada livro cadastrado, incrementando a cada novo cadastro.

Loop Principal do Programa.

O loop principal do programa exibe um menu com as seguintes opções:

1 - Cadastrar Livro: Chama a função cadastrar_livro() para cadastrar um novo livro.
2 - Consultar Livro(s): Chama a função consultar_livro() para consultar os livros.
3 - Remover Livro: Chama a função remover_livro() para remover um livro.
4 - Sair: Encerra o programa.
