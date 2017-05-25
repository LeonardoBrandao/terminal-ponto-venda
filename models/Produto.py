class Produto:

    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return 'ID: {}, {}, R$ {}'.format(self.id, self.nome, self.preco)

    def toSave(self):
        return '{}%{}%'.format(self.id, self.nome)