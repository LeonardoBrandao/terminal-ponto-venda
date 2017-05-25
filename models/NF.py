class NotaFiscal:
    def __init__(self, total, tipo_pag, pedido):
        self.total = total
        self.taxa = total*0.2
        self.tipo_pagamento = tipo_pag
        self.data = pedido.data

        nf = [
            str(pedido.idPedido),
            str(self.data),
            str(self.tipo_pagamento),
            str(self.taxa),
            str(self.total)
        ]

        f = open('NfPedido' + pedido.idPedido + '.txt', 'w')
        f.writelines(nf)
        f.close()