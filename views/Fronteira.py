from controllers.PedidoController import PedidoController

if __name__ == "__main__":
    controller = PedidoController()

    while True:
        print('\n1 - Fazer pedido.')
        print('2 - Buscar pedido.')
        print('3 - Buscar todos pedidos do cliente.')
        print('4 - Pagar pedido.')
        print('5 - Cancelar pedido.')
        print('6 - Buscar NF.')
        print('7 - Buscar produto.')
        print('8 - Listar todos produtos.')
        print('9 - Inserir produto.')
        print('0 - SAIR.')

        op = int(input("Selecione uma opção: "))

        if op == 1:
            controller.criarPedido()

        elif op == 2:
            controller.verificarPedido()

        elif op == 3:
            controller.listarPedidosCliente()

        elif op == 4:
            controller.pagarPedido()

        elif op == 5:
            controller.cancelarPedido()

        elif op == 6:
            controller.buscarNF()

        elif op == 7:
            controller.buscarProduto()

        elif op == 8:
            controller.listarTodosProdutos()

        elif op == 9:
            controller.inserirProduto()

        elif op == 0:
            break
