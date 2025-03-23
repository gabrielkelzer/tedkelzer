import os

#fala meu caro leitor, oque está abaixo são as funções em python

clear = lambda: os.system('clear') #clear serve pra limpar a tela

sleep = lambda: os.system('sleep 2') #sleep serve pra fazer a tela pausar por determinado tempo

def menu_do_tedkelzer(): #essa função é pra exibir o menu principal do programa
     print ('''\033[1;32m
        _____        _ _   __     _              
       |_   _|      | | | / /    | |             
         | | ___  __| | |/ /  ___| |_______ _ __ 
         | |/ _ \/ _` |    \ / _ \ |_  / _ \ '__|
         | |  __/ (_| | |\  \  __/ |/ /  __/ |   
         \_/\___|\__,_\_| \_/\___|_/___\___|_|\033[0m\033[1;31m v1\033[0m

                         \033[1;41mATENÇÃO:\033[0m

\033[1;36m    Este Script serve para ensinar o passo a passo para o
  usuário baixar o Android Studio no computador, porém eu
  também criei o programa para praticar os meus conhecimentos\033[0m\033[1;31m!
\033[0m

\033[1;31m[\033[0m\033[1;37m 01\033[0m\033[1;31m ]\033[0m \033[1;33mPRIMEIRO PASSO\033[0m              \033[1;31m [\033[0m\033[1;37m 02\033[0m\033[1;31m ] \033[0m\033[1;33mSEGUNDO PASSO\033[0m

\033[1;31m[\033[0m\033[1;37m 03\033[0m\033[1;31m ]\033[0m \033[1;33mTERCEIRO PASSO\033[0m              \033[1;31m [\033[0m \033[1;37m04 \033[0m\033[1;31m]\033[0m\033[1;33m QUARTO PASSO\033[0m

\033[1;31m[\033[0m\033[1;37m 05\033[0m\033[1;31m ]\033[0m \033[1;33mQUINTO PASSO\033[0m                \033[1;31m [\033[0m\033[1;37m 06\033[0m\033[1;31m ]\033[0m\033[1;33m SAIR\033[0m
     ''') #Meu caro leitor, essa é a última função.


#Logo abaixo tem algumas váriaveis para ajudar o programa a funcionar
MENU_TEDKELZER = "0"


while MENU_TEDKELZER != "06":
      clear()
      menu_do_tedkelzer()
      MENU_TEDKELZER = input('''\033[1;31mツ\033[0m \033[1;37m-\033[0m \033[1;32mESCOLHA UM NÚMERO: \033[0m''')
      clear()

      match MENU_TEDKELZER:
          case "01":
               print ('''
                         \033[1;41mESCOLHA 01:\033[0m
\033[1;37m
    Em resumo, para instalar o Software Android Studio no
  seu computador é preciso acessar o site de downloads que
  é chamado de -> \033[0m\033[1;34mhttps://developer.android.com/studio \033[0m\033[1;31m!

\033[0m\033[1;37m
  Acesse o site abaixo para saber mais\033[0m\033[1;31m : \033[0m
\033[1;34m  https://developer.android.com/studio/install?hl=pt-br \033[0m
               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "02":
               print ('''
                        \033[1;41m ESCOLHA 02: \033[0m
\033[1;37m
    Após ler os termos e as condições apresentadas no Soft
  Clique na opção\033[0m\033[1;33m "configure"\033[0m\033[1;37m no canto inferior a direita
  da tela.\033[0m\033[1;33m Lembre-se\033[0m\033[1;31m :\033[0m\033[1;37m indepedente da versão que você baixou
  e instalou... a tela de configuração será a mesma.\033[0m
               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "03":
               print ('''
                        \033[1;41m ESCOLHA 03: \033[0m
\033[1;37m
    Clicar em\033[0m \033[1;33mSDK MANAGER\033[0m\033[1;37m e com isso é aberto o\033[0m\033[1;33m ANDROID SDK
   LOCATION. \033[0m
               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "04":
               print ('''
                        \033[1;41m ESCOLHA 04: \033[0m
\033[1;37m
    Manter o \033[0m\033[1;33mSDK TOOLS\033[0m\033[1;37m selecionados pois é de extrema
   Importância para a emulação. \033[0m
               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "05":
               print ('''
                        \033[1;41m ESCOLHA 05: \033[0m
\033[1;37m
    Agora o próximo passo é configurar o emulador vá em
   configure, em seguida em\033[0m \033[1;33mAVD MANAGER.\033[0m
               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "06":
               print ('''
                        \033[1;41m ESCOLHA 06: \033[0m
\033[1;37m
    Obrigado por utilizar o meu programa, peço que você se inscreva
   no meu canal do YouTube\033[0m\033[1;33m @gabrielkelzer \033[0m\033[1;31m! \033[0m
               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m!\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA SAIR DO SOFTWARE:\033[0m')
          case _:    #Essa opção é somente se as anteriores não foram atendidas
               menu_do_tedkelzer()
               print ('\033[1;31m[ x ] - ESCOLHA INVÁLIDA ! \033[0m')
               sleep()
