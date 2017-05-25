class Endereco:
    def __init__(self, n, log, bairro, cidade):
        self.num = n
        self.logradouro = log
        self.bairro = bairro
        self.cidade = cidade

    def __str__(self):
        return '{}, {}, {} - {}'.format(self.logradouro, self.num, self.bairro, self.cidade)