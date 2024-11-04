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

# instânciando os objetos
roupa1 = Roupa("123", "Camisa", 125.25, "Camisa Mamonas Assassinas", "Preta", "GG", "Algodão") # instânciando o objeto roupa1 com os parâmetros "123", "Camisa", 125.25, "Camisa Mamonas Assassinas", "Preta", "GG", "Algodão"
roupa2 = Roupa("124", "Saia", 100.00, "Saia Festa Junina", "Rosa", "M", "Algodão") # instânciando o objeto roupa2 com os parâmetros "124", "Saia", 100.00, "Saia Festa Junina", "Rosa", "M", "Algodão"
calcado1 = Calcado("133", "Sapato", 150.25, "Sapato de Couro", "Preto", "40", "Borracha", "Couro", "Algodão") # instânciando o objeto calcado1 com os parâmetros "133", "Sapato", 150.25, "Sapato de Couro", "Preto", "40", "Borracha", "Couro", "Algodão"
calcado2 = Calcado("134", "Tênis", 133.63, "Tênis Fake Nike", "Branco", "41", "Borracha", "Couro", "Algodão") # instânciando o objeto calcado2 com os parâmetros "134", "Tênis", 133.63, "Tênis Fake Nike", "Branco", "41", "Borracha", "Couro", "Algodão"
eletronico1 = Eletronico("143", "Notebook", 1125.55, "220V") # instânciando o objeto eletronico1 com os parâmetros "143", "Notebook", 1125.55, "220V"
eletronico2 = Eletronico("144", "Rádio", 60.55, "110V") # instânciando o objeto eletronico2 com os parâmetros "144", "Rádio", 60.55, "110V"
chapeu1 = Chapeu("153", "Boné", 204.31, "Boné Lacoste", "Roxo", "G", "Aba Reta") # instânciando o objeto chapeu1 com os parâmetros "153", "Boné", 204.31, "Boné Lacoste", "Roxo", "G", "Aba Reta"
chapeu2 = Chapeu("154", "Chapéu", 304.31, "Chapéu Cowboy", "Preto", "G", "Aba Larga") # instânciando o objeto chapeu2 com os parâmetros "154", "Chapéu", 304.31, "Chapéu Cowboy", "Preto", "G", "Aba Larga"

# chamando os métodos imprimir dos objetos
roupa1.imprimir() # chamando os métodos imprimir do objeto roupa1
roupa2.imprimir() # chamando os métodos imprimir do objeto roupa2
calcado1.imprimir() # chamando os métodos imprimir do objeto calcado1
calcado2.imprimir() # chamando os métodos imprimir do objeto calcado2
eletronico1.imprimir() # chamando os métodos imprimir do objeto eletronico1
eletronico2.imprimir() # chamando os métodos imprimir do objeto eletronico2
chapeu1.imprimir() # chamando os métodos imprimir do objeto chapeu1
chapeu2.imprimir() # chamando os métodos imprimir do objeto chapeu2


listaDeObjetos = (roupa1, roupa2, calcado1, calcado2, eletronico1, eletronico2, chapeu1, chapeu2) # tupla dos objetos (produtos) da loja
listaDeCompra = [] # lista de compras do cliente
executando = True # variável de código em execução

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
  carrinhoDeCompraRetirar = int(input("Digite a posição do produto na sua lista para retirar:")) # imprime no console "Digite a posição do produto na sua lista para retirar:" e requisita a posição do produto que ele deseja retirar
# Ainda necessário aplicar uma condicional para caso a posição seja inválida
  print("Produto retirado:") # mensagem de produto retirado
  print(listaDeCompra[carrinhoDeCompraRetirar - 1].imprimir()) # imprime no console o produto a ser retirado do carrinho de compras
  listaDeCompra.pop(carrinhoDeCompraRetirar - 1) # retira o produto do carrinho de compras

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

while executando:
  requisicao = input("Digite 'a' para adicionar um produto \nDigite 'r' para remover um produto \nDigite 'f' para finalizar a compra \nDigite 'v' para verificar o carrinho \nDigite 's' para sair \n")
  if requisicao == "a":
    AdicionarAoCarrinho()
  elif requisicao == "r":
    RetirarDoCarrinho()
  elif requisicao == "f":
    FinalizarCompra()
  elif requisicao == "v":
    CarrinhoAgora()
  elif requisicao == "s":
    executando = False
  else:
    print("Comando inválido.\n")
