import random
import os
import time

os.system("cls")

naviosComp = 5
naviosJog = 5

tamanhoTabuleiro = [10, 5]

# Escolha do tamanho tabuleiro
while True:
    try:
        modoJogo = int(input("Bem vindo a batalha naval\n\nEscola o tamanho do tabuleiro\n\ndigite: 1 para 5x10\n        2 para 10x10\n        3 para Personalizado"))
        if modoJogo == 1:
            tamanhoTabuleiro[0] = 10
            tamanhoTabuleiro[1] = 5
            break
        elif modoJogo == 2:
            tamanhoTabuleiro[0] = 10
            tamanhoTabuleiro[1] = 10
            break
        elif modoJogo == 3:
            tamanhoTabuleiro[1] = int(input("Digite a quantidade de linhas do código"))
            tamanhoTabuleiro[0] = int(input("Digite a quantidade de colunas do código"))
            break
        else:
            os.system("cls")
            print("\Opção inválida. Tente novamente\n")
            print("Escola o tamanho do tabuleiro\n\ndigite: 1 para 5x10\n        2 para 10x10\n        3 para Personalizado")
    except ValueError:
        os.system("cls")
        print("Entrada inválida. Digite números\n")
        print("Escola o tamanho do tabuleiro\n\ndigite: 1 para 5x10\n        2 para 10x10\n        3 para Personalizado")

os.system("cls")

# Matrizes para exibição
tabuleiroJogExibir = [['🌊' for i in range(tamanhoTabuleiro[0])] for i in range(tamanhoTabuleiro[1])]

tabuleiroCompExibir = [['🌊' for i in range(tamanhoTabuleiro[0])] for i in range(tamanhoTabuleiro[1])]

# Matrizes escondidas para funcionamento do jogo
tabuleiroJogEsconder = [[0 for i in range(tamanhoTabuleiro[0])] for i in range(tamanhoTabuleiro[1])]

tabuleiroCompEsconder = [[0 for i in range(tamanhoTabuleiro[0])] for i in range(tamanhoTabuleiro[1])]

# Funções para imprimir tabuleiros. Computador e Jogador
def func_exibir_tabuleiro(tabuleiro, tipo, navios, contador=0):
    print(f"         Tabuleiro do {tipo}          Navios restantes: {navios - contador}")

    # Números para coordenas X
    print("        ", end="")
    for i in range(tamanhoTabuleiro[0]):
        if i < tamanhoTabuleiro[0] - 1 and i < 8:
            print(f"{i+1}     ", end="")
        elif i < tamanhoTabuleiro[0] - 1:
            print(f"{i+1}    ", end="")
        else:
            print(f"{i+1}     ")
    
    # Linhas para coordenas X
    print("    ", end="")
    for i in range(tamanhoTabuleiro[0]):
        if i < tamanhoTabuleiro[0] - 1:
            print(f"━━━━━━", end="")
        else:
            print(f"━━━━━━━ x")

    # Números e linhas para coordenas Y
    for linha in range(tamanhoTabuleiro[1]):
        if linha < 9:
            print(f" {linha+1} ┃ {tabuleiro[linha]}")
        else:
            print(f"{linha+1} ┃ {tabuleiro[linha]}")    
        if linha < tamanhoTabuleiro[1] - 1:
            print("   ┃")
    print("   y\n-------------------------------------------------------------------")
    
# Função para ler coordenadas do jogador
def func_input_coordenadas(texto, tabuleiro, parametroTipo, parametroNavios, parametroContador=0):
    while True:
        try:
            x = int(input(f"Escolha a coordenada X {texto}  ")) - 1
            y = int(input(f"Escolha a coordenada Y {texto}  ")) - 1
            if 0 <= x < tamanhoTabuleiro[0] and 0 <= y < tamanhoTabuleiro[1]:
                break
            else:
                os.system("cls")
                if parametroContador:
                    func_exibir_tabuleiro(tabuleiro, parametroTipo, parametroNavios, parametroContador)
                else:
                    func_exibir_tabuleiro(tabuleiro, parametroTipo, parametroNavios)
                print("\nCoordenada inválida. Tente novamente\n")
        except ValueError:
            os.system("cls")
            if parametroContador:
                func_exibir_tabuleiro(tabuleiro, parametroTipo, parametroNavios, parametroContador)
            else:
                func_exibir_tabuleiro(tabuleiro, parametroTipo, parametroNavios)
            print("\nEntrada inválida. Digite números\n")
    return x, y

