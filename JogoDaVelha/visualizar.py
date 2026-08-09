import pickle


with open("q_table.pkl", "rb") as arquivo:
    q_table = pickle.load(arquivo)


print("Quantidade de estados aprendidos:", len(q_table))
print()


for estado, acoes in q_table.items():

    print("Estado:", repr(estado))

    for acao, valor in acoes.items():
        print(f"  Ação {acao}: {valor:.4f}")

    print("-" * 40)