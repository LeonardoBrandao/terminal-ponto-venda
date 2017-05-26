import collections
import os

from models.Item import Item
from models.Produto import Produto
from models.NF import NotaFiscal


class Dbmanager:

    # metodos relacionados ao produto

    @staticmethod
    def setProduct(prod):
        f = open(os.path.abspath('controllers/produtos.txt'), 'a')
        f.write(prod)
        f.close()

    @staticmethod
    def getProduct(prod_id):
        produtos_txt = open(os.path.abspath('controllers/produtos.txt'), 'r').readlines()
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
        produtos_txt = open(os.path.abspath('controllers/produtos.txt'), 'r').readlines()
        products = []
        for produto_line in produtos_txt:
            infos = produto_line.strip('\n').split(':')
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

        f = open(os.path.abspath('controllers/pedidos.txt'), 'a')
        f.write(pedido)
        f.close()

    @staticmethod
    def getOrder(order_id):
        pedidos_txt = open(os.path.abspath('controllers/pedidos.txt'), 'r').readlines()
        for pedido_line in pedidos_txt:
            pedido = pedido_line.strip(':\n').split(',')
            if pedido[0] == order_id:
                itens = pedido[4].split(':')
                itens_pedido = []
                for item in itens:
                    item = item.strip(':\n').split('%')
                    product = Dbmanager.getProduct(item[0])
                    qnt = item[2]
                    itens_pedido.append(Item(product, qnt))
                order = collections.OrderedDict()
                order['Id'] = pedido[0]
                order['Data'] = pedido[1]
                order['Total'] = pedido[2]
                order['Status'] = pedido[3]
                order['Itens'] = itens_pedido

                return order
        return None

    @staticmethod
    def getAllOrders():
        pedidos_txt = open(os.path.abspath('controllers/pedidos.txt'), 'r').readlines()
        pedidos = []
        for pedido_line in pedidos_txt:
            pedidos.append(pedido_line.strip(':\n'))
        return pedidos

    @staticmethod
    def alterStateOrder(id, state):
        pedidos_txt = open(os.path.abspath('controllers/pedidos.txt'), 'r').readlines()
        f = open(os.path.abspath('controllers/pedidos.txt'), 'w')
        for pedido_line in pedidos_txt:
            pedido = pedido_line.strip(':\n').split(',')
            if pedido[0] != id:
                f.write(pedido_line)
            else:
                line = pedido_line.strip(':\n').split(',')
                wline = line[0] + ',' + line[1] + ',' + line[2] + ',' + state + ',' + line[4]+ ':\n'
                f.write(wline)
        f.close()

    # metodos relacionados ao cliente

    @staticmethod
    def getCustomer(id = False, identif = False):
        clientes_txt = open(os.path.abspath('controllers/clientes.txt'), 'r').readlines()
        for cliente_line in clientes_txt:
            c_infos = cliente_line.strip(',\n').split(',')
            if c_infos[3] == str(identif) or c_infos[0] == str(id):
                return c_infos[0]
        return None

    @staticmethod
    def getAllCustomers():
        clientes_txt = open(os.path.abspath('controllers/clientes.txt'), 'r').readlines()
        clientes = []
        for cliente_line in clientes_txt:
            clientes.append(cliente_line.strip(':\n'))
        return clientes

    @staticmethod
    def saveCustomer(infos):
        f = open(os.path.abspath('controllers/clientes.txt'), 'a')
        infos_save = ''

        for info in infos:
            infos_save += (str(info) + ',')

        infos_save.strip(',')
        infos_save += '\n'

        f.writelines(infos_save)

    # metodos para relacionar pedidos e clientes

    @staticmethod
    def relCustomerOrder(cid, oid):
        f = open(os.path.abspath('controllers/relClientePedido.txt'), 'a')
        f.write(cid + ',' + oid + '\n')
        f.close()

    @staticmethod
    def getCustomerOrder(cli = False, ord = False):
        if cli:
            txt = open(os.path.abspath('controllers/relClientePedido.txt'), 'r').readlines()
            for line in txt:
                content = line.strip('\n').split(',')
                if str(cli) == content[0]:
                    return content[1]
        elif ord:
            txt = open(os.path.abspath('controllers/relClientePedido.txt'), 'r').readlines()
            for line in txt:
                content = line.strip('\n').split(',')
                if str(ord) == content[1]:
                    return content[0]

        return None

    @staticmethod
    def getAllCustomerOrders():
        co_txt = open(os.path.abspath('controllers/relClientePedido.txt'), 'r').readlines()
        co = []
        for co_line in co_txt:
            co.append(co_line.strip(':\n'))
        return co

    # metodos relacionados a NF

    @staticmethod
    def setNF(tipo, date, total, order_id):
        id = Dbmanager.getAllNFs() + 1
        taxa = round(float(total) * 0.2, 2)
        f = open(os.path.abspath('controllers/nfs.txt'), 'a')
        nf = str(id) + ':' + str(order_id) + ':' + tipo + ':' + date + ':' + str(taxa) + ':' + str(total) + '\n'
        f.write(nf)
        f.close()

    @staticmethod
    def getNF(order_id):
        f = open(os.path.abspath('controllers/nfs.txt'), 'r').readlines()
        for line in f:
            infos = line.strip('\n').split(':')
            if infos[1] == str(order_id):
                id = infos[0]
                pedidoId = infos[1]
                tipo = infos[2]
                data = infos[3]
                total = infos[5]
                return NotaFiscal(id, pedidoId, tipo, data, total)
        return None

    @staticmethod
    def getAllNFs():
        try:
            f = open(os.path.abspath('controllers/nfs.txt'), 'r').readlines()
            return len(f)
        except FileNotFoundError:
            return 0
