# terminal-ponto-venda

Simulação de um tpv guardando dados em txt's.

## Isso é um projeto de faculdade, não usar em casos reais!

## Infos:
Método Main está em Fronteira.py

Estutura dos txt's:

    produtos:

        id:nome:valor


    clientes:

        id,nome,cpf/cnpj,ddd,tel,email,logradouro,numero,bairro,cidade


    pedidos:

        id,data,valor,status,carrinho

        itens no carrinho sao separados por :

        propriedade de cada produto é separada por %


    relClientePedido:

        Guarda a relação de qual cliente fez qual pedido.

        idCliente,idPedido


    nfs:

        idDaNf:idPedidoCorrespondente:tipoPagamento:data:taxa:total


DAO = controllers/Dbmanager.py