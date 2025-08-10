import math
import random
import time
import datetime
from io import StringIO
import os
import pywhatkit as kit

clientes= ["jose carlos de souza","lindalva silva nobrega","ricardo sergio perez","ana clara souza",
    "joao pedro silva","maria eduarda lima","carlos alberto mendes","fernanda souza pires",
    "pedro henrique alves","juliana silva santos","max verstappen da silva","luis inacio kleber"
    "jair messias pinto","pedro henrique alves","juliana silva santos","max verstappen da silva",
    "paulo henrique rocha","juliana silva santos","rafael lima fernandes","max verstappen da silva",
    "camila rodrigues costa","pedro henrique alves","mariana oliveira machado","lucas gabriel teixeira",
    "gabriela santos ramos","rodrigo alves pereira","larissa monteiro brito","andre luiz barros",
    "patricia gomes fonseca","bruno cesar pinto","aline rocha martins","felipe mendes cardoso",
    "beatriz costa soares","gustavo fernandes moraes","vanessa machado dias","eduardo pires campos",
    "carla fonseca araujo","ricardo teixeira matos", "natalia mendonca reis","tiago brito figueiredo",
    "isabela cardoso vieira","sergio ramos almeida","maria","maria","maria","maria","maria","maria","maria"]
cardapio= ['01 cafe expresso    5,00', '02 capuccino    8,00', '03 panqueca    12,00', '04 tapioca   6,00']
escolha = ' '
fim= True
certeza_bool = True
certeza_int = 0
nome = ''
celular_coffee = '+5511999999999'

while fim:
    
    #time.sleep(10)
    os.system('cls')
    certeza_bool = True
    print ('\nSeja bem vindo ao Coffee Shops Tia Rosa\n\nComo podemos te ajudar hoje?\n\n')
    print ('Para fazer uma reserva digite 1\n')
    print ('Para consultar pontos de fidelidade digite 2\n')
    lst_menu = int(input (''))

    if  lst_menu== 1:
        if lst_menu==1:
            for x in cardapio:
                print('\n' + x)
                print('para')
            print('\n')

            while certeza_bool== True:
                escolha = str(input('Digite sua escolha: '))
                print('revisar pedido: ' + escolha)
                print('\nDigite 1 para confirmar')
                certeza_int = int(input())

                if certeza_int == 1:
                    certeza_bool = False

            print('\nDigite seu nome completo para obter pontos de fidelidade')
            clientes.append(input())
            print('pedido concluido')
            kit.sendwhatmsg_instantly(celular_coffee,escolha,wait_time=15,tab_close=True)
            time.sleep(2)

    elif lst_menu== 2:
        print(clientes.count(input('Digite seu nome:')))
        time.sleep(1)
        input()
    else:
        print('Use 1 ou 2, sem espaços')
        time.sleep(1)