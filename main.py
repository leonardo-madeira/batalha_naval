from regras import *
from tabuleiro import *
from jogada import *
from telas import *

if __name__ ==  '__main__':
  tentativas = modoDeJogo()
  tabuleiro = criarTabuleiro()
  tabuleiro_mascarado = [["X" for _ in range(10)] for _ in range(10)]
  tabuleiro_contador = [["~" for _ in range(10)] for _ in range(10)]

  regras()

  while tentativas:
    if vitoria(tabuleiro_contador):
      break
    
    exibirTabuleiro(tabuleiro, tabuleiro_mascarado, tentativas)
    print()
    contadorPecas(tabuleiro_contador)
    print()

    coordenadas = validacaoCoordenada()
    if coordenadas:
      if validaJogada(coordenadas, tabuleiro, tabuleiro_mascarado, tabuleiro_contador):
        limpaTela(1)

        tentativas -= 1
      else:
        limpaTela(1)
    else:
      print("Coordenada inválida, tente novamente!")
      limpaTela(0.5)

  limpaTela(0)
  if tentativas == 0:
    gameOver()
    exibirTabuleiroFinal(tabuleiro,tabuleiro_mascarado)
  else:
    winner()