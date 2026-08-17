import random
import pickle

class AgenteQLearning:

    def __init__(self, alpha=0.1, gamma=0.9, epsilon=1.0):

        # Taxa de aprendizado
        self.alpha = alpha

        # Fator de desconto
        self.gamma = gamma

        # Probabilidade de exploração
        self.epsilon = epsilon

        self.q_table = {}

    # Obtém o valor Q de uma ação em um estado
    def obter_q(self, estado, acao):

        if estado not in self.q_table:
            return 0.0

        return self.q_table[estado].get(acao, 0.0)

    # Escolhe uma ação usando ε-greedy
    def escolher_acao(self, estado, acoes_disponiveis):

        # Exploração
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(acoes_disponiveis)

        melhor_valor = float("-inf")
        melhores_acoes = []

        for acao in acoes_disponiveis:

            valor = self.obter_q(estado, acao)

            if valor > melhor_valor:
                melhor_valor = valor
                melhores_acoes = [acao]

            elif valor == melhor_valor:
                melhores_acoes.append(acao)

        return random.choice(melhores_acoes)

    # Atualiza a tabela Q
    def atualizar_q(self, estado, acao, recompensa, novo_estado, novas_acoes):

        q_atual = self.obter_q(estado, acao)

        # Melhor valor do próximo estado

        if len(novas_acoes) == 0:
            max_q = 0

        else:
            max_q = max(
                self.obter_q(novo_estado, a)
                for a in novas_acoes
            )

        novo_q = q_atual + self.alpha * (recompensa + self.gamma * max_q - q_atual)

        if estado not in self.q_table:
            self.q_table[estado] = {}

        self.q_table[estado][acao] = novo_q

    # Salva a tabela Q
    def salvar(self, arquivo="q_table.pkl"):

        with open(arquivo, "wb") as f:
            pickle.dump(self.q_table, f)

    # Carrega a tabela Q
    def carregar(self, arquivo="q_table.pkl"):

        try:

            with open(arquivo, "rb") as f:
                self.q_table = pickle.load(f)

        except FileNotFoundError:
            self.q_table = {}