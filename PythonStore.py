class Usuario: # criação da classe Usuario
  def __init__(self, n, l, s): # construtor da classe Usuario e o uso dos parâmetros n para o nome, l para o login e s para a senha
    self.nome = n # atribuição do valor do parâmetro n para o atributo nome
    self.login = l # atribuição do valor do parâmetro l para o atributo login
    self.senha = s # atribuição do valor do parâmetro s para o atributo senha
  def imprimir(self): # método para imprimir informações do usuário
    print("Nome: ", self.nome) # imprime o valor do nome do usuário
    print("Login: ", self.login) # imprime o valor do login do usuário
    print("Senha: ", self.senha, "\n") # imprime o valor da senha do usuário

class Produto: # criação da classe Produto
  def __init__(self, c, d, v): # construtor da classe Produto e uso dos parâmetros c para o codigo, d para a descrição e v para valor
    self.codigo = c # atribuição do valor do parâmetro c para o atributo codigo
    self.descricao = d # atribuição do valor do parâmetro d para o atributo descricao
    self.valor = v # atribuição do valor do parâmetro v para o atributo valor
  def imprimir(self): # criação do método imprimir da classe Produto
    print("Código: ", self.codigo) # impressão do valor do atributo codigo
    print("Descrição: ", self.descricao) # impressão do valor do atributo descricao
    print("Valor: ", self.valor) # impressão do valor do atributo valor

class Eletronico(Produto): # criação da classe Eletronico que herda atributos e métodos da superclasse Produto
  def __init__(self, c, d, v, t): # construtor da classe Eletronico e uso dos parâmetros c, d e v para os atributos herdados da classe pai Produto e t para o atributo tensao
    self.tensao = t # atribuição do valor do parâmetro t para o atributo tensao
    super().__init__(c, d, v) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Produto
  def imprimir(self): # criação do método imprimir da classe Eletronico
    super().imprimir() # chamando o método da classe pai Produto imprimir()
    print("Tensão: ", self.tensao, "\n") # impressão do valor do atributo tensao

class Vestuario(Produto): # criação da classe Vestuario que herda atributos e métodos da superclasse Produto
  def __init__(self, c, d, v, n, co, ta): # construtor da classe Vestuario e uso dos parâmetros c, d e v para os atributos herdados da classe pai Produto e n, co e ta para os atributos nome, cor e tamanho
    self.nome = n # atribuição do parâmetro n para o atributo nome
    self.cor = co # atribuição do parâmetro co para o atributo cor
    self.tamanho = ta # atribuição do parâmetro ta para o atributo tamanho
    super().__init__(c, d, v) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Produto
  def imprimir(self): # criação do método imprimir da classe Vestuario
    super().imprimir() # chamando o método da classe pai Produto imprimir()
    print("Nome: ", self.nome)  # impressão do valor do atributo nome
    print("Cor: ", self.cor)  # impressão do valor do atributo cor
    print("Tamanho: ", self.tamanho)  # impressão do valor do atributo tamanho

class Calcado(Vestuario): # criação da classe Calcado que herda atributos e métodos da classe pai Vestuario
  def __init__(self, c, d, v, n, co, ta, ms, mps, mi): # construtor da classe Calcado e o uso dos parâmetros c, d, v, n, co e ta para os atributos herdados da classe pai Vestuario e ms, mps e mi para os atributos materialSola, materialParteSuperior e materialInterno
    self.materialSola = ms # atribuição do parâmetro ms para o atributo materialSola
    self.materialParteSuperior = mps # atribuição do parâmetro mps para o atributo materialParteSuperior
    self.materialInterno = mi # atribuição do parâmetro mi para o atributo materialInterno
    super().__init__(c, d, v, n, co, ta) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Vestuario
  def imprimir(self): # criação do método imprimir da classe Calcado
    super().imprimir() # chamando o método da classe pai Vestuario imprimir()
    print("Material da sola: ", self.materialSola) # impressão do valor do atributo materialSola
    print("Material da Parte Superior:", self.materialParteSuperior) # impressão do valor do atributo materialParteSuperior
    print("Material Interno: ", self.materialInterno, "\n") # impressão do valor do atributo materialInterno

