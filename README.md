  Batalha Naval
-Descrição do Projeto
Este projeto é uma implementação simples do jogo Batalha Naval em Python. O jogo é jogado em um tabuleiro de 5x5 onde o jogador e o adversário posicionam suas embarcações e se alternam para tentar acertar as embarcações do oponente. O primeiro a destruir todas as embarcações do oponente vence o jogo.

Regras do Jogo


-Inicialização:
O jogador deve iniciar o jogo digitando 1.


-Tabuleiro:
O tabuleiro do jogo é uma matriz 5x5, tanto para o jogador quanto para o adversário.
Posicionamento das Embarcações:
Cada jogador tem 5 embarcações para posicionar em seu tabuleiro.
O jogador escolhe as coordenadas (linha e coluna) onde deseja posicionar cada embarcação.
As coordenadas devem ser inseridas como números de 1 a 5.
O adversário posiciona suas embarcações aleatoriamente.


-Ataques:
O jogador e o adversário se alternam para atacar o tabuleiro do oponente.
O jogador insere as coordenadas (linha e coluna) onde deseja atacar.
Se uma embarcação do adversário for atingida, o símbolo '■' é substituído por 'X' no tabuleiro do adversário.
Se o ataque não atingir uma embarcação, o símbolo 'O' é colocado no tabuleiro.


-Conferência de Vitória:
Após cada ataque, o jogo verifica se todas as embarcações de um dos jogadores foram destruídas.
O jogo termina quando um dos jogadores destrói todas as embarcações do oponente.


-Estrutura do Código:
Função conferir_vitoria:
Verifica se ainda existem embarcações no tabuleiro.
Retorna True se ainda houver embarcações e False se todas foram destruídas.


-Loop Principal:
Inicializa o tabuleiro do jogador e do adversário.
Permite ao jogador posicionar suas embarcações.
O adversário posiciona suas embarcações aleatoriamente.
Executa os turnos de ataque alternados entre jogador e adversário.
Verifica após cada ataque se algum jogador venceu.
youtube:https://www.youtube.com/watch?v=nYXaBl8eVxw
-Integrantes:
João Gabriel de Paula Leite Abreu, Kevyn Gabriel Gonçalves de Moraes, Lorenzo Nakayama Machado, Yuri Allegretti Raffo Rodrigues
