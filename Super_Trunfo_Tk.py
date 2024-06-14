from tkinter import *
import random

# Função que irá criar as cartas do jogo
def cartas_baralho():
    # As cartas serão colocadas com os dados [nome, ataque, defesa, ataque Esp, defesa Esp, velocidade]
    return [
        ["Venusaur", 82, 83, 100, 100, 80],
        ["Charizard", 84, 78, 109, 85, 100],
        ["Blastoise", 83, 100, 85, 105, 78],
        ["Sandslash", 100, 110, 45, 55, 65],
        ["Nidoqueen", 92, 87, 75, 85, 76],
        ["Nidoking", 102, 77, 85, 75, 85],
        ["Clefable", 70, 73, 95, 90, 60],
        ["Ninetales", 76, 75, 81, 100, 100],
        ["Golbat", 80, 70, 65, 75, 90],
        ["Vileplume", 80, 85, 110, 90, 50],
        ["Parasect", 95, 80, 60, 80, 30],
        ["Dugtrio", 80, 50, 50, 70, 120],
        ["Golduck", 82, 78, 95, 80, 85],
        ["Arcanine", 110, 80, 100, 80, 95],
        ["Poliwrath", 95, 95, 70, 90, 70],
        ["Alakazam", 50, 45, 135, 95, 120],
        ["Machamp", 130, 80, 65, 85, 55],
        ["Tentacruel", 70, 65, 80, 120, 100],
        ["Gengar", 65, 60, 130, 75, 110],
        ["Cloyster", 95, 180, 85, 45, 70],
        ["Rapidash", 100, 70, 80, 80, 105],
        ["Marowak", 80, 110, 50, 80, 45],
        ["Hitmonlee", 120, 53, 35, 110, 87],
        ["Hitmonchan", 105, 79, 35, 110, 76],
        ["Starmie", 75, 85, 100, 85, 115],
        ["Gyarados", 125, 79, 60, 100, 81],
        ["Snorlax", 110, 65, 65, 110, 30],
        ["Dragonite", 134, 95, 100, 100, 80],
        ["Mr.Mime", 45, 65, 100, 120, 90],
        ["Mewtwo", 110, 100, 190, 90, 150],
    ]

def separar_cartas(baralho):
    random.shuffle(baralho)
    metade = len(baralho) // 2
    return baralho[:metade], baralho[metade:]

def rodadas_jogo():
    pass  # Aqui você pode adicionar a lógica do jogo

# Criar uma janela
root = Tk()
root.title("Jogo de Cartas")

# Função para exibir as regras
def exibir_regras():
    regras = Toplevel(root)
    regras.title("Regras do Jogo")
    texto = Label(regras, text="Regras do Jogo Aqui")
    texto.pack()

# Função para exibir o histórico
def exibir_historico():
    historico = Toplevel(root)
    historico.title("Histórico do Jogo")
    texto = Label(historico, text="Histórico do Jogo Aqui")
    texto.pack()
# Função para sair do jogo
def sair_jogo():
    root.destroy()

# Criar botões
botao_jogar = Button(root, text="Jogar", command=rodadas_jogo)
botao_regras = Button(root, text="Regras", command=exibir_regras)
botao_historico = Button(root, text="Histórico", command=exibir_historico)
botao_sair = Button(root, text="Sair", command=sair_jogo)

# Colocar os botões na janela
botao_jogar.pack()
botao_regras.pack()
botao_historico.pack()
botao_sair.pack()

# Rodar a aplicação
root.mainloop()