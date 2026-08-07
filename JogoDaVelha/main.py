from tabuleiro import Tabuleiro
from jogador_aleatorio import JogadorAleatorio

jogo = Tabuleiro()
computador = JogadorAleatorio()

print("Posições do tabuleiro:")
jogo.mostrar_posicoes()

jogador = "X"

while not jogo.terminou():

    jogo.mostrar()

    if jogador == "X":

        try:
            posicao = int(input("Escolha uma posição (0-8): "))
        except ValueError:
            print("Digite um número válido.")
            continue

    else:

        posicao = computador.escolher_jogada(jogo)
        print(f"Computador escolheu: {posicao}")

    if not jogo.fazer_jogada(posicao, jogador):
        print("Jogada inválida!")
        continue

    jogador = "O" if jogador == "X" else "X"

jogo.mostrar()

if jogo.verificar_vitoria("X"):
    print("Jogador X venceu!")

elif jogo.verificar_vitoria("O"):
    print("Jogador O venceu!")

else:
    print("Empate!")