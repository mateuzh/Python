import mysql.connector
from time import sleep


def separador():
    print(f"-=-"*30)


crud = mysql.connector.connect(
    host='localhost',
    user='teste',
    password='1234',
    database='crud_PY'
)

busca = crud.cursor()

delete = f"delete " \
         f"vendas, " \
         f"detalhes_venda, " \
         f"from " \
         f"detalhes_venda " \
         f"inner join vendas on detalhes_venda.id = vendas.id " \
         f"where datediff(NOW(), data_venda) > 5 and tipo_pgto = '0' and pagamento = '0'; "
print("-=-=-= BEM-VINDO =-=-=-\n-=- LOJA VIRTUAL PY -=-")
while True:
    usuario = int(input("Menu:\n"
                        "1- Clientes \n"
                        "2- Produtos\n"
                        "3- Vendas\n"
                        "4- Relatórios \n"
                        "0- Finalizar\n"
                        "Resposta: "))
    separador()
    if usuario == 0:
        print(f"Finalizando... ")
        sleep(1)
        break
    elif usuario == 1:
        while True:
            menuClientes = int(input("Clientes: \n"
                                     "1- Novo cliente \n"
                                     "2- Tabela de Clientes \n"
                                     "3- Atualizar informações\n "
                                     "0- Menu Inicial\n"
                                     "-> "))
            separador()
            if menuClientes == 1:
                cpf = int(input("CPF: "))
                nomeCliente = str(input("Nome: "))
                comando = f"insert into clientes (cpf, nome) values ('{cpf}','{nomeCliente}');"
                busca.execute(comando)
                crud.commit()
                telefone = str(input("Telefone: ")).strip().split()
                tipo = str(input("Tipo: Ex: Residencial, Comercial, Pessoal -> "))
                comando = f"insert into telefones (id, ddd, numero, tipo) values ('{cpf}'," \
                          f"'{telefone[0]}','{telefone[1]}','{tipo}');"
                busca.execute(comando)
                crud.commit()
                separador()
            elif menuClientes == 2:
                comando = f"select telefones.id as Cpf, clientes.nome as Nome,telefones.ddd as DDD, " \
                          f"telefones.numero as Numero, telefones.tipo as Tipo from telefones " \
                          f"inner join clientes on telefones.id = clientes.cpf;"
                busca.execute(comando)
                telefones = busca.fetchall()
                print(f'{"CPF":<6}  {"NOME":<6}  {"DDD":<6}  {"TELEFONE":<15}  {"TIPO":<5}')
                for NumerosTelefone in telefones:
                    print(NumerosTelefone)
                separador()
            elif menuClientes == 3:
                cpf = int(input("CPF: "))
                comando = f"select clientes.cpf, clientes.nome, telefones.ddd, telefones.numero, telefones.tipo " \
                          f"from clientes " \
                          f"inner join telefones on clientes.cpf = telefones.id " \
                          f"where cpf = '{cpf}'"
                busca.execute(comando)
                clientes = busca.fetchall()
                for nome in clientes:
                    print(nome)
                separador()
                nomeNovo = str(input("Novo nome: "))
                novoNumero = str(input("Número: ")).strip().split()
                novoTipo = str(input("Novo tipo: Ex: Residencial, Comercial ou Pessoal "))
                update = f"update clientes set nome = '{nomeNovo}' where cpf = '{cpf}';"
                busca.execute(update)
                crud.commit()
                updateTelefones = f"update telefones set ddd = '{novoNumero[0]}', numero = '{novoNumero[1]}', " \
                                  f"tipo = '{novoTipo}' where id = '{cpf}';"
                busca.execute(updateTelefones)
                crud.commit()
                print("Cadastro atualizado com sucesso! ")
                separador()
            elif menuClientes == 0:
                break
    elif usuario == 2:
        while True:
            menuProdutos = int(input("Produtos:\n"
                                     "1- Tabela de Produtos\n"
                                     "2- Novo produto\n"
                                     "3- Atualizar Produto\n "
                                     "0- Menu Inicial\n"
                                     "Opção: "))
            separador()
            if menuProdutos == 1:
                select = f"select id, descricao, preco, quantidade from produtos"
                busca.execute(select)
                tabelaProdutos = busca.fetchall()
                for p in tabelaProdutos:
                    print(p)
                separador()
            elif menuProdutos == 2:
                print("Cadastro de produto: ")
                descricaoProduto = str(input("Descricao do produto: ")).strip()
                valorProduto = float(input("Preço: R$"))
                quantidade = int(input("Quantidade: "))
                insert = f"insert into produtos " \
                         f"(descricao, preco, quantidade) " \
                         f"values ('{descricaoProduto}','{valorProduto}','{quantidade}')"
                busca.execute(insert)
                crud.commit()
                separador()
            elif menuProdutos == 3:
                print("Atualizar/Alterar dados de um produto:")
                idProduto = int(input("ID: "))
                select = f"select id, descricao, preco, quantidade from produtos where id = '{idProduto}'"
                busca.execute(select)
                Produto = busca.fetchall()
                for p in Produto:
                    print(p)
                print("Atualize os dados preenchendo os campos abaixo: \n")
                novaDescricao = str(input("Descrição: "))
                novoPreco = float(input("Preço: R$"))
                quantidadeAtualizada = int(input("Quantidade: "))
                update = f"update produtos set descricao = '{novaDescricao}', preco = '{novoPreco}', " \
                         f"quantidade = '{quantidadeAtualizada}' where id = '{idProduto}';"
                busca.execute(update)
                crud.commit()
                separador()
            elif menuProdutos == 0:
                break
    elif usuario == 3:
        while True:
            menuVendas = int(input("Menu de Vendas:\n"
                                   "1- Nova venda\n"
                                   "2- Consultar vendas\n"
                                   "3- Pagamentos \n"
                                   "0- Menu Inicial\n"
                                   "-> "))
            separador()
            if menuVendas == 1:
                cpfVenda = int(input("CPF do cliente: "))
                idProduto = int(input("ID do produto: "))
                pagamento = int(input("Pagamento:\n"
                                      "1- Debito, Credito, Dinheiro, Pix \n"
                                      "0- Boleto ainda não compensado\n"
                                      "Resposta: "))
                separador()
                if pagamento == 1:
                    autorizacaoEntrega = 1
                else:
                    autorizacaoEntrega = 0
                insertVendas = f"insert into vendas (cpf, id_produto, pagamento, entrega) " \
                               f"values ('{cpfVenda}','{idProduto}',{pagamento},{autorizacaoEntrega})"
                busca.execute(insertVendas)
                crud.commit()
                selectNovaVenda = f"select id from vendas where cpf = '{cpfVenda}'"
                busca.execute(selectNovaVenda)
                novaVenda = busca.fetchall()
                Data = str(input("Data da venda: ")).strip().split('/')
                quantidade = int(input("Quantidade: "))
                formaPagamento = int(input("Forma de pagamento:\n"
                                           "1- Cartao de Crédito/Debito\n"
                                           "2- Dinheiro/Cheque/Pix\n"
                                           "3- Boleto\n"
                                           "-> "))
                insertDetalhes = f"insert into detalhes_venda " \
                                 f"(id, id_produto, cpf_cliente, data_venda, quantidade, tipo_pgto) " \
                                 f"values" \
                                 f"('{novaVenda[0][0]}','{idProduto}','{cpfVenda}','{Data[2]}-{Data[1]}-{Data[0]}'," \
                                 f"'{quantidade}'," \
                                 f"'{formaPagamento}')"
                separador()
            elif menuVendas == 2:
                select = f"select vendas.id, vendas.cpf, clientes.nome, vendas.id_produto, " \
                         f"vendas.pagamento, vendas.entrega, " \
                         f"detalhes_venda.data_venda, detalhes_venda.quantidade, " \
                         f"produtos.preco * detalhes_venda.quantidade, " \
                         f"detalhes_venda.tipo_pgto " \
                         f"from vendas " \
                         f"inner join detalhes_venda on vendas.id = detalhes_venda.id " \
                         f"inner join produtos on vendas.id_produto = produtos.id " \
                         f"inner join clientes on vendas.cpf = clientes.cpf ; "
                busca.execute(select)
                tabelaVendas = busca.fetchall()
                for v in tabelaVendas:
                    print(v)
                separador()
            elif menuVendas == 3:
                while True:
                    print("Vendas com boletos ainda pendentes: ")
                    select = f"select clientes.nome, " \
                             f"vendas.id, " \
                             f"produtos.descricao, " \
                             f"detalhes_venda.quantidade, " \
                             f"detalhes_venda.quantidade * produtos.preco as Preco, " \
                             f"vendas.pagamento " \
                             f"from vendas " \
                             f"inner join clientes on vendas.cpf = clientes.cpf " \
                             f"inner join produtos on vendas.id_produto = produtos.id " \
                             f"inner join detalhes_venda on vendas.id = detalhes_venda.id " \
                             f"where vendas.pagamento = '0'; "
                    busca.execute(select)
                    pendencias = busca.fetchall()
                    for p in pendencias:
                        print(p)
                    separador()
                    pagamento = int(input("Deseja marcar alguma das vendas acima como paga? \n"
                                          "1- Alterar pagamento para efetuado \n"
                                          "2- Alterar pagamento para pendente\n"
                                          "3- Voltar\n"
                                          "->"))
                    separador()
                    if pagamento == 1:
                        cpf = int(input("CPF: "))
                        updatePendencias = f"update vendas set pagamento = 1, entrega = 1 where cpf = '{cpf}'"
                        busca.execute(updatePendencias)
                        crud.commit()
                    elif pagamento == 2:
                        cpf = int(input("CPF: "))
                        updatePendencias = f"update vendas set pagamento = 0, entrega = 0 where cpf = '{cpf}'"
                        busca.execute(updatePendencias)
                        crud.commit()
                    elif pagamento == 3:
                        break
            elif menuVendas == 0:
                break
    elif usuario == 4:
        while True:
            escolhaRelatorio = int(input("Relatórios disponíveis: \n"
                                         "1- Total vendido em quantidade e valores de cada produto\n"
                                         "2- Total comprado em produtos, quantidade e valores por cada cliente\n"
                                         "3- Total comprado por um cliente específico\n"
                                         "4- Total em vendas com boletos abertos  (que ainda não foram pagos)\n"
                                         "0- Sair\n"
                                         "->"))
            separador()
            if escolhaRelatorio == 1:
                selectRelatorio = f"select produtos.descricao as Produto, " \
                                  f"produtos.preco * detalhes_venda.quantidade as valor, " \
                                  f"detalhes_venda.quantidade as Quantidade " \
                                  f"from vendas " \
                                  f"inner join produtos on vendas.id_produto = produtos.id " \
                                  f"inner join detalhes_venda on vendas.id = detalhes_venda.id; "
                busca.execute(selectRelatorio)
                Relatorio1 = busca.fetchall()
                print(f"1- Total vendido em quantidade e valores de cada produto\n")
                for r in Relatorio1:
                    print(r)
                separador()
            elif escolhaRelatorio == 2:
                selectRelatorio = f"select " \
                                  f"clientes.nome as Nome, " \
                                  f"detalhes_venda.quantidade as Quantidade, " \
                                  f"produtos.preco * detalhes_venda.quantidade as Preco, " \
                                  f"produtos.descricao as Descricao " \
                                  f"from clientes " \
                                  f"inner join detalhes_venda on clientes.cpf = detalhes_venda.cpf_cliente " \
                                  f"inner join produtos on detalhes_venda.id_produto = produtos.id; "
                busca.execute(selectRelatorio)
                Relatorio2 = busca.fetchall()
                print(f"2- Total comprado em produtos, quantidade e valores por cada cliente\n")
                for r2 in Relatorio2:
                    print(r2)
                separador()
            elif escolhaRelatorio == 3:
                print(f"3- Total comprado por um cliente específico")
                cpf = int(input("CPF: "))
                selectRelatorio = f"select " \
                                  f"clientes.nome, " \
                                  f"produtos.descricao, " \
                                  f"detalhes_venda.quantidade, " \
                                  f"detalhes_venda.quantidade * produtos.preco as Valor " \
                                  f"from clientes " \
                                  f"inner join detalhes_venda on clientes.cpf = detalhes_venda.cpf_cliente " \
                                  f"inner join produtos on detalhes_venda.id_produto = produtos.id " \
                                  f"where clientes.cpf = '{cpf}'; "
                busca.execute(selectRelatorio)
                Relatorio3 = busca.fetchall()
                for r3 in Relatorio3:
                    print(r3)
                separador()
            elif escolhaRelatorio == 4:
                print("4- Total em vendas com boletos abertos  (que ainda não foram pagos)")
                selectRelatorio = f"select clientes.nome, " \
                                  f"vendas.id, " \
                                  f"produtos.descricao, " \
                                  f"detalhes_venda.quantidade, " \
                                  f"detalhes_venda.quantidade * produtos.preco as Preco, " \
                                  f"vendas.pagamento " \
                                  f"from vendas " \
                                  f"inner join clientes on vendas.cpf = clientes.cpf " \
                                  f"inner join produtos on vendas.id_produto = produtos.id " \
                                  f"inner join detalhes_venda on vendas.id = detalhes_venda.id " \
                                  f"where vendas.pagamento = '0'; "
                busca.execute(selectRelatorio)
                pendencias = busca.fetchall()
                for p in pendencias:
                    print(p)
                separador()
            elif escolhaRelatorio == 0:
                break
