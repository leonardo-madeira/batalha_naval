def validacaoCoordenada():
  posicao = input("Insira a coordenada: ").upper()
  linha_dicionario = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
  }
  
  if posicao[0].isalpha() and posicao[1:].isdigit():
    linha = posicao[0]
    coluna = int(posicao[1:])
    print(coluna)
    if linha in linha_dicionario.keys() and coluna > 0 and coluna <= 10:
      coluna = coluna - 1
      for letra, i in linha_dicionario.items():
        if linha == letra:
          return [i, coluna]
  
  return False
  
def validaJogada(coordenada:list, tabuleiro:list,tabuleiro_mascarado, tabuleiro_contador:list):
  pecas = {
    "Porta-aviões": "P",
    "Navio de batalha": "N",
    "Cruzador": "C",
    "Destruidor": "D",
    "Submarino": "S",
  }

  if tabuleiro_mascarado[coordenada[0]][coordenada[1]] != "X":
    print("Você já jogou nessa posição!")
    return False
  
  tabuleiro_mascarado[coordenada[0]][coordenada[1]] = tabuleiro[coordenada[0]][coordenada[1]]
  tabuleiro_contador[coordenada[0]][coordenada[1]] = tabuleiro[coordenada[0]][coordenada[1]]



  if tabuleiro[coordenada[0]][coordenada[1]] != "~":
    for peca, inicial in pecas.items():
      if tabuleiro[coordenada[0]][coordenada[1]] == inicial:
        print(f"Você acertou um {peca}"),
    return True
  else:
    print("Você atingiu a água!")
    return True
  
def vitoria(tabuleiro_contador):
  
  soma_pecas = 18
  qnt_posicoes = len(tabuleiro_contador) * len(tabuleiro_contador) 
  qnt_agua_min = qnt_posicoes - soma_pecas

  frequencia = {"~": 0}

  for i in tabuleiro_contador:
    for elemento in i:
      if elemento == "~":
        frequencia[elemento] += 1
  
  if frequencia["~"] == qnt_agua_min:
    return True

def contadorPecas(tabuleiro_contador):
  pecas = {
    "Porta-aviões": 5,
    "Navio de batalha": 4,
    "Cruzador": 3,
    "Destruidor": 4,
    "Submarino": 2,
  }
   
  frequencia = {
    "P": 0,
    "N": 0,
    "C": 0,
    "D": 0,
    "S": 0,
  }

  for i in tabuleiro_contador:
   for elemento in i:
     if elemento != "~":
       frequencia[elemento] += 1
    
  print("Você já acertou: ")


  for index, (peca_atual, quantidade_atual) in enumerate(frequencia.items()):
    print(f"{list(pecas.keys())[index]}: {quantidade_atual}/{list(pecas.values())[index]}")
    

