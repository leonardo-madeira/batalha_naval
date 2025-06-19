import time
import os


def exibirTabuleiro(tabuleiro, tabuleiro_mascarado, tentativas):
  ordenada = ["A","B","C","D","E","F","G","H","I","J"]

  print(f"Tentativas restantes: {tentativas}")

  print('   1  2  3  4  5  6  7  8  9  10')
  for index, i in enumerate(tabuleiro_mascarado):
    print(f"{ordenada[index]}", end="  ")
    for elemento in i:
      print(f"{elemento}", end="  ")
    print()

def exibirTabuleiroFinal(tabuleiro, tabuleiro_mascarado):
  print("TABULEIRO REAL")
  ordenada = ["A","B","C","D","E","F","G","H","I","J"]
  print('   1  2  3  4  5  6  7  8  9  10')
  for index, i in enumerate(tabuleiro):
    print(f"{ordenada[index]}", end="  ")
    for elemento in i:
      print(f"{elemento}", end="  ")
    print()

  print()
  print()

  print("SEU TABULEIRO APÓS A ÚLTIMA JOGADA")
  print('   1  2  3  4  5  6  7  8  9  10')
  for index, i in enumerate(tabuleiro_mascarado):
    print(f"{ordenada[index]}", end="  ")
    for elemento in i:
      print(f"{elemento}", end="  ")
    print()

def gameOver():
    print(r"""
    .---------------------------------------------------------------------------------.
        _____            __  __  ______    ____ __      __ ______  _____   _ 
       / ____|    /\    |  \/  ||  ____|  / __ \\ \    / /|  ____||  __ \ | |
      | |  __    /  \   | \  / || |__    | |  | |\ \  / / | |__   | |__) || |
      | | |_ |  / /\ \  | |\/| ||  __|   | |  | | \ \/ /  |  __|  |  _  / | |
      | |__| | / ____ \ | |  | || |____  | |__| |  \  /   | |____ | | \ \ |_|
       \_____|/_/    \_\|_|  |_||______|  \____/    \/    |______||_|  \_\(_)                                                                                                                
    '---------------------------------------------------------------------------------'
    """)

    time.sleep(1.5)
    os.system('cls')

    print("Você perdeu por tentativas.")
    print("O tabuleiro original e o seu estão abaixo pra conferência!")
    print()

def winner():
    print(r"""
    .----------------------------------------------------------------------------------------.
     __      __ ____    _____  ______      _____            _   _  _    _   ____   _    _  _ 
     \ \    / // __ \  / ____||  ____|    / ____|    /\    | \ | || |  | | / __ \ | |  | || |
      \ \  / /| |  | || |     | |__      | |  __    /  \   |  \| || |__| || |  | || |  | || |
       \ \/ / | |  | || |     |  __|     | | |_ |  / /\ \  | . ` ||  __  || |  | || |  | || |
        \  /  | |__| || |____ | |____    | |__| | / ____ \ | |\  || |  | || |__| || |__| ||_|
         \/    \____/  \_____||______|    \_____|/_/    \_\|_| \_||_|  |_| \____/  \____/ (_)
    '----------------------------------------------------------------------------------------'
    """)

def limpaTela(x):
    time.sleep(x)
    os.system('cls' if os.name == 'nt' else 'clear')