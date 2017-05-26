from models.Pedido import Pedido
from controllers.Dbmanager import Dbmanager
from controllers.ClienteController import ClienteController
import os

class PedidoController:
    pedido = None


    @staticmethod
    def buscarProduto():
        print('')
        id = input('Id do produto: ')
        prod = Dbmanager.getProduct(id)
        if prod is None:
            print('Produto não encontrado.')
        else:
            print(prod)
        print('')

    def criarPedido(self):
        file = open(os.path.abspath('produtos.txt'), 'r').readlines()
        ids = []
        for line in file:
            product = line.split(':')
            print('ID: {} - {} - R$ {}'.format(product[0], product[1], product[2]), end='')
            ids.append(int(product[0]))

        carrinho = []

        while True:
            id_prod = None
            while id_prod not in ids:
                try:
                    id_prod = int(input("\nId do produto para ser adicionado: "))
                except TypeError:
                    print('Nenhum produto com esse id!')

            qnt = int(input("Quantidade: "))
            while isinstance(qnt, int) is False:
                print('Valor Inválido')
                qnt = int(input("Quantidade: "))

            carrinho.append([id_prod, qnt])

            quit = input('Fechar pedido? [s/N] ')
            if quit == 's' or quit == 'S':
                break

        self.pedido = Pedido(carrinho)
        self.pedido.salvarPedido()
        pag = input('Pagar agora? [S/n] ')
        if pag == 'n' or pag == 'N':
            print('Pedido salvo para pagamento posterior.')
        else:
            PedidoController.pagarPedido(self.pedido.idPedido)


    @staticmethod
    def verificarPedido():
        id = input('\nDigite o ID do pedido: ')
        Pedido.verificarPedido(id)

    @staticmethod
    def cancelarPedido():
        id = input('\nDigite o ID do pedido: ')
        pedido = Dbmanager.getOrder(id)
        try:
            status = pedido['Status']

            if status != 'Aprovado':
                Pedido.mudarPedido(id, 'Cancelado')
            else:
                print('Pedido já foi pago e não pode ser cancelado!')
        except TypeError:
            print('Pedido não encontrado.')

    @staticmethod
    def listarTodosProdutos():
        produtos = Dbmanager.getAllProducts()
        for produto in produtos:
            print(str(produto))

    @staticmethod
    def listarPedidosCliente():
        op = input('\nProcurar o cliente por:\n1 - Id\n2 - Documento\n')
        inp = input('Numero: ')
        cliente = ClienteController.buscarCliente(inp, op)
        if cliente is None:
            print('Cliente não encontrado.')
            return
        id = cliente
        allPedidos = Dbmanager.getAllCustomerOrders()
        for pedido in allPedidos:
            order = pedido.split(',')
            if order[0] == id:
                pedido_obj =Dbmanager.getOrder(order[1])
                print('-'*10)
                try:
                    for k in pedido_obj:
                        if isinstance(pedido_obj[k], list):
                            for item in pedido_obj[k]:
                                print(item)
                        else:
                            print('{}: {}'.format(k, pedido_obj[k]))
                    return
                except ValueError:
                    pass
        print('Cliente não encontrado.')

    @staticmethod
    def inserirProduto():
        id = len(Dbmanager.getAllProducts()) + 1
        n = input('Nome: ')
        preco = None
        while isinstance(preco, int) == False:
            try:
                preco = int(input('Preço: R$ '))
            except ValueError:
                print('Valor Inválido.')
        preco = str(preco)
        prod = str(id) + ':' + n + ':' + preco + '\n'
        Dbmanager.setProduct(prod)


    @staticmethod
    def pagarPedido(idP=False):
        if not idP:
            id = input('Digite o id do pedido:')
        else:
            id = str(idP)
        pedido = Dbmanager.getOrder(id)
        try:
            status = pedido['Status']
            if status != 'Aprovado':
                Pedido.fazerPagamento(pedido['Total'], pedido['Id'])
            else:
                print('Pedido já foi pago e aprovado.')
        except TypeError:
            print('Pedido não encontrado.')

    @staticmethod
    def buscarNF():
        id = input('Digite o id do pedido:')
        try:
            status = Dbmanager.getOrder(id)['Status']
            if status == 'Aprovado':
                nf = Dbmanager.getNF(id)
                infosNF = nf.infosNF()
                if infosNF['Tipo'] == '1':
                    infosNF['Tipo'] = 'Crédito'
                elif infosNF['Tipo'] == '2':
                    infosNF['Tipo'] = 'Débito'
                elif infosNF['Tipo'] == '3':
                    infosNF['Tipo'] = 'Dinheiro'

                for k, v in infosNF.items():
                    print('{}: {}'.format(str(k), str(v)))
            else:
                print('Esse pedido ainda não foi pago e não foi gerada uma NF para ele ainda.')
        except TypeError:
            print('Pedido não encontrado.')



