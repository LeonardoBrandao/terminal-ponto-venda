from models.InfosCliente import InfosCliente
from models.Cliente import Cliente
from controllers.Dbmanager import Dbmanager

class PessoaJuridica(Cliente):
    def __init__(self, *args):
        super().__init__(args[0][0], args[0][1], args[0][2])
        self.cnpj = args[0][3]
        self.infosCliente = InfosCliente(args[0][4], args[0][5], args[0][6], args[0][7],
                                         args[0][8], args[0][9], args[0][10])

    def salvar(self):
        infos = [
            str(self.id),
            str(self.name),
            str(self.cnpj),
            str(self.infosCliente.getEnd()),
            str(self.infosCliente.getEmail()),
            str(self.infosCliente.getTel()),
        ]

        Dbmanager.saveCustomer(infos)