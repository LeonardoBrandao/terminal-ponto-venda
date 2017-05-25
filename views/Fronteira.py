from controllers.PedidoController import PedidoController

if __name__ == "__main__":
    controller = PedidoController()

    while True:
        print('\n1 - Buscar produto.')
        print('2 - Fazer pedido.')
        print('3 - Verificar estado do pedido.')
        print('4 - Cancelar pedido.')
        print('0 - SAIR.')

        op = int(input("Selecione uma opção: "))

        if op == 1:
            controller.buscarProduto()

        elif op == 2:
            controller.criarPedido()

        elif op == 3:
            controller.verificarPedido()

        elif op == 4:
            controller.listarPedidosCliente()

        elif op == 5:
            controller.cancelarPedido()

        elif op == 0:
            break