class Roupa(Vestuario): # criação da classe Roupa que herda atributos e métodos da classe pai Vestuario
  def __init__(self, c, d, v, n, co, ta, te): # método construtor da classe Roupa e o uso dos parâmetros c, d, v, n, co e ta para os atributos herdados da classe pai Vestuario e te para o atributo tecido
    self.tecido = te # atribuição do parâmetro te para o atributo tecido
    super().__init__(c, d, v, n, co, ta) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Vestuario
  def imprimir(self): # criação do método imprimir da classe Roupa
    super().imprimir() # chamando o método da classe pai Vestuario imprimir()
    print("Tecido: ", self.tecido, "\n") # impressão do valor do atributo tecido

class Chapeu(Vestuario): # criação da classe Chapeu que herda atributos e métodos da classe pai Vestuario
  def __init__(self, c, d, v, n, co, ta, ti): # método construtor da classe Roupa e o uso dos parâmetros c, d, v, n, co e ta para os atributos herdados da classe pai Vestuario e ti para o atributo tipo
    self.tipo = ti # atribuição do parâmetro ti para o atributo tipo
    super().__init__(c, d, v, n, co, ta) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Vestuario
  def imprimir(self):# criação do método imprimir da classe Chapeu
    super().imprimir() # chamando o método da classe pai Vestuario imprimir()
    print("Tipo: ", self.tipo, "\n")  # impressão do valor do atributo tipo

# instânciando os objetos dos usuários
usuario1 = Usuario("Fulano da Silva", "Fulano123", "FuSilva123%") # instânciando o objeto usuario1 com o nome Fulano da Silva, o login Fulano123 e a senha FuSilva123%
usuario2 = Usuario("Ciclano dos Santos", "Ciclanosantos", "Cici123@") # instânciando o objeto usuario2 com o nome Ciclano dos Santos, o login Ciclanosantos e a senha Cici123@
usuario3 = Usuario("Joca Silva", "JocaBr", "JocaS234$") # instânciando o objeto usuario3 com o nome Joca Silva, o login JocaBr e a senha JocaS234$
usuarioAdmin = Usuario("Administrador", "Admin", "Admin") # instânciando o objeto usuarioAdmin com o nome Administrador, login Admin e a senha Admin

def ImprimirTodosProdutos(): # função para impressão dos produtos cadastrados
    if not listaDeObjetos:  # condicional para verificar se a lista de objetos dos produtos está vazia
        print("Não há produtos cadastrados.\n") # se a lista estiver vazia imprime "Não há produtos cadastrados."
        return # retorna vazio a função
    print("Lista de Produtos:\n") # se houver produtos na lista imprime "Lista de Produtos:"
    for produto in listaDeObjetos:  # loop da lista de objetos dos produtos para passar por todos os objetos cadastrados
        produto.imprimir() # imprime o produto cadastrado da vez em que o loop for estiver chamando

def ImprimirTodosUsuarios(): # função para imprimir todos os usuários
    if not listaDeUsuarios:  # condicional para verificar se a lista de objetos de usuários está vazia
        print("Não há produtos cadastrados.\n") # se a lista estiver vazia imprime "Não há produtos cadastrados"
        return # retorna vazio a função
    print("Lista de Usuários:\n") # se houver usuários na lista imprime "Lista de Usuários:"
    for usuario in listaDeUsuarios:  # loop para verificar a lista completa dos objetos da lista de usuários
        usuario.imprimir() # imprime o usuário cadastrado da vez

def AdicionarAoCarrinho(): # função para adicionar um produto ao carrinho de compras do cliente
  carrinhoDeCompraAdicionar = input("Coloque o código do produto:") # imprime no console "Coloque o código do produto:" e requisita o código do produto
  for lista in listaDeObjetos: # loop para verificar se o código do produto existe entres os objetos e adiciona se o produto existir
    if lista.codigo == carrinhoDeCompraAdicionar: # condicional para vericar o código entre os objetos
      listaDeCompra.append(lista) # adiciona o produto à lista de compra do cliente
      return # retorna para o main
  print("Produto inválido.\n") # caso o código do produto não está registrado entre os objetos enviará ao console "Produto inválido."

