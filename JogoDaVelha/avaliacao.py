from tabuleiro import Tabuleiro
from agente import AgenteQLearning
from jogador_heuristico import JogadorHeuristico

NUM_PARTIDAS = 10000

def jogar_partida(agente, adversario, ia_comeca):

    ambiente = Tabuleiro()

    while not ambiente.terminou():

        # IA começa
        if ia_comeca:

            estado = ambiente.estado()
            acoes = ambiente.jogadas_disponiveis()

            acao = agente.escolher_acao(estado, acoes)

            ambiente.fazer_jogada(acao, "X")

            if ambiente.verificar_vitoria("X"):
                return "Vitoria"

            if ambiente.empate():
                return "Empate"

        # Adversário joga
        acao_adversario = adversario.escolher_jogada(ambiente)

        ambiente.fazer_jogada(acao_adversario, "O")

        if ambiente.verificar_vitoria("O"):
            return "Derrota"

        if ambiente.empate():
            return "Empate"

        # Agora a IA joga
        estado = ambiente.estado()
        acoes = ambiente.jogadas_disponiveis()

        acao = agente.escolher_acao(estado, acoes)

        ambiente.fazer_jogada(acao, "X")

        if ambiente.verificar_vitoria("X"):
            return "Vitoria"

        if ambiente.empate():
            return "Empate"

        # Próxima rodada
        ia_comeca = False


def avaliar():

    agente = AgenteQLearning(epsilon=0)
    agente.carregar()

    adversario = JogadorHeuristico()

    vitorias = 0
    derrotas = 0
    empates = 0

    for partida in range(NUM_PARTIDAS):

        # Alterna quem começa
        ia_comeca = partida % 2 == 0

        resultado = jogar_partida(
            agente,
            adversario,
            ia_comeca
        )

        if resultado == "Vitoria":
            vitorias += 1

        elif resultado == "Derrota":
            derrotas += 1

        else:
            empates += 1

        if (partida + 1) % 1000 == 0:

            total = partida + 1

            print()
            print(f"Partida {total}")
            print(f"Vitórias: {vitorias} ({vitorias / total * 100:.2f}%)")
            print(f"Derrotas: {derrotas} ({derrotas / total * 100:.2f}%)")
            print(f"Empates: {empates} ({empates / total * 100:.2f}%)")

    print()
    print("AVALIAÇÃO CONCLUÍDA")

    print(f"Total de partidas: {NUM_PARTIDAS}")
    print(f"Vitórias: {vitorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")

    print()

    print(f"Taxa de vitória: {vitorias / NUM_PARTIDAS * 100:.2f}%")
    print(f"Taxa de derrota: {derrotas / NUM_PARTIDAS * 100:.2f}%")
    print(f"Taxa de empate: {empates / NUM_PARTIDAS * 100:.2f}%")


if __name__ == "__main__":
    avaliar()