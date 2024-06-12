import random
from tkinter import *

# Função que cria as cartas do jogo
def cartas_baralho():
    # As cartas serão colocadas com os dados [nome, ataque, defesa, ataque esp, defesa esp, velocidade]
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

# Função para distribuir as cartas entre os jogadores
def distribuir_cartas(baralho):
    random.shuffle(baralho)  # Embaralha o baralho
    metade = len(baralho) // 2  # Calcula a metade do baralho
    return baralho[:metade], baralho[metade:]  # Divide o baralho entre dois jogadores

# Função para jogar uma rodada
def jogar_rodada(carta_jogador, carta_computador, atributo_idx):
    if carta_jogador[atributo_idx] > carta_computador[atributo_idx]:
        return "jogador"
    elif carta_jogador[atributo_idx] < carta_computador[atributo_idx]:
        return "computador"
    else:
        return "empate"

# Função principal do jogo
def jogo_super_trunfo():
    baralho = cartas_baralho()  # Cria o baralho de cartas
    cartas_jogador, cartas_computador = distribuir_cartas(baralho)  # Distribui as cartas entre os jogadores

    atributos = ["nome", "ataque", "defesa", "ataque esp", "defesa esp", "velocidade"]
    
    while cartas_jogador and cartas_computador:  # Enquanto ambos os jogadores tiverem cartas
        print(f"Jogador tem {len(cartas_jogador)} cartas, Computador tem {len(cartas_computador)} cartas")
        
        # Remove a primeira carta de cada jogador com .pop(0)
        carta_jogador = cartas_jogador.pop(0)  # Remove e retorna a primeira carta da lista de cartas do jogador
        carta_computador = cartas_computador.pop(0)  # Remove e retorna a primeira carta da lista de cartas do computador
        
        print(f"Sua carta: {carta_jogador}")
        

        atributo = input("Escolha um atributo para comparar (ataque, defesa, ataque esp, defesa esp, velocidade): ")
        
        if atributo not in atributos:
            print("Atributo inválido. Você perde a vez.")
            cartas_computador.append(carta_computador)  # Adiciona a carta do computador de volta ao final da lista
            cartas_computador.append(carta_jogador)  # Adiciona a carta do jogador ao final da lista do computador
            continue
        
        # Mapear o atributo para seu índice na sublista
        atributo_idx = atributos.index(atributo)

        resultado = jogar_rodada(carta_jogador, carta_computador, atributo_idx)

        if resultado == "jogador":
            print("Você ganhou esta rodada!")
            # Adiciona ambas as cartas ao final da lista de cartas do jogador
            cartas_jogador.append(carta_jogador)
            cartas_jogador.append(carta_computador)
        elif resultado == "computador":
            print("Você perdeu esta rodada!")
            # Adiciona ambas as cartas ao final da lista de cartas do computador
            cartas_computador.append(carta_jogador)
            cartas_computador.append(carta_computador)
        else:
            print("Empate!")
            # Adiciona ambas as cartas de volta ao final de suas listas originais
            cartas_jogador.append(carta_jogador)
            cartas_computador.append(carta_computador)

        print("\n")

    if len(cartas_jogador) == 0:
        print("Você perdeu o jogo!")
    else:
        print("Você ganhou o jogo!")

# Iniciar o jogo
jogo_super_trunfo()
