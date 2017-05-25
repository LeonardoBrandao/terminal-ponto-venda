from models.Pedido import Pedido
from controllers.Dbmanager import Dbmanager

class PedidoController:
    pedido = None


    @staticmethod
    def buscarProduto():
        file = open('controllers/produtos.txt', 'r').readlines()
        print('')
        for line in file:
            product = line.split(':')
            print('ID: {} - {} - R$ {}'.format(product[0], product[1], product[2]), end='')
        print('')

    def criarPedido(self):
        file = open('controllers/produtos.txt', 'r').readlines()
        ids = []
        for line in file:
            product = line.split(':')
            print('ID: {} - {} - R$ {}'.format(product[0], product[1], product[2]), end='')
            ids.append(int(product[0]))

        carrinho = []

        while True:
            id_prod = int(input("\nId do produto para ser adicionado: "))
            qnt = int(input("Quantidade: "))
            carrinho.append([id_prod, qnt])

            quit = input('Fechar pedido? [s/N]')
            if quit == 's' or quit == 'S':
                break

        self.pedido = Pedido(carrinho)
        self.pedido.salvarPedido()
        self.pedido.infosPagamento()

    @staticmethod
    def verificarPedido():
        id = input('\n\nDigite o ID do pedido: ')
        Pedido.verificarPedido(id)

    @staticmethod
    def cancelarPedido():
        id = input('\n\nDigite o ID do pedido: ')
        pedido = Dbmanager.getOrder(id)
        status = pedido['Status']

        if status != 'Aprovado':
            Pedido.cancelarPedido(id, 'Cancelado')
        else:
            print('Pedido já foi pago e não pode ser cancelado!')

    @staticmethod
    def listarPedidosCliente():
        pass


