from controllers.Dbmanager import Dbmanager
from models.PJuridica import PessoaJuridica
from models.PFisica import PessoaFisica

class ClienteController:
    @staticmethod
    def novoCliente():
        i = input('1 - Novo Cliente.\n2 - Buscar Cliente.\n')
        if i == '1':
            return (True, 1)
        elif i == '2':
            op = input('1 - Id\n2 - Documento\n')
            if op == '1':
                id = input('Id do cliente: ')
                return (id, op)
            elif op == '2':
                id = input('Numero do documento do cliente: ')
                return (id, op)

    @staticmethod
    def criarCliente():
        infos = []

        op = input('1 - Pessoa Fisica\n2 - Pessoa Juridica\n')

        while int(op) not in [1, 2]:
            print('Valor invalido')
            op = input('1 - Pessoa Fisica\n2 - Pessoa Juridica\n')

        infos.append(len(Dbmanager.getAllCustomers()) + 1)  # id
        infos.append(input('Nome: '))
        if op == '1':
            infos.append('PF')
            infos.append(input('CPF: '))
        elif op == '2':
            infos.append('PJ')
            infos.append(input('CNPJ: '))
        infos.append(input('DDD tel: '))
        infos.append(input('Numero tel: '))
        infos.append(input('Email: '))
        end = input('Endereço: ')
        n = input('Num: ')
        infos.append(n)
        infos.append(end)
        infos.append(input('Bairro: '))
        infos.append(input('Cidade: '))

        Dbmanager.saveCustomer(infos)
        if op == '1':
            return PessoaFisica(infos).id
        elif op == '2':
            return PessoaJuridica(infos).id

    @staticmethod
    def buscarCliente(id, op):
        if op == '1':
            return Dbmanager.getCustomer(id=id)
        else:
            return Dbmanager.getCustomer(identif=str(id))