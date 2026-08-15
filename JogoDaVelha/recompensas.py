from copy import deepcopy

def recompensa_intermediaria(tabuleiro, ultima_jogada):

    recompensa = 0

    # Centro
    if ultima_jogada == 4:
        recompensa += 0.3

    # Cantos
    if ultima_jogada in [0, 2, 6, 8]:
        recompensa += 0.2

    # Bloqueou vitória do adversário
    if bloqueou_vitoria(tabuleiro):
        recompensa += 2

    return recompensa

def bloqueou_vitoria(tabuleiro):

    jogadas = tabuleiro.jogadas_disponiveis()

    for jogada in jogadas:

        copia = deepcopy(tabuleiro)

        copia.fazer_jogada(jogada, "O")

        if copia.verificar_vitoria("O"):
            return True

    return False