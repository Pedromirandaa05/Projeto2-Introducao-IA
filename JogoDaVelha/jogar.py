from tabuleiro import Tabuleiro
from agente import AgenteQLearning

def mostrar_tabuleiro(ambiente):
    estado = ambiente.estado()

    print()
    print(f" {estado[0]} | {estado[1]} | {estado[2]} ")
    print("---+---+---")
    print(f" {estado[3]} | {estado[4]} | {estado[5]} ")
    print("---+---+---")
    print(f" {estado[6]} | {estado[7]} | {estado[8]} ")
    print()

def obter_jogada(ambiente):

    while True:

        try:
            jogada = int(
                input("Escolha uma posição (1-9): ")
            )

            # Converter de 1-9 para 0-8
            jogada -= 1

            if jogada not in ambiente.jogadas_disponiveis():
                print("Essa posição não está disponível.")
                continue

            return jogada

        except ValueError:
            print("Digite um número de 1 a 9.")


def jogar():

    ambiente = Tabuleiro()

    # Carregar agente treinado
    agente = AgenteQLearning(epsilon=0)

    agente.carregar()

    print("       JOGO DA VELHA - IA")
    print()
    print("Você é O")
    print("A IA é X")
    print()
    print("Posições do tabuleiro:")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

    ambiente.reiniciar()

    # Partida

    while not ambiente.terminou():

        # IA

        estado = ambiente.estado()

        acoes = ambiente.jogadas_disponiveis()

        acao = agente.escolher_acao(estado, acoes)

        ambiente.fazer_jogada(acao, "X")

        print("A IA jogou:")
        mostrar_tabuleiro(ambiente)

        # Verificar vitória da IA
        if ambiente.verificar_vitoria("X"):

            print("A IA venceu!")
            return

        # Verificar empate
        if ambiente.empate():

            print("Empate!")
            return

        # JOGADOR HUMANO
        
        print("Sua vez.")
        
        jogada = obter_jogada(ambiente)
        
        ambiente.fazer_jogada(jogada, "O")
        
        mostrar_tabuleiro(ambiente)
    
        # Verificar vitória do jogador
        if ambiente.verificar_vitoria("O"):
        
            print("Você venceu!")
            return
        
            # Verificar empate
        if ambiente.empate():
        
            print("Empate!")
            return

if __name__ == "__main__":
    jogar()