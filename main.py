#Biblioteca online
import os

Biblioteca = []
livro = {}

def Menu_principal():
    os.system('cls')
    print('Biblioteca sem nome')
    print(''' 
1 - Cadastrar novo livro                        
2 - Buscas                     
3 - Sair''')
    try:
        escolha = int(input('\nO que deseja fazer? '))

        if escolha == 1:
            Cadastrar_novo_livro()
        elif escolha == 2:
            Busca()
        elif escolha == 3:
            os.system('cls')
            print('Saindo do app.')
        else:
            print('Valor invalido')
            Menu_principal()
    except:
        print('Valor  invalido.')
        Menu_principal()


def Cadastrar_novo_livro():
    livro = {}  # Cria um novo dicionário para cada livro
    livro['nome'] = input('Digite o nome do livro: ')
    livro['autor'] = input('Qual o autor? ')
    livro['genero'] = input('Qual o genero? ')

    # Verifica se já existe um livro com o mesmo nome e autor
    for livro_existente in Biblioteca:
        if livro_existente['nome'].lower() == livro['nome'].lower() and \
           livro_existente['autor'].lower() == livro['autor'].lower():
            print('Já existe um livro com o mesmo nome e autor na biblioteca.')
            input('Pressione uma tecla para voltar ao menu principal.')
            Menu_principal()
            return

    # Adiciona um identificador único ao livro
    livro['id'] = len(Biblioteca) + 1
    Biblioteca.append(livro)
    print('O livro foi adicionado com sucesso.')
    input('Pressione uma tecla para voltar ao menu principal.')
    Menu_principal()


def buscador(nome_autor_genero, espeficicações):
    livros_encontrados = [livro for livro in Biblioteca if livro[espeficicações].lower().strip() == nome_autor_genero.lower().strip()]

    if livros_encontrados:
        os.system('cls')
        print(f'{"ID":<3} | {"Nome do livro":<20} | {"Autor":<20} | {"Genero":<20}')
        for livro in livros_encontrados:
            print(f'{livro["id"]:<3} | {livro["nome"].ljust(20)} | {livro["autor"].ljust(20)} | {livro["genero"].ljust(20)}')

        input('Pressione uma tecla para continuar.')
        Menu_principal()

    else:
        os.system('cls')
        print('Livro não encontrado.')
        input('Digite uma tecla para voltar ao menu principal.')
        Menu_principal()


def Busca():
    os.system('cls')  # Limpa a tela do console
    try:
        Busca = int(input('''
Como deseja realizar a busca?
1 - Por nome
2 - Por autor
3 - Por genero
4 - Voltar ao menu principal\n'''))

        if Busca == 1:
            nome = input('Digite o nome do livro: ')
            buscador(nome,'nome')

        elif Busca == 2:
            autor = input('Digite o autor: ')
            buscador(autor, 'autor')

        elif Busca == 3:
            genero = input('Digite o genero: ')
            buscador(genero, 'genero')

        elif Busca == 4:
            Menu_principal()

        else:
            print('Valor inválido')

    except ValueError:
        print('Valor inválido')

def main():
    os.system('cls')
    Menu_principal()

if __name__ == '__main__':
    main()