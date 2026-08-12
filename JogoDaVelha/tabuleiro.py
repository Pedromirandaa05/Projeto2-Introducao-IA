class Tabuleiro:
    def __init__(self):
        self.reiniciar()

    def reiniciar(self):
        self.tabuleiro = [" " for _ in range(9)]

    def mostrar(self):
        print()
        print(f" {self.tabuleiro[0]} | {self.tabuleiro[1]} | {self.tabuleiro[2]}")
        print("---+---+---")
        print(f" {self.tabuleiro[3]} | {self.tabuleiro[4]} | {self.tabuleiro[5]}")
        print("---+---+---")
        print(f" {self.tabuleiro[6]} | {self.tabuleiro[7]} | {self.tabuleiro[8]}")
        print()

    def mostrar_posicoes(self):
        print()
        print(" 0 | 1 | 2")
        print("---+---+---")
        print(" 3 | 4 | 5")
        print("---+---+---")
        print(" 6 | 7 | 8")
        print()

    def fazer_jogada(self, posicao, jogador):

        if posicao < 0 or posicao > 8:
            return False

        if self.tabuleiro[posicao] != " ":
            return False

        self.tabuleiro[posicao] = jogador
        return True

    def jogadas_disponiveis(self):
        return [i for i in range(9) if self.tabuleiro[i] == " "]

    def verificar_vitoria(self, jogador):

        combinacoes = [
            (0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6)
        ]

        for a, b, c in combinacoes:
            if (self.tabuleiro[a] == jogador and
                self.tabuleiro[b] == jogador and
                self.tabuleiro[c] == jogador):
                return True

        return False

    def empate(self):

        return (" " not in self.tabuleiro and
                not self.verificar_vitoria("X") and
                not self.verificar_vitoria("O"))

    def terminou(self):

        return (
            self.verificar_vitoria("X") or
            self.verificar_vitoria("O") or
            self.empate()
        )

    def estado(self):
        
        return "".join(self.tabuleiro)

    def vencedor(self):

        if self.verificar_vitoria("X"):
            return "X"

        if self.verificar_vitoria("O"):
            return "O"

        return None

    def linha_vencedora(self, jogador):

        combinacoes = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        estado = self.estado()

        for a, b, c in combinacoes:
            if (
                estado[a] == jogador and
                estado[b] == jogador and
                estado[c] == jogador
            ):
                return (a, b, c)

        return None