def RetirarDoCarrinho(): # função para retirar um produto do carrinho de compras do cliente
  if not listaDeCompra: # verifica se a variável listaDeCompra está vazia
    print("O carrinho está vazio\n") # se estiver vázia irá imprimir no console "O carrinho está vazio"
    return # retorna para o main
  for i, lista in enumerate(listaDeCompra): # loop para passar por toda lista de compra e enumerar as posições dos produtos
    print("Posição: ", i+1) # imprime a posição do produto
    lista.imprimir() # imprime as informações do produto
  carrinhoDeCompraRetirar = int(input("Digite a posição do produto na sua lista para retirar:\n")) # imprime no console "Digite a posição do produto na sua lista para retirar:" e requisita a posição do produto que ele deseja retirar
  if 1 <= carrinhoDeCompraRetirar <= len(listaDeCompra):
    print("Produto retirado:\n") # mensagem de produto retirado
    print(listaDeCompra[carrinhoDeCompraRetirar - 1].imprimir()) # imprime no console o produto a ser retirado do carrinho de compras
    listaDeCompra.pop(carrinhoDeCompraRetirar - 1) # retira o produto do carrinho de compras
    return # retorna vazio a função
  else: # caso a condicional não for atendida segue para a linha abaixo
    print("Posição inválida.\n") # imprime "Posição inválida" se não houver atendido a condicional if
    return # retorna vazio a função

def CarrinhoAgora(): # função para verificar o estado do carrinho
  if not listaDeCompra: # verifica se a variável listaDeCompra está vazia
    print("O carrinho está vazio\n")  # se estiver vázia irá imprimir no console "O carrinho está vazio"
    return # retorna para o main
  for lista in listaDeCompra: # loop para imprimir todos os produtos dentro do carrinho de compras
    lista.imprimir() # impressão do produto do estado atual do loop
  valorFinal = 0 # atribui o valor 0 para a variável listaFinal para o calculo do valor parcial do carrinho
  for lista in listaDeCompra: # loop para calcular o valor parcial do carrinho
    valorFinal += lista.valor # soma o valor do produto ao resultado da variável valorFinal
  print("O valor do carrinho é: R$", valorFinal) # imprime no console "O valor do carrinho é: R$" mais o valor da variável valorFinal

def FinalizarCompra(): # função para finalizar a compra
  if not listaDeCompra: # verifica se a variável listaDeCompra está vazia
    print("O carrinho está vazio\n")  # se estiver vázia irá imprimir no console "O carrinho está vazio"
    return # retorna para o main
  for lista in listaDeCompra: # loop para imprimir todos os produtos dentro do carrinho de compras
    lista.imprimir() # impressão do produto do estado atual do loop
  valorFinal = 0 # atribui o valor 0 para a variável listaFinal para o calculo do valor final do carrinho
  for lista in listaDeCompra: # loop para calcular o valor final do carrinho
    valorFinal += lista.valor # soma o valor do produto ao resultado da variável valorFinal
  print("O valor da compra é: R$",valorFinal) # Imprime no console "O valor da compra é: R$" mais o valor total da compra
  print("Realizar Pagamento. \n") # imprime no console "Realizar Pagamento."
  listaDeCompra.clear() # limpa a lista de compras

def AutenticarUsuario(): # função para autentificar o usuário
    login1 = input("Digite o login: ") # pede para o usuário digitar o login
    senha1 = input("Digite a senha: ") # pede para o usuário digitar a senha
    for usuario in listaDeUsuarios: # loop para verificar todos os objetos da lista de usuários
      if usuarioAdmin.login == login1 and usuarioAdmin.senha == senha1: # se o usuário e a senha forem iguais as do administrador
          ExecucaoAdmin() # executa a função de execução do administrador
      elif usuario.login == login1 and usuario.senha == senha1: # senão se o login e a senha pertencer a um usuário
        print("Bem-vindo(a) ", usuario.nome) # imprime "Bem-vindo(a) " concatenado com o valor do nome do usuário
        return True # retorna true a função
    print("Login ou senha incorretos.\n") # caso não atenda aos requisitos anteriores imprime "Login ou senha incorretos."
    return False # retorna false a função

def AdicionarUsuario(): # função para adicionar usuário
    nome = input("Digite o nome do usuário: ") # pede para digitar o nome do usuário que irá ser adicionado
    login = input("Digite o login do usuário: ") # pede para digitar o login do usuário que irá ser adicionado
    for usuario in listaDeUsuarios: # loop para verificar toda a lista de usuários
      if usuario.login == login: # se houver registro de login que já existe
        print("Este login já está sendo utilizado.") # imprime "Este login já está sendo utilizado."
        return # retorna vazio a função
    senha = input("Digite a senha do usuário: ") # pede para digitar a senha do novo usuário
    novoUsuario = Usuario(nome, login, senha) # intância o objeto novo_usuário
    listaDeUsuarios.append(novoUsuario) # adiciona o objeto novo_usuario na lista de usuários
    print("Usuário adicionado com sucesso.\n") # imprime no console "Usuário adicionado com sucesso."

