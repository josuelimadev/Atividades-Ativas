produtos={
    "1": {
        "prodnome": "Cafe",
        "ingredientes": "cafe moído agua quente",
        "preco": 5.5
    },
    "2": {
        "prodnome": "Cafe com leite",
        "ingredientes": "cafe expresso, leite",
        "preco": 8.9
    },
    "3": {
        "prodnome": "Cafe com Leite",
        "ingredientes": "cafe expresso, leite vaporizado",
        "preco": 9.5
    },
    "4": {
        "prodnome": "Nescau",
        "ingredientes": "nescau, leite",
        "preco": 12.0
    },
    "5": {
        "prodnome": "Pao de Queijo",
        "ingredientes": "Pao de queijo)",
        "preco": 7.0
    }
}

def listaprodutos():
    print("Lista de Produtos")
    for codproduto, dados in produtos.items():
        nome=dados['prodnome']
        print(f"\n {codproduto} {nome} Preço: {dados['preco']:.2f}")
        print(f" Ingredientes: {dados['ingredientes']}")


opcao=1
while opcao!=9:
        opcao=9

        print('1 Listar Produtos')
        print('2 Listar Clientes')
        print('3 Listar Pedidos')
        print('4 fazer Pedidos')
        print('5 Sair')

        opcao = int(input("Escolha a operação [0]: ") or 0)

        if opcao==0:
            break
        elif opcao==1:
            listaprodutos()
        elif opcao==2:
            print(opcao)
        elif opcao==3:
            print(opcao)
        elif opcao==4:
            print(opcao)
        else:
            print("Opção inválida. ENTER para continuar.")
            input()
            continue
        print()
        input('ENTER para voltar')
        