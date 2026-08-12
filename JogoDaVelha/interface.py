import tkinter as tk
from tkinter import messagebox

from tabuleiro import Tabuleiro
from agente import AgenteQLearning


COR_X = "#1976D2"
COR_O = "#D32F2F"

COR_VITORIA = "#8BC34A"

COR_FUNDO = "#ECEFF1"

COR_BOTAO = "white"


class Interface:

    def __init__(self):

        self.tabuleiro = Tabuleiro()

        self.agente = AgenteQLearning(epsilon=0)
        self.agente.carregar()

        self.janela = tk.Tk()

        self.janela.title("Jogo da Velha - IA")

        self.janela.configure(bg=COR_FUNDO)

        self.status = tk.Label(self.janela, text="Sua vez", font=("Arial",18,"bold"), bg=COR_FUNDO)

        self.status.grid(row=0, column=0, columnspan=3, pady=15)

        self.botoes = []

        for linha in range(3):

            linha_botoes=[]

            for coluna in range(3):

                indice = linha*3+coluna

                botao = tk.Button(self.janela, width=4, height=2, font=("Arial",32,"bold"),
                                  bg=COR_BOTAO, relief="raised", command=lambda i=indice:self.jogada_humano(i))

                botao.grid(row=linha+1, column=coluna, padx=6, pady=6)

                linha_botoes.append(botao)

            self.botoes.append(linha_botoes)

        tk.Button(self.janela, text="Nova partida", font=("Arial",12),command=self.reiniciar).grid(row=4, column=0, columnspan=3, pady=15)

        self.reiniciar()

        self.janela.mainloop()

    def atualizar(self):

        estado=self.tabuleiro.estado()

        for i in range(9):

            l=i//3
            c=i%3

            texto=estado[i]

            if texto==" ":
                texto=""

            self.botoes[l][c]["text"]=texto

            self.botoes[l][c]["bg"]=COR_BOTAO

            if texto=="X":
                self.botoes[l][c]["fg"]=COR_X

            elif texto=="O":
                self.botoes[l][c]["fg"]=COR_O

    def destacar(self,linha):

        for indice in linha:

            l=indice//3
            c=indice%3

            self.botoes[l][c]["bg"]=COR_VITORIA


    def jogada_humano(self,posicao):

        if posicao not in self.tabuleiro.jogadas_disponiveis():
            return

        self.tabuleiro.fazer_jogada(posicao,"O")

        self.atualizar()

        if self.tabuleiro.verificar_vitoria("O"):

            self.destacar(self.tabuleiro.linha_vencedora("O"))

            messagebox.showinfo(
                "Fim",
                "Você venceu!"
            )

            self.reiniciar()

            return

        if self.tabuleiro.empate():

            messagebox.showinfo(
                "Fim",
                "Empate!"
            )

            self.reiniciar()

            return

        self.status["text"]="IA pensando..."

        self.janela.after(350, self.jogada_ia)

    def jogada_ia(self):

        estado=self.tabuleiro.estado()

        acoes=self.tabuleiro.jogadas_disponiveis()

        acao=self.agente.escolher_acao(estado, acoes)

        self.tabuleiro.fazer_jogada(acao, "X")

        self.atualizar()

        if self.tabuleiro.verificar_vitoria("X"):

            self.destacar(self.tabuleiro.linha_vencedora("X"))

            messagebox.showinfo(
                "Fim",
                "A IA venceu!"
            )

            self.reiniciar()

            return

        if self.tabuleiro.empate():

            messagebox.showinfo(
                "Fim",
                "Empate!"
            )

            self.reiniciar()

            return

        self.status["text"]="Sua vez"

    def reiniciar(self):

        self.tabuleiro.reiniciar()

        self.atualizar()

        self.status["text"]="Sua vez"

if __name__=="__main__":
    Interface()