import os

restaurantes = [{'nome' : 'Pizzaria Mamadio', 'categoria' : 'Pizzaria', 'ativo' : False }, 
                {'nome' : 'Restaurante da Larissa', 'categoria' : 'comida caseira', 'ativo' : True}, 
                {'nome' : 'Kamen Rider', 'categoria' : 'japonesa', 'ativo' : False}]

def exibir_nome_do_programa():
      print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
      print('1. Cadastrar Restaurante')
      print('2. Listar Restaurante')
      print('3. Alterar o Estado do Restaurante')
      print("""4. Sair
            """)

def finalizar_app():
    exibir_subtitulo('Encerrando o app')

def voltar_menu():
     input('\nDigite uma tecla para voltar ao menu principal: ')
     main()

def opcao_invalida():
     print('Opção Invalida\n')
     voltar_menu()

def exibir_subtitulo(texto):
     os.system('cls')
     linha = '*' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()
     
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do Restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
     exibir_subtitulo('Lista de Restaurantes Cadastrados ')
     print(f'{'Nome do Restaurante'.ljust(32)} | {'Categoria'.ljust(20)} | Status')
     for restaurante in restaurantes:
          nome_restaurante = restaurante['nome']
          categoria = restaurante['categoria']
          ativo = 'ativado' if restaurante['ativo'] else 'desativado'
          print(f'- {nome_restaurante.ljust(30)} | {categoria.ljust(20)} | {ativo}')

     voltar_menu() 

def alternar_estado_restaurante():
     exibir_subtitulo('Alterando o Estado do Restaurante')
     nome_restaurante = input('Digite o nome do Restaurante que deseja alterar o estado: ')
     restaurante_encontrado = False

     for restaurante in restaurantes:
          if nome_restaurante == restaurante['nome']:
               restaurante_encontrado = True
               restaurante['ativo'] = not restaurante['ativo']
               mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
               print(mensagem)
     if not restaurante_encontrado:
           print('O restaurante não foi encontrato')

     
     voltar_menu()
     
def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))

            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
                        
            elif opcao_escolhida == 2:
                  listar_restaurantes()

            elif opcao_escolhida == 3:
                  alternar_estado_restaurante()
            
            elif opcao_escolhida == 4:
                  finalizar_app()
      except:
           opcao_invalida()            

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()