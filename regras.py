from telas import *

def regras():
  

  print("====== REGRAS =======")

  print("\n==============")
  print("Sobre as coordenadas:")
  print("As coordenadas devem ser fornecidas por uma letra seguida de um número.\nExemplo: A3")
  print("As letras das cordenadas vão de A até J, não sendo válida uma entrada fora desse intervalo.")
  print("Os números das coordenadas vão de 1 até 10, não sendo válida uma entrada fora desse intervalo")
  print("==============")

  print("\n==============")
  print("Sobre as peças do tabuleiro:")  
  print("Porta-aviões | Quantidade: 1 | Ocupa 5 células | Representado por P no tabuleiro")
  print("Navio de batalha | Quantidade: 1 | Ocupa 4 células | Representado por N no tabuleiro")
  print("Cruzador | Quantidade: 1 | Ocupa 3 células | Representado por C no tabuleiro")
  print("Destruidores| Quantidade: 2 | Cada um ocupa 2 células | Representado por D no tabuleiro")
  print("Submarinos| Quantidade: 2 | Cada um ocupa 1 células | Representado por s no tabuleiro")
  print("==================")

  while True:
    validador = input("Digite 's' para avancar: ")
    if validador == "s":
      break
  limpaTela(0.1)
  print(r"""
    .---------------------------------------------------------------------------------.
       ____    ____   __  __        _   ____    _____   ____   _ 
      |  _ \  / __ \ |  \/  |      | | / __ \  / ____| / __ \ | |
      | |_) || |  | || \  / |      | || |  | || |  __ | |  | || |
      |  _ < | |  | || |\/| |  _   | || |  | || | |_ || |  | || |
      | |_) || |__| || |  | | | |__| || |__| || |__| || |__| ||_|
      |____/  \____/ |_|  |_|  \____/  \____/  \_____| \____/ (_)                                                                                                                                                             
    '---------------------------------------------------------------------------------'
    """)
  limpaTela(2)

def modoDeJogo ():
  while True:
    print("=============")
    print("Selecione seu modo de jogo:")
    print("1 - Fácil: 50 tentativas\n2 - Médio: 42 tentativas\n3 - Dificil: 35 tentativas")
    modo = int(input("Digite o número da opção: "))
    if modo == 1:
      limpaTela(0.1)
      return 50
    elif modo == 2:
      limpaTela(0.1)
      return 42
    elif modo == 3:
      limpaTela(0.1) 
      return 35
    else:
      print("Opção inválida, tente novamente")
      continue