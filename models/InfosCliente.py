from models.Telefone import Telefone
from models.Email import Email
from models.Endereco import Endereco

class InfosCliente:
    """
    Party que unifica informações do cliente em uma unica classe.
    """

    def __init__(self, ddd, ntel, em, n, log, bai, cid):
        self.tel = Telefone(ddd, ntel)
        self.email = Email(em)
        self.end = Endereco(n, log, bai, cid)


    def getTel(self):
        return self.tel

    def getEmail(self):
        return self.email

    def getEnd(self):
        return self.end
