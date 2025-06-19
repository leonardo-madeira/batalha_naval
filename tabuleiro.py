import random

def validadorPosicao(tabuleiro, linha, coluna, tamanho, orientacao):
  if orientacao == 'h':
    for i in range(tamanho):
        if tabuleiro[linha][coluna + i] != "~":
          return False
  else:
    for i in range(tamanho):
        if tabuleiro[linha + i][coluna] != "~":
          return False
  return True

def criarTabuleiro():
  tabuleiro = [["~" for _ in range(10)] for _ in range(10)]

  pecas = {
    "Porta-aviões": 5,
    "Navio de batalha": 4,
    "Cruzador": 3,
    "Destruidor": 2,
    "Destruidor2": 2,
    "Submarino": 1,
    "Submarino2": 1
  }

  for peca, tamanho in pecas.items():

    verifica_posicao = False
    h = ((0,9), (0, 9 - tamanho))
    v = ((0, 9 - tamanho), (0,9)) 
    while not verifica_posicao:
      orientacao = random.choice(['h', 'v'])
      linha = random.randint(h[0][0], h[0][1]) if orientacao == 'h' else random.randint(v[0][0], v[0][1])
      coluna = random.randint(h[1][0], h[1][1]) if orientacao == 'h' else random.randint(v[1][0], v[1][1])

      if validadorPosicao(tabuleiro, linha, coluna, tamanho, orientacao):
        for i in range(tamanho):
          if orientacao == 'h':
            tabuleiro[linha][coluna + i] = peca[0]
          else:
            tabuleiro[linha + i][coluna] = peca[0]
        verifica_posicao = True

  return tabuleiro