def RemoverUsuario(): # função para remover usuário
    login = input("Digite o login do usuário que deseja remover: ") # pede ao usuário para digitar o login do usuário a ser removido
    for usuario in listaDeUsuarios: # loop para verificar toda a lista de usuários
        if usuario.login == login and usuario.login != "Admin": # condicional para remover o usuário digitado se for igual a da lista e diferente do login do administrado segue em diante
            listaDeUsuarios.remove(usuario) # remove o usuário (objeto) que atendeu as condições
            print("Usuário removido com sucesso.\n") # imprime "Usuário removido com sucesso."
            return # retorna vazio a função
    print("Usuário não encontrado.\n") # imprime "Usuário não encontrado."

def TrocarSenhaAdm(): # função para trocar senha do Administrador
    nova_senha = input("Digite a nova senha do administrador: ") # pede ao administrador digitar a nova senha 
    for usuario in listaDeUsuarios: # loop para verificar a lista de usuários
        if usuario.login == "Admin": # condicional para verificar se a conta a ser trocada a senha é do administrador
            usuario.senha = nova_senha # troca a senha do administrador
            print("Senha do administrador alterada com sucesso.\n") # imprime "Senha do administrador alterada com sucesso."
            return # retorna vazio a função

def AdicionarEletronico(): # função para adicionar um novo produto eletrônico
    codigo = input("Digite o código do produto: ") # pede para o usuário digitar o código do novo produto eletrônico
    for produto in listaDeObjetos: # loop para verificar a lista de objetos (produtos)
      if produto.codigo == codigo: # condicional para verificar se o codigo digitado existe no sistema
        print("Este código já está sendo utilizado.") # caso o código existe no sistema imprime "Este código já está sendo utilizado."
        return # retorna vazio a função
    descricao = input("Digite a descrição do produto: ") # pede ao usuário digitar a descrição do produto eletrônico
    valor = float(input("Digite o valor do produto: ")) # pede ao usuário digitar o valor do produto eletrônico
    tensao = input("Digite a tensão do produto: ") # pede ao usuário digitar a tensão do produto eletrônico
    novoEletronico = Eletronico(codigo, descricao, valor, tensao)  # instância o objeto novoEletronico
    listaDeObjetos.append(novoEletronico) # adiciona o objeto novoEletronico na lista de produtos
    print("Produto eletrônico adicionado com sucesso.\n") # imprime no console "Produto eletrônico adicionado com sucesso."

def AdicionarCalcado(): # função para adicionar um novo calçado
    codigo = input("Digite o código do produto: ") # pede para o usuário digitar o código do novo produto calçado
    for produto in listaDeObjetos: # loop para verificar a lista de objetos (produtos)
      if produto.codigo == codigo: # condicional para verificar se o codigo digitado existe no sistema
        print("Este código já está sendo utilizado.") # caso o código existe no sistema imprime "Este código já está sendo utilizado."
        return # retorna vazio a função
    descricao = input("Digite a descrição do produto: ") # pede ao usuário digitar a descrição do produto calçado
    valor = float(input("Digite o valor do produto: ")) # pede ao usuário digitar o valor do produto calçado
    nome = input("Digite o nome do produto: ") # pede ao usuário digitar o nome do produto calçado
    cor = input("Digite a cor do produto: ") # pede ao usuário digitar a cor do produto calçado
    tamanho = input("Digite o tamanho do produto: ") # pede ao usuário digitar o tamanho do produto calçado
    materialSola = input("Digite o material da sola: ") # pede ao usuário digitar o material da sola do produto calçado
    materialParteSuperior = input("Digite o material da parte superior: ") # pede ao usuário digitar o material da parte superior do produto calçado
    materialInterno = input("Digite o material interno: ") # pede ao usuário digitar o material interno do produto calçado
    novoCalcado = Calcado(codigo, descricao, valor, nome, cor, tamanho, materialSola, materialParteSuperior, materialInterno) # intancia o objeto novoCalcado
    listaDeObjetos.append(novoCalcado) # adiciona o objeto novoCalcado na lista de objetos (produto)
    print("Calçado adicionado com sucesso.\n") # imprime no console "Calçado adicionado com sucesso."

