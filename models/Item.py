class Item:

    def __init__(self, produto, qnt):
        self.produto = produto
        self.quantidade = qnt

    def __str__(self):
        return '{}, Quantidade: {}'.format(str(self.produto), self.quantidade)