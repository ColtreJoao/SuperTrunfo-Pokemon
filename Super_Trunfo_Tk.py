import random
from tkinter import *
from tkinter import messagebox

#------------------------------------------------------------------------------------------------------------------------

##### Função que cria as cartas do jogo e suas imagens #####
def cartas_baralho():
    return [
        ["Venusaur", 82, 83, 100, 100, 80, "imagens/Venusaur.png"],
        ["Charizard", 84, 78, 109, 85, 100, "imagens/Charizard.png"],
        ["Blastoise", 83, 100, 85, 105, 78, "imagens/Blastoise.png"],
        ["Sandslash", 100, 110, 45, 55, 65, "imagens/Sandslash.png"],
        ["Nidoqueen", 92, 87, 75, 85, 76, "imagens/Nidoqueen.png"],
        ["Nidoking", 102, 77, 85, 75, 85, "imagens/Nidoking.png"],
        ["Clefable", 70, 73, 95, 90, 60, "imagens/Clefable.png"],
        ["Ninetales", 76, 75, 81, 100, 100, "imagens/Ninetales.png"],
        ["Golbat", 80, 70, 65, 75, 90, "imagens/Golbat.png"],
        ["Vileplume", 80, 85, 110, 90, 50, "imagens/Vileplume.png"],
        ["Parasect", 95, 80, 60, 80, 30, "imagens/Parasect.png"],
        ["Dugtrio", 80, 50, 50, 70, 120, "imagens/Dugtrio.png"],
        ["Golduck", 82, 78, 95, 80, 85, "imagens/Golduck.png"],
        ["Arcanine", 110, 80, 100, 80, 95, "imagens/Arcanine.png"],
        ["Poliwrath", 95, 95, 70, 90, 70, "imagens/Poliwrath.png"],
        ["Alakazam", 50, 45, 135, 95, 120, "imagens/Alakazam.png"],
        ["Machamp", 130, 80, 65, 85, 55, "imagens/Machamp.png"],
        ["Tentacruel", 70, 65, 80, 120, 100, "imagens/Tentacruel.png"],
        ["Gengar", 65, 60, 130, 75, 110, "imagens/Gengar.png"],
        ["Cloyster", 95, 180, 85, 45, 70, "imagens/Cloyster.png"],
        ["Rapidash", 100, 70, 80, 80, 105, "imagens/Rapidash.png"],
        ["Marowak", 80, 110, 50, 80, 45, "imagens/Marowak.png"],
        ["Hitmonlee", 120, 53, 35, 110, 87, "imagens/Hitmonlee.png"],
        ["Hitmonchan", 105, 79, 35, 110, 76, "imagens/Hitmonchan.png"],
        ["Starmie", 75, 85, 100, 85, 115, "imagens/Starmie.png"],
        ["Gyarados", 125, 79, 60, 100, 81, "imagens/Gyarados.png"],
        ["Snorlax", 110, 65, 65, 110, 30, "imagens/Snorlax.png"],
        ["Dragonite", 134, 95, 100, 100, 80, "imagens/Dragonite.png"],
        ["Mr.Mime", 45, 65, 100, 120, 90, "imagens/MrMime.png"],
        ["Mewtwo", 110, 100, 190, 90, 150, "imagens/Mewtwo.png"],
    ]
    
#-----------------------------------------------------------------------------------------------------------

###### Função para distribuir as cartas entre os jogadores #####
def distribuir_cartas(baralho):
    random.shuffle(baralho)
    metade = len(baralho) // 2
    return baralho[:metade], baralho[metade:]

#-------------------------------------------------------------------------------------------------

historico_partidas = []
cartas_jogador = []
cartas_computador = []

def jogar_rodada(carta_jogador, carta_computador, atributo_idx):
    global historico_partidas
    
    if carta_jogador[atributo_idx] > carta_computador[atributo_idx]:
        resultado = "Você ganhou esta rodada!"
    elif carta_jogador[atributo_idx] < carta_computador[atributo_idx]:
        resultado = "Você perdeu esta rodada!"
    else:
        resultado = "Empate!"
    
    historico_partidas.append(f"{carta_jogador[0]} vs {carta_computador[0]} - {resultado}")
    
    if carta_jogador[atributo_idx] > carta_computador[atributo_idx]:
        return "jogador"
    elif carta_jogador[atributo_idx] < carta_computador[atributo_idx]:
        return "computador"
    else:
        return "empate"

    
#-------------------------------------------------------------------------------------------------------------