def AdicionarChapeu(): # função para adicionar um novo chapéu
    codigo = input("Digite o código do produto: ") # pede para o usuário digitar o código do novo produto chapéu
    for produto in listaDeObjetos: # loop para verificar a lista de objetos (produtos)
      if produto.codigo == codigo: # condicional para verificar se o codigo digitado existe no sistema
        print("Este código já está sendo utilizado.") # caso o código existe no sistema imprime "Este código já está sendo utilizado."
        return # retorna vazio a função
    descricao = input("Digite a descrição do produto: ") # pede ao usuário digitar a descrição do produto chapéu
    valor = float(input("Digite o valor do produto: ")) # pede ao usuário digitar o valor do produto chapéu
    nome = input("Digite o nome do produto: ") # pede ao usuário digitar o nome do produto chapéu
    cor = input("Digite a cor do produto: ") # pede ao usuário digitar a cor do produto chapéu
    tamanho = input("Digite o tamanho do produto: ") # pede ao usuário digitar o tamanho do produto chapéu
    tipo = input("Digite o tipo do chapéu: ") # pede ao usuário digitar o tipo do chapéu
    novoChapeu = Chapeu(codigo, descricao, valor, nome, cor, tamanho, tipo) # instância o objeto novoChapeu
    listaDeObjetos.append(novoChapeu) # adiciona o objeto novoChapeu na lista de produtos
    print("Chapéu adicionado com sucesso.\n") # imprime no console "Chapéu adicionado com sucesso."

def AdicionarRoupa(): # função para adicionar uma nova roupa
    codigo = input("Digite o código do produto: ") # pede para o usuário digitar o código do novo produto chapéu
    for produto in listaDeObjetos: # loop para verificar a lista de objetos (produtos)
      if produto.codigo == codigo: # condicional para verificar se o codigo digitado existe no sistema
        print("Este código já está sendo utilizado.") # caso o código existe no sistema imprime "Este código já está sendo utilizado."
        return # retorna vazio a função
    descricao = input("Digite a descrição do produto: ") # pede ao usuário digitar a descrição do novo produto roupa
    valor = float(input("Digite o valor do produto: ")) # pede ao usuário digitar o valor do produto roupa
    nome = input("Digite o nome do produto: ") # pede ao usuário digitar o nome do novo produto roupa
    cor = input("Digite a cor do produto: ") # pede ao usuário digitar a cor do novo produto roupa
    tamanho = input("Digite o tamanho do produto: ") # pede ao usuário digitar o tamanho do novo produto roupa
    tecido = input("Digite o tipo de tecido: ") # pede ao usuário digitar o tecido do novo produto roupa
    novaRoupa = Roupa(codigo, descricao, valor, nome, cor, tamanho, tecido) # instância o objeto novaRoupa
    listaDeObjetos.append(novaRoupa) # adiciona o objeto novaRoupa na lista de produtos
    print("Roupa adicionada com sucesso.\n") # imprime no console "Roupa adicionada com sucesso."

def RemoverProduto(): # função para remover um produto da lista de produtos
    codigo = input("Digite o código do produto que deseja remover: ") # pede ao usuário digitar o código do produto que será retirado
    for produto in listaDeObjetos: # loop para verificar a lista de objetos (lista de produtos)
        if produto.codigo == codigo: # condicional para verificar se o objeto contém o mesmo código
            listaDeObjetos.remove(produto) # se for o mesmo código removerá o produto da lista
            print("Produto removido com sucesso.\n") # imprime no console "Produto removido com sucesso."
            return # retorna vazio a função
    print("Produto não encontrado.\n") # imprime "Produto não encontrado." caso não tenha encontrado o código na lista

