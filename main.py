import random
def conferir_vitoria(matriz):
    for linha in matriz:
        for elemento in linha:
            if elemento == '■':
                return True
    return False
print('Seja bem-vindo à BATALHA NAVAL!')
###tabuleiro inicial adversario
madversario = [
        ['□','□','□','□','□'],
        ['□','□','□','□','□'],
        ['□','□','□','□','□'],
        ['□','□','□','□','□'],
        ['□','□','□','□','□'],
    ]
iniciar = 0
iniciar = int(input('Digite 1 para iniciar:'))
###loop inicial
while iniciar == 1:
    print('Este é o seu tabuleiro:')
    mjogador = [
        ['□','□','□','□','□'],
        ['□','□','□','□','□'],
        ['□','□','□','□','□'],
        ['□','□','□','□','□'],
        ['□','□','□','□','□'],
    ]
    for linha in mjogador:
        print(linha)

###posicionar embarcacoes
    print('Você tem 5 embarcações para posicionar\nDigite as coordenadas das embarcações:')
    
    for i in range(1, 6):
        print(f'Embarcação {i}:')
        emb_y = int(input('Linha:'))
        emb_x = int(input('Coluna:'))
        mjogador[emb_y-1][emb_x-1] = '■'
    print('Seu tabuleiro:')
    for linha in mjogador:
        print(linha)
    

    for i in range(1, 6):
        emb_ady = (random.randint(1,5))
        emb_adx = (random.randint(1,5))
        madversario[emb_ady-1][emb_adx-1] = '■'
    print('Tabuleio do adversário:')
    for linha in madversario:
        print(linha)

###atacar
    print('Hora de atacar!')
    print('Digie as coordenadas onde deseja atacar o tabuleiro do adversário')
    for i in range(100):
            print(f'Rodada {i+1}:')
            atty = int(input('Linha:'))
            attx = int(input('Coluna:'))
            if madversario[atty-1][attx-1] == '■':
                madversario[atty-1][attx-1] = 'X'
                print('Você atingiu uma embarcação inimiga!')
            else:
                madversario[atty][attx] = 'O'
                print('Você não atingiu uma embarcação inimiga')
            print('Tabuleiro do adversário:')
            for i in madversario:
                print(i)
            if not conferir_vitoria(madversario):###conferindo se o jogador venceu
                print('Você venceu!')
                iniciar = 0
                break
            print('Vez do adversário')
            attady = (random.randint(1,5))
            attadx = (random.randint(1,5))
            if mjogador[attady-1][attadx-1] == '■':
                mjogador[attady-1][attadx-1] = 'X'
                print('Uma das suas embarcações foi atingida!')
            else:
                mjogador[attady-1][attadx-1] = 'O'
                print('Nenhuma embarcação foi atingida')
            print('Seu tabuleiro:')
            for i in mjogador:
                print(i)         
            if not conferir_vitoria(mjogador):###conferindo se o adversario venceu
                print('Você perdeu!')
                iniciar = 0
                break            
    break
print('Esse código foi feito por:\nYuri Allegretti')