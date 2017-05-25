import datetime
from controllers.Dbmanager import Dbmanager
from controllers.ClienteController import ClienteController


class Pedido:
    def __init__(self, carrinho):
        file = open('controllers/pedidos.txt', 'r')
        self.linhas_txt = len(file.readlines())
        file.close()
        self.idPedido = self.linhas_txt + 1
        dt = datetime.datetime.now()
        dt = datetime.date(dt.year, dt.month, dt.day)
        self.date = datetime.date.strftime(dt, '%d/%m/%y')
        self.pago = False
        self.status = 'Aguardando Pagamento'
        self.carrinho = carrinho

    @staticmethod
    def verificarPedido(pedido_id):
        pedido = Dbmanager.getOrder(pedido_id)
        try:
            for k in pedido:
                if isinstance(pedido[k], list):
                    for item in pedido[k]:
                        print(item)
                else:
                    print('{}: {}'.format(k, pedido[k]))
        except ValueError:
            pass

    def salvarPedido(self):
        itens = ''
        for i in self.carrinho:
            item = Dbmanager.getProduct(i[0])
            itens += (item.toSave() + str(i[1]) + ':')

        (criarC, doc) = ClienteController.novoCliente()
        if criarC == True:
            cliente = ClienteController.criarCliente()
        else:
            cliente = ClienteController.buscarCliente(criarC, doc)

        order = [str(self.idPedido), str(self.date), str(self.status), str(itens), '\n']

        Dbmanager.setOrder(order)
        Dbmanager.relCustomerOrder(str(cliente), str(self.idPedido))

    def infosPagamento(self, *args):
        pass

    @staticmethod
    def cancelarPedido(id, state):
        Dbmanager.alterStateOrder(id, state)