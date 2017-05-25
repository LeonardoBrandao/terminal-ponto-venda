import collections

from models.Item import Item
from models.Produto import Produto


class Dbmanager:

    # metodos relacionados ao produto

    @staticmethod
    def setProduct(prod):
        f = open('controllers/produtos.txt', 'a')
        f.write(prod)
        f.close()

    @staticmethod
    def getProduct(prod_id):
        produtos_txt = open('controllers/produtos.txt', 'r').readlines()
        for produto_line in produtos_txt:
            infos = produto_line.strip('\n').split(':')
            if infos[0] == str(prod_id):
                id = infos[0]
                name = infos[1]
                price = infos[2]
                return Produto(id, name, price)
        return None

    @staticmethod
    def getAllProducts():
        produtos_txt = open('controllers/produtos.txt', 'r').readlines()
        products = []
        for produto_line in produtos_txt:
            infos = produto_line.strip('\n').split(',')
            id = infos[0]
            name = infos[1]
            price = infos[2]
            products.append(Produto(id, name, price))
        return products

    # metodos relacionados ao pedido

    @staticmethod
    def setOrder(order):
        pedido = ''
        for i in range(len(order) - 1):
            if order[i] == order[-2]:
                pedido += order[i] + '\n'
            else:
                pedido += order[i] + ','

        f = open('controllers/pedidos.txt', 'a')
        f.write(pedido)
        f.close()

    @staticmethod
    def getOrder(order_id):
        pedidos_txt = open('controllers/pedidos.txt', 'r').readlines()
        for pedido_line in pedidos_txt:
            pedido = pedido_line.strip(':\n').split(',')
            if pedido[0] == order_id:
                itens = pedido[3].split(':')
                itens_pedido = []
                for item in itens:
                    item = item.strip(':\n').split('%')
                    product = Dbmanager.getProduct(item[0])
                    qnt = item[2]
                    itens_pedido.append(Item(product, qnt))
                order = collections.OrderedDict()
                order['Id'] = pedido[0]
                order['Data'] = pedido[1]
                order['Status'] = pedido[2]
                order['Itens'] = itens_pedido

                return order
        return None

    @staticmethod
    def getAllOrders():
        pedidos_txt = open('controllers/pedidos.txt', 'r').readlines()
        pedidos = []
        for pedido_line in pedidos_txt:
            pedidos.append(pedido_line.strip(':\n'))
        return pedidos

    @staticmethod
    def alterStateOrder(id, state):
        pedidos_txt = open('controllers/pedidos.txt', 'r').readlines()
        f = open('controllers/pedidos.txt', 'w')
        for pedido_line in pedidos_txt:
            pedido = pedido_line.strip(':\n').split(',')
            if pedido[0] != id:
                f.write(pedido_line)
            else:
                line = pedido_line.strip(':\n').split(',')
                wline = line[0] + line[1] + state + line[3]
                f.write(wline)
        f.close()

    # metodos relacionados ao cliente

    @staticmethod
    def getCustomer(id = False, identif = False):
        clientes_txt = open('controllers/clientes.txt', 'r').readlines()
        for cliente_line in clientes_txt:
            c_infos = cliente_line.strip(',\n').split(',')
            if c_infos[2] == str(identif) or c_infos[0] == str(id):
                return c_infos[0]
        return None

    @staticmethod
    def getAllCustomers():
        clientes_txt = open('controllers/clientes.txt', 'r').readlines()
        clientes = []
        for cliente_line in clientes_txt:
            clientes.append(cliente_line.strip(':\n'))
        return clientes

    @staticmethod
    def saveCustomer(infos):
        f = open('controllers/clientes.txt', 'a')
        infos_save = ''

        for info in infos:
            infos_save += (str(info) + ',')

        infos_save.strip(',')
        infos_save += '\n'

        f.writelines(infos_save)

    # metodos para relacionar pedidos e clientes

    @staticmethod
    def relCustomerOrder(cid, oid):
        f = open('controllers/relClientePedido.txt', 'a')
        f.write(cid + ',' + oid + '\n')
        f.close()

    @staticmethod
    def getCustomerOrder(cli = False, ord = False):
        if cli:
            txt = open('controllers/relClientePedido.txt', 'r').readlines()
            for line in txt:
                content = line.strip('\n').split(',')
                if str(cli) == content[0]:
                    return content[1]
        elif ord:
            txt = open('controllers/relClientePedido.txt', 'r').readlines()
            for line in txt:
                content = line.strip('\n').split(',')
                if str(ord) == content[1]:
                    return content[0]

        return None
