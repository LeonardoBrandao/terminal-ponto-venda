class Telefone:
    def __init__(self, ddd, n):
        self.ddd = ddd
        self.num = n

    def __str__(self):
        return '({}) {}'.format(self.ddd, self.num)