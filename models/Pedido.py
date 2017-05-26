import datetime
import os

from controllers.Dbmanager import Dbmanager
from controllers.ClienteController import ClienteController


class Pedido:
    def __init__(self, carrinho):
        file = open(os.path.abspath('pedidos.txt'), 'r')
        self.linhas_txt = len(file.readlines())
        file.close()
        self.idPedido = self.linhas_txt + 1
        dt = datetime.datetime.now()
        dt = datetime.date(dt.year, dt.month, dt.day)
        self.date = datetime.date.strftime(dt, '%d/%m/%y')
        self.pago = False
        self.status = 'Aguardando Pagamento'
        self.carrinho = carrinho
        self.total = 0
        for item in self.carrinho:
            preco = str(Dbmanager.getProduct(item[0]).preco).replace(',', '.')
            self.total += round((float(preco) * item[1]), 2)
        self.total = str(self.total)

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
        except (ValueError, TypeError) as e:
            print('Pedido não encontrado, tente novamente.')

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

        order = [str(self.idPedido), str(self.date), str(self.total), str(self.status), str(itens), '\n']

        Dbmanager.setOrder(order)
        Dbmanager.relCustomerOrder(str(cliente), str(self.idPedido))

    @staticmethod
    def fazerPagamento(total, idPedido):
        tipo = input('\n1 - Credito\n2 - Debito\n3 - Dinheiro')
        pag = input('Pagamento aprovado? [S/n] ')
        data = datetime.datetime.now()
        data = datetime.date(data.year, data.month, data.day)
        data = datetime.date.strftime(data, '%d/%m/%y')
        if pag == 'n' or pag == 'N':
            print('Pagamento foi recusado.')
            Pedido.mudarPedido(idPedido, 'Pagamento Recusado')
        else:
            Dbmanager.setNF(tipo, data, total, idPedido)
            Pedido.mudarPedido(idPedido, 'Aprovado')

    @staticmethod
    def mudarPedido(id, state):
        Dbmanager.alterStateOrder(id, state)