def ExecucaoAdmin(): # função de execução do administrador
  executandoAdmin = True # atribui o valor true para a variável
  while executandoAdmin: # enquanto for true a variável executandoAdmin esse loop será executado
    requisicaoAdmin = input("Para adicionar ou remover Produto digite 'p'\nPara adicionar ou remover usuario digite 'u'\nDigite 's' para sair\n") # pede para o usuário escolher "p" para ir pra as funções de produto, "u" para as funções usuários e "s" para sair.
    if requisicaoAdmin.lower() == "u": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "u"
      requisicaoAdmin = input("Para adicionar usuário digite 'a'\nPara remover usuário digite 'r'\nPara modificar a senha do Administrador digite 'ms'\nPara imprimir os usuários digite 'i'\n") # pede ao usuário para escolher "a" para adicionar um usuário, "r" para remover um usuário, "ms" para mudar a senha
      if requisicaoAdmin.lower() == "a": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "a"
        AdicionarUsuario() # executa a função AdicionarUsuario
      elif requisicaoAdmin.lower() == "r": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "r"
        RemoverUsuario() # executa a função RemoverUsuario
      elif requisicaoAdmin.lower() == "ms": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "rs"
        TrocarSenhaAdm() # exucuta a função TrocarSenhaAdm
      elif requisicaoAdmin.lower() == "i": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "i"
        ImprimirTodosUsuarios() # executa a função ImprimirTodosUsuarios
      else: # se não for atendido as condições executa a linha abaixo
        print("Comando inválido.\n") # imprime no console "Comando inválido."
    elif requisicaoAdmin.lower() == "p": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "p"
      requisicaoAdmin = input("Digite 'a' para adicionar.\nDigite 'r' para remover.\nDigite 'i' para imprimir todos os produtos.\n") # pede ao usuário escolher "a" para adicionar um produto, "r" para remover um produto e "i" para imprimir todos os produtos cadastrados
      if requisicaoAdmin.lower() == "a": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "a"
        requisicaoAdmin = input("Escolha o tipo de produto.\nDigite 'e' para Eletrônicos.\nDigite 'ca' para calçados.\nDigite 'ch' para chapéus.\nDigite 'r' para roupas.\n") # Pede ao usuário escolher o tipo de produto a ser adicionado "e" eletrônico, "ca" para calçados, "ch" para chapéu, "r" para roupas
        if requisicaoAdmin.lower() == "e": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "e"
          AdicionarEletronico() # exucuta a função AdicionarEletronico
        elif requisicaoAdmin.lower() == "ca": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "ca"
          AdicionarCalcado() # exucuta a função AdicionarCalcado
        elif requisicaoAdmin.lower() == "ch": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "ch"
          AdicionarChapeu() # exucuta a função AdicionarChapeu
        elif requisicaoAdmin.lower() == "r": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "r"
          AdicionarRoupa() # exucuta a função AdicionarRoupa
        else: # se não for atendido as condições executa a linha abaixo
          print("Comando inválido.\n") # imprime no console "Comando inválido."
      elif requisicaoAdmin.lower() == "r": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "r"
        RemoverProduto() # executa a função RemoverProduto
      elif requisicaoAdmin.lower() == "i": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "i"
        ImprimirTodosProdutos() # executa a função ImprimirTodosProdutos
      else: # se não for atendido as condições executa a linha abaixo
        print("Comando inválido.\n") # imprime no console "Comando inválido."
    elif requisicaoAdmin.lower() == "s": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "s"
      executandoAdmin = False # atribui false para a variável executandoAdmin
      Autentificado() # executa a função Autentificado
    else: # se não for atendido as condições executa a linha abaixo
        print("Comando inválido.\n") # imprime no console "Comando inválido."

def Autentificado(): # função para autentificar o usuário
  primeiraAut = True # atribui true para a variável primeiraAut
  while primeiraAut: # enquanto for true a variável primeiraAut esse loop será executado
    primRequisicao = input("Digite 'l' para logar ou 'c' para cadastrar uma nova conta") # pede para o usuário escolher "l" para logar e "c" para cadastrar uma nova conta
    if primRequisicao.lower() == "c": # transforma o valor da variável primRequisicao em minusculo e compara com a string "c"
      AdicionarUsuario() # executa a função AdicionarUsuario
    elif primRequisicao.lower() == "l": # transforma o valor da variável primRequisicao em minusculo e compara com a string "l"
      global autentificado # cria a variável global autentificado
      autentificado = False # atribui o valor false para autentificado
      while not autentificado: # enquanto for false a variável autentificado esse loop será executado
        autentificado = AutenticarUsuario() # atribui o valor retornado da função AutenticarUsuario
      Execucao() # executa a função Execucao
    else: # se não for atendido as condições executa a linha abaixo
      print("Comando inválido.\n") # imprime no console "Comando inválido."

