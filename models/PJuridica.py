from models.InfosCliente import InfosCliente
from models.Cliente import Cliente
from controllers.Dbmanager import Dbmanager

class PessoaJuridica(Cliente):
    def __init__(self, *args):
        super().__init__(args[0], args[1], args[2])
        self.cnpj = args[3]
        self.infosCliente = InfosCliente(args[4], args[5], args[6], args[7], args[8], args[9], args[10])

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