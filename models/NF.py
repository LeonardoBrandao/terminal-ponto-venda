import collections


class NotaFiscal:
    def __init__(self, id, idPedido, tipo, data, total,):
        self.id = id
        self.idPedido = idPedido
        self.tipo = tipo
        self.data = data
        self.total = str(total).replace(',', '.')
        self.taxa = round(float(self.total)*0.2, 2)

    def infosNF(self):
        return collections.OrderedDict([
            ('Id', self.id),
            ('Id Pedido', self.idPedido),
            ('Tipo', self.tipo),
            ('Data', self.data),
            ('Taxa', self.taxa),
            ('Total', self.total)
        ])