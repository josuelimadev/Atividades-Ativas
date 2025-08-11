import time
import datetime
from io import StringIO
import os
import pywhatkit as kit

"""importei 2 bibliotecas de tempo para funcoes diferentes, tambem usei StringIO para usar 
caracteres especiais, a bibilioteca os eu usei para limpar a tela depois de realizar os pedidos
e o pywhatkit serve pra mandar mensagens no whatsapp"""

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

cardapio= ['01 cafe expresso     5,00   |   02 capuccino         8,00',
           '03 latte            10,00   |   04 cha verde         5,00',
           '05 bubble tea       17,00   |   06 mocha            15,00',
           '07 chocolate quente  7,00   |   08 cafe gelado       5,00',
           '09 panqueca         12,00   |   10 tapioca           6,00',
           '11 pão na chapa      4,00   |   12 croissant        12,00']

"""criei uma lista de clientes e um cardapio em formato lista e adicionei nomes de clientes 
ficticios e alguns produtos, optei por fazer assim porque nao sei usar banco de dados,
seria interessante mudar o sistema para ficar mais facil de alterar o cardapio
"""
# IMPORTANTE, por nao ter um banco de dados, ao fechar o sistema, o registro de pontos de fidelidade
# se apagara, pois as novas adicoes na lista sumirao

escolha = ' '
fim= True
certeza_bool = True
certeza_int = 0
nome = ''
celular_coffee='+5511999999999'#insira o numero da empresa para receber o pedido via whatsapp

#declarei as listas e variaveis que usei no projeto
#tem mais algumas que eu usei dentro do codigo ao inves de usar como variavel global

while fim: # vai repetir o sistema enquanto fim for verdadeiro
    
    os.system('cls') # limpa o terminal apos a repeticao
    certeza_bool = True # ta aqui pra resetar um comando la na frente
    print ('\nSeja bem vindo ao Coffee Shops Tia Rosa\n\nComo podemos te ajudar hoje?\n\n')
    print ('Para fazer uma reserva digite 1\n')
    print ('Para consultar pontos de fidelidade digite 2\n')
    lst_menu = int(input ('')) # vai ler a resposta do usuario

    if  lst_menu== 1: # caso a resposta for 1
        
        for x in cardapio:
           print('\n' + x)
           #vai imprimir a lista cardapio inteira, pra cada item vai dar uma quebra de linha

        while certeza_bool== True: # vai repetir ate certeza_bool for False
            escolha = str(input('\nDigite sua escolha: ')) # a string escolha sera o que digtarem
            print('revisar pedido: ' + escolha) # verificacao de erros
            print('\nDigite 1 para confirmar')
            certeza_int = int(input()) # checa se tem certeza

            if certeza_int == 1: 
                certeza_bool = False
                # se for 1, termina o clico acima
        print('\nDigite seu nome completo para obter pontos de fidelidade')
        clientes.append(input()) # adiciona o cliente na lista de clientes
        print('aguarde seu pedido ser processado')
        ult_ped = clientes[-1] # checa o ultimo cliente a pedir
        mensagem = ult_ped + ' pediu ' + escolha # variavel mensagem para mandar o pedido
        kit.sendwhatmsg_instantly(celular_coffee,mensagem,wait_time=17,tab_close=True) # manda a mensagem
        print('pedido concluido')
        time.sleep(2) # espera 2 segundos

    elif lst_menu== 2: # caso a resposta for 2
        print(clientes.count(input('Digite seu nome:'))) # procura o nome
        time.sleep(1) # espera 1 segundo
        input() # confirma
    else:
        print('Use 1 ou 2, sem espaços') # aviso de erro para outros numeros
        time.sleep(1) # espera 1 segundo
