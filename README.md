# PythonStore

<p -width="100%" align="center">
    <img src="./image/pythonstore.jpg" alt="pythonstore" width="500px">
</p>

![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Descrição

<p align="justify">
  Uma aplicação de gerenciamento de produtos e usuários em um ambiente de loja virtual. Ele usa classes para representar usuários, produtos e diferentes categorias de produtos, como eletrônicos :iphone:, vestuário :coat:, calçados :boot: e chapéus :tophat:, com atributos específicos para cada categoria. Possuí métodos de autenticação de usuário e permissões para o administrador adicionar e remover produtos e usuários. Funções para adicionar e remover produtos ao carrinho, verificar o carrinho atual, e finalizar a compra com um resumo de valores. O administrador tem um menu de opções para manipulação direta do catálogo de produtos e lista de usuários. O administrado tem a possibilidade de trocar a senha dele. E é possível o usuário fazer um cadastro na loja para realizar as funções de compra.
</p>

## index.py

```python
from src import imprimirfunc
from src import autentif

imprimirfunc.ImprimirTodosProdutos() # executa a função ImprimirTodosProdutos
autentif.Autentificado() # executa a função Autentificado
```
<p align="justify">
    Irá chamar a função ImprimirTodosProdutos() do módulo imprimirfunc. E após as impressões dos produtos irá chamar a função Autentificado() do módulo autentif para autentificar o usuário.
</p>

## :rocket: Status do Projeto
<p align="center">
  Em construção...
</p>

## Mapa do Projeto

```.
├───image       //pasta com imagens do Readme
└───src         //pasta pasta com os módulos utilizados no código
```
