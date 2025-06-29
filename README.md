# Jogo Batalha Naval em Python

## Descrição
Este projeto é referente a uma atividade da disciplina de algoritimos no curso de Ciência de Dados e Inteligência Arficial da Universiade Estadual de Londrina.

Este projeto implementa o clássico jogo Batalha Naval em Python, onde o jogador deve descobrir a posição dos navios em um tabuleiro 10x10. Os navios são posicionados aleatoriamente pelo sistema e o jogador tem um número limitado de tentativas para acertar todos os navios.

O jogo apresenta interface simples no terminal, com atualização do tabuleiro após cada jogada, indicação de acertos e erros, e controle do progresso com exibição de peças já acertadas.

---

## Como Rodar

1. Tenha Python 3 instalado no seu sistema.
2. Certifique-se que o projeto esteja organizado da seguinte forma:

```
batalha_naval/
├── main.py
└── src/
    ├── jogada.py
    ├── regras.py
    ├── tabuleiro.py
    └── telas.py
```

3. Execute o jogo pelo terminal, estando na pasta raiz do projeto (`batalha_naval`):

```bash
python main.py
```

4. Siga as instruções na tela para escolher o modo de jogo e inserir coordenadas.

---

## Decisões Funcionamento

### Tabuleiros
- Existem 3 tabuleiros rodando simultaneamente:
  - ```tabuleiro``` : tabuleiro real que está com a posição de todas as peças
  - ```tabuleiro_mascarado``` : aquele que é exibido para o jogador com todas as posições inicialmente preenchidas por ```X```
  - ```tabuleiro_contador``` : tabuleiro backend para contar a quantidade de peças que o jogador acertou e determinar vitória, inicialmente preenchidas por ```~```

### Determinar vitória

#### O sistema para determinar vitória desenvovlido é feito através da seguinte equação: ```len(tabuleiro)*len(tabuleiro) - somatório das peças```

#### Essa conta representa a quantidade total de casas do tabuleiro menos a quantidade de peças existentes. A partir do momento que a quantidade de água presente no tabuleiro é igual ao resultado da equação, é sinal que o jogador venceu a partida.


### Posicionamento dos Navios

- O tabuleiro é uma matriz 10x10 preenchida inicialmente com água (`"~"`).
- Os navios (Porta-aviões, Navio de batalha, Cruzador, Destruidor e Submarino) são representados por letras iniciais e possuem tamanhos definidos.
- O posicionamento dos navios é aleatório, horizontal ou vertical, garantindo que não haja sobreposição.
- Um validador confere se a posição escolhida para o navio está livre antes de posicioná-lo.


### Controle de Jogadas

- O jogador informa a coordenada da jogada no formato letra + número (exemplo: `A5`).
- O programa valida se a coordenada é válida e se a posição ainda não foi jogada.
- Cada jogada atualiza o tabuleiro mascarado, mostrando acertos e mantendo posições não descobertas ocultas.
- O jogo informa se houve acerto ou se atingiu a água.
- O número de tentativas varia conforme o modo escolhido pelo jogador (Fácil, Médio, Difícil).
- O jogo termina quando o jogador acerta todos os navios ou esgota as tentativas.

---

## Exemplos de Uso

- Ao iniciar, escolha o nível de dificuldade:

```
Selecione seu modo de jogo:
1 - Fácil: 50 tentativas
2 - Médio: 42 tentativas
3 - Difícil: 35 tentativas
Digite o número da opção:
```

- Depois, veja as regras explicadas e o tabuleiro com as posições não descobertas marcadas com `X`.

- Ao jogar, insira coordenadas válidas (exemplo: `B7`).

- O jogo mostrará mensagens como:

```
Você acertou um Cruzador
```

ou

```
Você atingiu a água!
```

- No fim, se você vencer, verá uma mensagem de parabéns, ou se perder, o tabuleiro final para conferência.

---

*Idealizado e desenvolvido por Leonardo Madeira*<br>
*Apenas o Readme.md foi gerado com auxílio de IA*