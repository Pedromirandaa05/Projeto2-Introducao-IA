from tabuleiro import Tabuleiro
from agente import AgenteQLearning
from jogador_aleatorio import JogadorAleatorio

NUM_PARTIDAS = 10000

def avaliar():

    ambiente = Tabuleiro()

    agente = AgenteQLearning(epsilon=0)

    agente.carregar()

    adversario = JogadorAleatorio()

    vitorias = 0
    derrotas = 0
    empates = 0

    for partida in range(NUM_PARTIDAS):

        ambiente.reiniciar()

        while not ambiente.terminou():

            # IA escolhe a melhor ação

            estado = ambiente.estado()

            acoes = ambiente.jogadas_disponiveis()

            acao = agente.escolher_acao(estado, acoes)

            ambiente.fazer_jogada(acao, "X")

            # IA venceu

            if ambiente.verificar_vitoria("X"):

                vitorias += 1
                break

            # Empate

            if ambiente.empate():

                empates += 1
                break

            # Jogador aleatório joga

            acao_adversario = adversario.escolher_jogada(ambiente)

            ambiente.fazer_jogada(acao_adversario, "O")

            # IA perdeu

            if ambiente.verificar_vitoria("O"):

                derrotas += 1
                break

            # Empate


            if ambiente.empate():

                empates += 1
                break

        # Mostrar progresso

        if (partida + 1) % 1000 == 0:

            total = partida + 1

            print()
            print(f"Partida {total}")
            print(
                f"Vitórias: {vitorias} "
                f"({vitorias / total * 100:.2f}%)"
            )
            print(
                f"Derrotas: {derrotas} "
                f"({derrotas / total * 100:.2f}%)"
            )
            print(
                f"Empates: {empates} "
                f"({empates / total * 100:.2f}%)"
            )

    # Resultado final

    print()
    print("       AVALIAÇÃO CONCLUÍDA")

    print(f"Total de partidas: {NUM_PARTIDAS}")
    print(f"Vitórias: {vitorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")

    print()

    print(
        f"Taxa de vitória: "
        f"{vitorias / NUM_PARTIDAS * 100:.2f}%"
    )

    print(
        f"Taxa de derrota: "
        f"{derrotas / NUM_PARTIDAS * 100:.2f}%"
    )

    print(
        f"Taxa de empate: "
        f"{empates / NUM_PARTIDAS * 100:.2f}%"
    )

if __name__ == "__main__":
    avaliar()