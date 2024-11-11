from . import autentif
from . import imprimirfunc as imp
from . import funcs_user as func
from . import funcs_adm as afunc

def Execucao(): # função de execução do usuário comprador
  executando = True # variável de código em execução
  while executando: # enquanto for true a variável executando esse loop será executado
    requisicao = input("Digite 'a' para adicionar um produto \nDigite 'r' para remover um produto \nDigite 'f' para finalizar a compra \nDigite 'v' para verificar o carrinho \nDigite 'p' ver os produtos da loja \nDigite 's' para sair \n")
    if requisicao.lower() == "a": # transforma o valor da variável requisicao em minusculo e compara com a string "a"
      func.AdicionarAoCarrinho() # executa a função AdicionarAoCarrinho
    elif requisicao.lower() == "r": # transforma o valor da variável requisicao em minusculo e compara com a string "r"
      func.RetirarDoCarrinho() # executa a função RetirarDoCarrinho
    elif requisicao.lower() == "f": # transforma o valor da variável requisicao em minusculo e compara com a string "f"
      func.FinalizarCompra() # executa a função FinalizarCompra
    elif requisicao.lower() == "v": # transforma o valor da variável requisicao em minusculo e compara com a string "v"
      func.CarrinhoAgora() # executa a função CarrinhoAgora
    elif requisicao.lower() == "p": # transforma o valor da variável requisicao em minusculo e compara com a string "p"
      imp.ImprimirTodosProdutos() # executa a função ImprimirTodosProdutos
    elif requisicao.lower() == "s": # transforma o valor da variável requisicao em minusculo e compara com a string "s"
      executando = False # atribui false para a variável executando
      autentificado = False # atribui false para a variável autentificado
      autentif.Autentificado() # executa a função Autentificado
    else: # se não for atendido as condições executa a linha abaixo
      print("Comando inválido.\n") # imprime no console "Comando inválido."

def ExecucaoAdmin(): # função de execução do administrador
  executandoAdmin = True # atribui o valor true para a variável
  while executandoAdmin: # enquanto for true a variável executandoAdmin esse loop será executado
    requisicaoAdmin = input("Para adicionar ou remover Produto digite 'p'\nPara adicionar ou remover usuario digite 'u'\nDigite 's' para sair\n") # pede para o usuário escolher "p" para ir pra as funções de produto, "u" para as funções usuários e "s" para sair.
    if requisicaoAdmin.lower() == "u": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "u"
      requisicaoAdmin = input("Para adicionar usuário digite 'a'\nPara remover usuário digite 'r'\nPara modificar a senha do Administrador digite 'ms'\nPara imprimir os usuários digite 'i'\n") # pede ao usuário para escolher "a" para adicionar um usuário, "r" para remover um usuário, "ms" para mudar a senha
      if requisicaoAdmin.lower() == "a": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "a"
        afunc.AdicionarUsuario() # executa a função AdicionarUsuario
      elif requisicaoAdmin.lower() == "r": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "r"
        afunc.RemoverUsuario() # executa a função RemoverUsuario
      elif requisicaoAdmin.lower() == "ms": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "rs"
        afunc.TrocarSenhaAdm() # exucuta a função TrocarSenhaAdm
      elif requisicaoAdmin.lower() == "i": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "i"
        imp.ImprimirTodosUsuarios() # executa a função ImprimirTodosUsuarios
      else: # se não for atendido as condições executa a linha abaixo
        print("Comando inválido.\n") # imprime no console "Comando inválido."
    elif requisicaoAdmin.lower() == "p": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "p"
      requisicaoAdmin = input("Digite 'a' para adicionar.\nDigite 'r' para remover.\nDigite 'i' para imprimir todos os produtos.\n") # pede ao usuário escolher "a" para adicionar um produto, "r" para remover um produto e "i" para imprimir todos os produtos cadastrados
      if requisicaoAdmin.lower() == "a": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "a"
        requisicaoAdmin = input("Escolha o tipo de produto.\nDigite 'e' para Eletrônicos.\nDigite 'ca' para calçados.\nDigite 'ch' para chapéus.\nDigite 'r' para roupas.\n") # Pede ao usuário escolher o tipo de produto a ser adicionado "e" eletrônico, "ca" para calçados, "ch" para chapéu, "r" para roupas
        if requisicaoAdmin.lower() == "e": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "e"
          afunc.AdicionarEletronico() # exucuta a função AdicionarEletronico
        elif requisicaoAdmin.lower() == "ca": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "ca"
          afunc.AdicionarCalcado() # exucuta a função AdicionarCalcado
        elif requisicaoAdmin.lower() == "ch": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "ch"
          afunc.AdicionarChapeu() # exucuta a função AdicionarChapeu
        elif requisicaoAdmin.lower() == "r": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "r"
          afunc.AdicionarRoupa() # exucuta a função AdicionarRoupa
        else: # se não for atendido as condições executa a linha abaixo
          print("Comando inválido.\n") # imprime no console "Comando inválido."
      elif requisicaoAdmin.lower() == "r": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "r"
        afunc.RemoverProduto() # executa a função RemoverProduto
      elif requisicaoAdmin.lower() == "i": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "i"
        imp.ImprimirTodosProdutos() # executa a função ImprimirTodosProdutos
      else: # se não for atendido as condições executa a linha abaixo
        print("Comando inválido.\n") # imprime no console "Comando inválido."
    elif requisicaoAdmin.lower() == "s": # transforma o valor da variável requisicaoAdmin em minusculo e compara com a string "s"
      executandoAdmin = False # atribui false para a variável executandoAdmin
      autentif.Autentificado() # executa a função Autentificado
    else: # se não for atendido as condições executa a linha abaixo
        print("Comando inválido.\n") # imprime no console "Comando inválido."