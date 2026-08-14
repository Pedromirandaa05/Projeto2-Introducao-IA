import random
from copy import deepcopy

class JogadorHeuristico:

    def escolher_jogada(self, tabuleiro):

        jogadas = tabuleiro.jogadas_disponiveis()

        # 1. Se puder vencer, vence
        for jogada in jogadas:

            copia = deepcopy(tabuleiro)

            copia.fazer_jogada(jogada, "O")

            if copia.verificar_vitoria("O"):
                return jogada

        # 2. Se a IA puder vencer na próxima jogada, bloqueia
        for jogada in jogadas:

            copia = deepcopy(tabuleiro)

            copia.fazer_jogada(jogada, "X")

            if copia.verificar_vitoria("X"):
                return jogada

        # 3. Centro
        if 4 in jogadas:
            return 4

        # 4. Cantos
        cantos = [0, 2, 6, 8]
        livres = [c for c in cantos if c in jogadas]

        if livres:
            return random.choice(livres)

        # 5. Restante
        return random.choice(jogadas)