def Execucao(): # função de execução do usuário comprador
  executando = True # variável de código em execução
  while executando: # enquanto for true a variável executando esse loop será executado
    requisicao = input("Digite 'a' para adicionar um produto \nDigite 'r' para remover um produto \nDigite 'f' para finalizar a compra \nDigite 'v' para verificar o carrinho \nDigite 'p' ver os produtos da loja \nDigite 's' para sair \n")
    if requisicao.lower() == "a": # transforma o valor da variável requisicao em minusculo e compara com a string "a"
      AdicionarAoCarrinho() # executa a função AdicionarAoCarrinho
    elif requisicao.lower() == "r": # transforma o valor da variável requisicao em minusculo e compara com a string "r"
      RetirarDoCarrinho() # executa a função RetirarDoCarrinho
    elif requisicao.lower() == "f": # transforma o valor da variável requisicao em minusculo e compara com a string "f"
      FinalizarCompra() # executa a função FinalizarCompra
    elif requisicao.lower() == "v": # transforma o valor da variável requisicao em minusculo e compara com a string "v"
      CarrinhoAgora() # executa a função CarrinhoAgora
    elif requisicao.lower() == "p": # transforma o valor da variável requisicao em minusculo e compara com a string "p"
      ImprimirTodosProdutos() # executa a função ImprimirTodosProdutos
    elif requisicao.lower() == "s": # transforma o valor da variável requisicao em minusculo e compara com a string "s"
      executando = False # atribui false para a variável executando
      autentificado = False # atribui false para a variável autentificado
      Autentificado() # executa a função Autentificado
    else: # se não for atendido as condições executa a linha abaixo
      print("Comando inválido.\n") # imprime no console "Comando inválido."

# instânciando os objetos de produtos
roupa1 = Roupa("123", "Camisa", 125.25, "Camisa Mamonas Assassinas", "Preta", "GG", "Algodão") # instânciando o objeto roupa1 com os parâmetros "123", "Camisa", 125.25, "Camisa Mamonas Assassinas", "Preta", "GG", "Algodão"
roupa2 = Roupa("124", "Saia", 100.00, "Saia Festa Junina", "Rosa", "M", "Algodão") # instânciando o objeto roupa2 com os parâmetros "124", "Saia", 100.00, "Saia Festa Junina", "Rosa", "M", "Algodão"
calcado1 = Calcado("133", "Sapato", 150.25, "Sapato de Couro", "Preto", "40", "Borracha", "Couro", "Algodão") # instânciando o objeto calcado1 com os parâmetros "133", "Sapato", 150.25, "Sapato de Couro", "Preto", "40", "Borracha", "Couro", "Algodão"
calcado2 = Calcado("134", "Tênis", 133.63, "Tênis Fake Nike", "Branco", "41", "Borracha", "Couro", "Algodão") # instânciando o objeto calcado2 com os parâmetros "134", "Tênis", 133.63, "Tênis Fake Nike", "Branco", "41", "Borracha", "Couro", "Algodão"
eletronico1 = Eletronico("143", "Notebook", 1125.55, "220V") # instânciando o objeto eletronico1 com os parâmetros "143", "Notebook", 1125.55, "220V"
eletronico2 = Eletronico("144", "Rádio", 60.55, "110V") # instânciando o objeto eletronico2 com os parâmetros "144", "Rádio", 60.55, "110V"
chapeu1 = Chapeu("153", "Boné", 204.31, "Boné Lacoste", "Roxo", "G", "Aba Reta") # instânciando o objeto chapeu1 com os parâmetros "153", "Boné", 204.31, "Boné Lacoste", "Roxo", "G", "Aba Reta"
chapeu2 = Chapeu("154", "Chapéu", 304.31, "Chapéu Cowboy", "Preto", "G", "Aba Larga") # instânciando o objeto chapeu2 com os parâmetros "154", "Chapéu", 304.31, "Chapéu Cowboy", "Preto", "G", "Aba Larga"

# listas de objetos
listaDeObjetos = [roupa1, roupa2, calcado1, calcado2, eletronico1, eletronico2, chapeu1, chapeu2] # tupla dos objetos (produtos) da loja
listaDeCompra = [] # lista de compras do cliente
listaDeUsuarios = [usuario1, usuario2, usuario3, usuarioAdmin] # lista de usuários do sistema

ImprimirTodosProdutos() # executa a função ImprimirTodosProdutos
Autentificado() # executa a função Autentificado