print("Finalmente, Almirante.\nPosicione a sua frota\n")

# Posicionamento das embarcações
func_exibir_tabuleiro(tabuleiroJogExibir, "Jogador", naviosJog)

for i in range(5):
    while True:
        x, y = func_input_coordenadas(f"para posicionar seus navios {i+1}/5.", tabuleiroJogExibir, "Jogador", naviosJog, i)
        if tabuleiroJogEsconder[y][x] == 0:
            break
        else:
            os.system("cls")
            func_exibir_tabuleiro(tabuleiroJogExibir, "Jogador", naviosJog, i)
            print("Já tem um navio empregado nessa posição")
    os.system("cls")
    tabuleiroJogEsconder[y][x] = 1
    tabuleiroJogExibir[y][x] = '⛵'
    tabuleiroCompEsconder[random.randint(0, tamanhoTabuleiro[1] - 1)][random.randint(0, tamanhoTabuleiro[0] - 1)] = 1
    func_exibir_tabuleiro(tabuleiroJogExibir, "Jogador", naviosJog, i+1)

os.system("cls")

func_exibir_tabuleiro(tabuleiroCompExibir, "Computador", naviosComp)

func_exibir_tabuleiro(tabuleiroJogExibir, "Jogador", naviosJog)

# Loop principal - Jogo
while True:
    # Geração de coordenadas
    x, y = func_input_coordenadas("para realizar um ataque.", tabuleiroCompExibir, "Computador", naviosComp)
    os.system("cls")
    while True:
        w = random.randint(0, tamanhoTabuleiro[1] - 1); z = random.randint(0, tamanhoTabuleiro[0] - 1)
        if tabuleiroJogEsconder[w][z] == 1 or tabuleiroJogExibir[w][z] == "🌊":
            break

    # Ataque jogador
    print(f"Você atacou nas coordenadas: {x + 1, y + 1}")
    for t in range(3):
        print(".", end="", flush=True)
        time.sleep(0.2)
    if tabuleiroCompEsconder[y][x] == 1:
        print("\nNavio inimigo alvejado\n")
        naviosComp -= 1
        tabuleiroCompExibir[y][x] = "💀"
        tabuleiroCompEsconder[y][x] = 2
    elif tabuleiroCompEsconder[y][x] == 2:
        print("\nNavio inimigo já abatido\n")
    else:
        print("\nO disparo não atingiu nada\n")
        tabuleiroCompExibir[y][x] = "❌"

    time.sleep(0.3)
  
    # Tabuleiro do Computador
    func_exibir_tabuleiro(tabuleiroCompExibir, "Computador", naviosComp)

    # Fim de jogo
    if naviosComp == 0:
        func_exibir_tabuleiro(tabuleiroJogExibir, "Jogador", naviosJog)
        print("Excelente Almirante. Você afundou todos os navios inimigos\nJogador ganhou - Obrigado por jogar. by João Abreu, Kevyn Gonçalves, Lorenzo Nakayma, Yuri Allegreti")
        break

    time.sleep(0.5)
    
    # Ataque Computador
    print(f"O computador atacou nas coordenadas: {z + 1, w + 1}")
    for t in range(3):
        print(".", end="", flush=True)
        time.sleep(0.2)
    if tabuleiroJogEsconder[w][z] == 1:
        print("\nSeu navio foi alvejado\n")
        naviosJog -= 1
        tabuleiroJogExibir[w][z] = "💀"
        tabuleiroJogEsconder[w][z] = 2
    else:
        print("\nO disparo não atingiu nada\n")
        tabuleiroJogExibir[w][z] = "❌"

    time.sleep(0.3)
   
    # Tabuleiro do jogador
    func_exibir_tabuleiro(tabuleiroJogExibir, "Jogador", naviosJog)
   
    # Fim de jogo
    if naviosJog == 0:
        print("Barro Almirante. Afundaram todos os seus navios\nComputador ganhou - Obrigado por jogar. by João Abreu, Kevyn Gonçalves, Lorenzo Nakayma, Yuri Allegreti")
        break