import random

def tabuleiro(rows, cols, num_mina):
    # Inicializa o tabuleiro com todos os quadrados laranjas
    tab = [["🟨" for _ in range(cols)] for _ in range(rows)]

    # Coloca as minas no tabuleiro aleatoriamente
    bombas_colocadas = 0
    while bombas_colocadas < num_mina:
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if tab[row][col] != "💣":
            tab[row][col] = "💣"
            bombas_colocadas += 1

    return tab

def repr_tabuleiro(tab):
    for row in tab:
        print(" ".join(row))

def check_quadrado(tab, row, col):
    if tab[row][col] == "💣":
        return "\033[1;31;40mBOOM! Você acertou uma bomba\033[0m"  # Texto em vermelho
    else:
        return "\033[1;32;40mVocê está seguro\033[0m"  # Texto em verde

# Tamanho do tabuleiro e número de minas
rows, cols, num_minas = 5, 5, 5

# Cria o tabuleiro
board = tabuleiro(rows, cols, num_minas)

# Loop do jogo interativo
tabuleiro_mostrado = False  # Flag para controlar se o tabuleiro inteiro foi mostrado
game_over = False  # Flag para controlar se o jogo terminou
while not game_over:
    # Se o tabuleiro não foi mostrado, imprime o tabuleiro inicial com quadrados amarelos
    if not tabuleiro_mostrado:
        print("Campo Minado ...  ")
        repr_tabuleiro([["🟨" for _ in range(cols)] for _ in range(rows)])
        print("Escolha uma célula para revelar.")
        tabuleiro_mostrado = True

    # Pede ao jogador para escolher uma célula
    while True:
        row = int(input("Escolha a linha: "))
        col = int(input("Escolha a coluna: "))
        if 1 <= row <= rows and 1 <= col <= cols:
            break
        else:
            print("Por favor, escolha uma linha e coluna válidas.")

    # Verifica se a célula contém alguma bomba
    resultado = check_quadrado(board, row - 1, col - 1)

    # Se o jogador acertou uma bomba ou desistiu, mostra todas as bombas e encerra o jogo
    if resultado.startswith("BOOM!") or resultado.lower().startswith("desistiu"):
        print("\033[1;31;40mTabuleiro completo:\033[0m")  # Título em vermelho
        repr_tabuleiro(board)
        game_over = True
    else:
        # Caso contrário, mostra apenas a célula selecionada
        print("\033[1;32;40mTabuleiro:\033[0m")  # Título em verde
        tab = [["🟨" for _ in range(cols)] for _ in range(rows)]
        tab[row - 1][col - 1] = board[row - 1][col - 1]
        repr_tabuleiro(tab)

    print(resultado)

    # Pergunta ao jogador se ele quer continuar jogando
    if not game_over:
        play_again = input("Quer jogar de novo? (s/n): ")
        if play_again.lower() != "s":
            game_over = True
