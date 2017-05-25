from controllers.PedidoController import PedidoController

if __name__ == "__main__":
    controller = PedidoController()

    while True:
        print('\n1 - Fazer pedido.')
        print('2 - Verificar estado do pedido.')
        print('3 - Buscar pedidos do cliente.')
        print('4 - Cancelar pedido.')
        print('5 - Buscar produto.')
        print('6 - Inserir produto.')
        print('0 - SAIR.')

        op = int(input("Selecione uma opção: "))

        if op == 1:
            controller.criarPedido()

        elif op == 2:
            controller.verificarPedido()

        elif op == 3:
            controller.listarPedidosCliente()

        elif op == 4:
            controller.cancelarPedido()

        elif op == 5:
            controller.buscarProduto()

        elif op == 6:
            controller.inserirProduto()

        elif op == 0:
            break
