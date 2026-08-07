import random

class JogadorAleatorio:

    def escolher_jogada(self, tabuleiro):
        
        jogadas = tabuleiro.jogadas_disponiveis()
        return random.choice(jogadas)