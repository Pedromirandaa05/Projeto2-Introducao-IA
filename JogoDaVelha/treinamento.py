from tabuleiro import Tabuleiro
from agente import AgenteQLearning
from recompensas import recompensa_intermediaria
from jogador_heuristico import JogadorHeuristico
from jogador_aleatorio import JogadorAleatorio

import random
import os
import csv

# Número de partidas utilizadas no treinamento
NUM_EPISODIOS = 50000

def treinar():

    ambiente = Tabuleiro()
    agente = AgenteQLearning()

    # Continua treinando a partir da Q-Table existente
    if os.path.exists("q_table.pkl"):
        agente.carregar()
        print("Q-Table carregada. Continuando treinamento...")
    else:
        print("Nenhuma Q-Table encontrada. Iniciando treinamento do zero.")

    adversario_heuristico = JogadorHeuristico()
    adversario_aleatorio = JogadorAleatorio()

    # Estatísticas gerais
    vitorias = 0
    derrotas = 0
    empates = 0

    # Dados que serão utilizados posteriormente nos gráficos
    resultados = []

    for episodio in range(NUM_EPISODIOS):

        ambiente.reiniciar()

        # Escolhe o adversário da partida
        if random.random() < 0.5:
            adversario = adversario_heuristico
        else:
            adversario = adversario_aleatorio

        ia_comeca = episodio % 2 == 0

        resultado = None
        # Adversário começa metade das partidas
        if not ia_comeca:

            jogada = adversario.escolher_jogada(ambiente)

            ambiente.fazer_jogada(jogada, "O")

        while not ambiente.terminou():

            # 1. Estado atual

            estado = ambiente.estado()

            acoes = ambiente.jogadas_disponiveis()

            # 2. Agente escolhe uma ação

            acao = agente.escolher_acao(estado, acoes)

            # 3. Agente faz a jogada

            ambiente.fazer_jogada(acao, "X")

            # 4. Verificar se a IA venceu

            if ambiente.verificar_vitoria("X"):

                recompensa = 10
                resultado = "Vitoria"

                agente.atualizar_q(estado, acao, recompensa, ambiente.estado(), [])

                vitorias += 1

                break

            # 5. Verificar empate

            if ambiente.empate():

                recompensa = 2
                resultado = "Empate"

                agente.atualizar_q(estado, acao, recompensa, ambiente.estado(), [])

                empates += 1

                break

            # 6. Jogador aleatório joga

            acao_adversario = adversario.escolher_jogada(ambiente)

            ambiente.fazer_jogada(acao_adversario, "O")

            # 7. Verificar se a IA perdeu

            if ambiente.verificar_vitoria("O"):

                recompensa = -10
                resultado = "Derrota"

                agente.atualizar_q(estado, acao, recompensa, ambiente.estado(), [])

                derrotas += 1

                break

            # 8. Verificar empate após jogada do O

            if ambiente.empate():

                recompensa = 2
                resultado = "Empate"

                agente.atualizar_q(estado, acao, recompensa, ambiente.estado(), [])

                empates += 1

                break

            # 9. Partida continua

            recompensa = recompensa_intermediaria(ambiente, acao)

            novo_estado = ambiente.estado()

            novas_acoes = ambiente.jogadas_disponiveis()

            # 10. Atualizar Q-Table

            agente.atualizar_q(estado, acao, recompensa, novo_estado, novas_acoes)

            agente.epsilon = max(
            0.05,
            agente.epsilon * 0.9998)

        # Registrar resultado da partida

        resultados.append({
            "episodio": episodio + 1,
            "resultado": resultado,
            "vitorias": vitorias,
            "derrotas": derrotas,
            "empates": empates
        })

        # Mostrar progresso a cada 1000 partidas

        if (episodio + 1) % 1000 == 0:

            total = episodio + 1

            taxa_vitoria = (vitorias / total) * 100
            taxa_derrota = (derrotas / total) * 100
            taxa_empate = (empates / total) * 100

            print()
            print(f" Episódio {total} ")
            print(f"Vitórias:  {vitorias}")
            print(f"Derrotas:  {derrotas}")
            print(f"Empates:   {empates}")
            print(f"Taxa de vitória: {taxa_vitoria:.2f}%")
            print(f"Taxa de derrota: {taxa_derrota:.2f}%")
            print(f"Taxa de empate:  {taxa_empate:.2f}%")

    # Salvar Q-Table

    agente.salvar()

    # Salvar resultados em CSV

    with open("resultados.csv", "w", newline="", encoding="utf-8") as arquivo:

        campos = ["episodio", "resultado", "vitorias", "derrotas", "empates"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(resultados)

    # Resultado final

    print()
    print("TREINAMENTO CONCLUÍDO")

    print(f"Total de partidas: {NUM_EPISODIOS}")
    print(f"Vitórias: {vitorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")

    print()

    print(
        f"Taxa de vitória: "
        f"{(vitorias / NUM_EPISODIOS) * 100:.2f}%"
    )

    print(
        f"Taxa de derrota: "
        f"{(derrotas / NUM_EPISODIOS) * 100:.2f}%"
    )

    print(
        f"Taxa de empate: "
        f"{(empates / NUM_EPISODIOS) * 100:.2f}%"
    )

    print()
    print("Q-Table salva em: q_table.pkl")
    print("Resultados salvos em: resultados.csv")


if __name__ == "__main__":
    treinar()