##### Função para iniciar o jogo #####
def iniciar_jogo():
    global cartas_jogador, cartas_computador, carta_atual_jogador, carta_atual_computador, atributos

    baralho = cartas_baralho()
    cartas_jogador, cartas_computador = distribuir_cartas(baralho)
    carta_atual_jogador = cartas_jogador.pop(0)
    carta_atual_computador = cartas_computador.pop(0)
    atributos = ["nome", "ataque", "defesa", "ataque esp", "defesa esp", "velocidade"]

    atualizar_interface()
    
#---------------------------------------------------------------------------------------------------------------------------

##### Função para atualizar a interface do jogo #####
def atualizar_interface():
    global carta_atual_jogador

    carta_jogador_label.config(text=f"Sua carta: {carta_atual_jogador[0]}\nAtaque: {carta_atual_jogador[1]}\nDefesa: {carta_atual_jogador[2]}\nAtaque Esp: {carta_atual_jogador[3]}\nDefesa Esp: {carta_atual_jogador[4]}\nVelocidade: {carta_atual_jogador[5]}")
    carta_img = PhotoImage(file=carta_atual_jogador[6])
    carta_jogador_img_label.config(image=carta_img)
    carta_jogador_img_label.image = carta_img
    
# -----------------------------------------------------------------------------------------------------------------------

##### Função para selecionar o atributo e jogar a rodada #####
def selecionar_atributo(atributo):
    global carta_atual_jogador, carta_atual_computador, cartas_jogador, cartas_computador

    atributo_idx = atributos.index(atributo)
    resultado = jogar_rodada(carta_atual_jogador, carta_atual_computador, atributo_idx)

    if resultado == "jogador":
        messagebox.showinfo("Resultado", "Você ganhou esta rodada!")
        cartas_jogador.append(carta_atual_jogador)
        cartas_jogador.append(carta_atual_computador)
    elif resultado == "computador":
        messagebox.showinfo("Resultado", "Você perdeu esta rodada!")
        cartas_computador.append(carta_atual_jogador)
        cartas_computador.append(carta_atual_computador)
    else:
        messagebox.showinfo("Resultado", "Empate!")
        cartas_jogador.append(carta_atual_jogador)
        cartas_computador.append(carta_atual_computador)

    if cartas_jogador and cartas_computador:
        carta_atual_jogador = cartas_jogador.pop(0)
        carta_atual_computador = cartas_computador.pop(0)
        atualizar_interface()
    else:
        if len(cartas_jogador) == 0:
            messagebox.showinfo("Fim de Jogo", "Você perdeu o jogo!")
        else:
            messagebox.showinfo("Fim de Jogo", "Você ganhou o jogo!")
        esconder_janela(tela_jogar)
        mostrar_janela(tela_inicial)
        
# ---------------------------------------------------------------------------------------------------        

##### Funções para mostrar e esconder janelas #####
def mostrar_janela(janela):
    janela.deiconify()
    
def esconder_janela(janela):
    janela.withdraw()

def regras_jogo():
    esconder_janela(tela_inicial)
    mostrar_janela(tela_regras)

def historico():
    esconder_janela(tela_inicial)
    mostrar_janela(tela_historico)

def jogar():
    esconder_janela(tela_inicial)
    mostrar_janela(tela_jogar)
    iniciar_jogo()
    
# ------------------------------------------------------------------------------------------------

##### INTERFACE GRAFICA #####
tela_inicial = Tk()
tela_inicial.title("Super Trunfo Pokemon")
tela_inicial.geometry("1920x1080")
tela_inicial.resizable(False, False)
tela_inicial.config(background="Black")

#-------------------------------------------------------------------------------------------------

##### JANELAS AUXILIARES #####
##### Tela de Regras #####
tela_regras = Toplevel(tela_inicial)
tela_regras.title("Regras do Jogo")
tela_regras.geometry("1920x1080")
tela_regras.resizable(False, False)
tela_regras.config(background="Black")
esconder_janela(tela_regras)

Button(tela_regras, text="Voltar", command=lambda: (esconder_janela(tela_regras), mostrar_janela(tela_inicial)), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.03, rely=0.03, anchor=CENTER)

def regras_jogo():
    esconder_janela(tela_inicial)
    mostrar_janela(tela_regras)

    # Adicionando o conteúdo das regras
    Label(tela_regras, text="Regras do Jogo", font=("Georgia", 24), bg="Black", fg="White").pack(pady=20)
    
    regras = [
        "1. O jogador batalha contra um bot.",
        "1. O jogador recebe metade das cartas do baralho no início do jogo.",
        "2. Em cada rodada, o jogador escolhe um atributo da carta atual para competir.",
        "3. O jogador com o valor mais alto no atributo escolhido ganha a rodada e as cartas.",
        "4. O jogo continua até que um jogador fique sem cartas.",
        "5. O jogador com mais cartas no final é o vencedor."
    ]
    
    for regra in regras:
        Label(tela_regras, text=regra, font=("Georgia", 14), bg="Black", fg="White").pack(anchor=W, padx=50)

#-------------------------------------------------------------------------------------------------------------------

##### Tela de Histórico #####
def historico():
    esconder_janela(tela_inicial)
    mostrar_janela(tela_historico)
    atualizar_historico()

def atualizar_historico():
    historico_texto.config(state=NORMAL)
    historico_texto.delete("1.0", END)
    for partida in historico_partidas:
        historico_texto.insert(END, partida + "\n")
    historico_texto.config(state=DISABLED)

tela_historico = Toplevel(tela_inicial)
tela_historico.title("Histórico")
tela_historico.geometry("1920x1080")
tela_historico.resizable(False, False)
tela_historico.config(background="Black")
esconder_janela(tela_historico)

historico_texto = Text(tela_historico, font=("Georgia", 14), bg="Black", fg="White", wrap=WORD, state=DISABLED)
historico_texto.pack(padx=20, pady=20, fill=BOTH, expand=True)

Button(tela_historico, text="Voltar", command=lambda: (esconder_janela(tela_historico), mostrar_janela(tela_inicial)), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.03, rely=0.03, anchor=CENTER)

#--------------------------------------------------------------------------------------------------------


##### Tela de Jogar #####
tela_jogar = Toplevel(tela_inicial)
tela_jogar.title("Jogar")
tela_jogar.geometry("1920x1080")
tela_jogar.resizable(False, False)
tela_jogar.config(background="Black")
esconder_janela(tela_jogar)

Button(tela_jogar, text="Voltar", command=lambda: (esconder_janela(tela_jogar), mostrar_janela(tela_inicial)), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.03, rely=0.03, anchor=CENTER)


carta_jogador_label = Label(tela_jogar, text="", font=("Georgia", 18), bg="Black", fg="White")
carta_jogador_label.place(relx=0.5, rely=0.3, anchor=CENTER)

carta_jogador_img_label = Label(tela_jogar, bg="Black")
carta_jogador_img_label.place(relx=0.5, rely=0.5, anchor=CENTER)

Button(tela_jogar, text="Ataque", command=lambda: selecionar_atributo("ataque"), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.3, rely=0.7, anchor=CENTER)
Button(tela_jogar, text="Defesa", command=lambda: selecionar_atributo("defesa"), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.5, rely=0.7, anchor=CENTER)
Button(tela_jogar, text="Ataque Esp", command=lambda: selecionar_atributo("ataque esp"), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.7, rely=0.7, anchor=CENTER)
Button(tela_jogar, text="Defesa Esp", command=lambda: selecionar_atributo("defesa esp"), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.3, rely=0.8, anchor=CENTER)
Button(tela_jogar, text="Velocidade", command=lambda: selecionar_atributo("velocidade"), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.5, rely=0.8, anchor=CENTER)

#--------------------------------------------------------------------------------------------------------

##### COMPONENTES #####
imagem_inicio1 = PhotoImage(file="imagens/Mewtwo.png")
imagem_inicio1 = imagem_inicio1.zoom(3, 3)
img_1 = Label(image=imagem_inicio1, bg="Black")

imagem_inicio2 = PhotoImage(file="imagens/mew.png")
imagem_inicio2 = imagem_inicio2.zoom(3, 3)
img_2 = Label(image=imagem_inicio2, bg="Black")

imagem = PhotoImage(file="imagens/logo.png")
imagem = imagem.zoom(1, 1)
logo = Label(image=imagem, bg="Black")

botao_jogar = Button(tela_inicial, text="Jogar", font=("Georgia", 18), bg="Black", fg="White", command=jogar)
botao_historico = Button(tela_inicial, text="Histórico", font=("Georgia", 18), bg="Black", fg="White", command=historico)
botao_regras = Button(tela_inicial, text="Regras", font=("Georgia", 18), bg="Black", fg="White", command=regras_jogo)

#--------------------------------------------------------------------------------------------------------

##### CENTRALIZANDO OS COMPONENTES #####
img_1.place(relx=0.2, rely=0.5, anchor=CENTER)
img_2.place(relx=0.9, rely=0.5, anchor=CENTER)
logo.place(relx=0.5, rely=0.25, anchor=CENTER)

botao_jogar.place(relx=0.5, rely=0.5, anchor=CENTER)
botao_historico.place(relx=0.5, rely=0.6, anchor=CENTER)
botao_regras.place(relx=0.5, rely=0.7, anchor=CENTER)

tela_inicial.mainloop()
