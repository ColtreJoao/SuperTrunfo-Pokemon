from tkinter import *
from tkinter import messagebox
import sys
import os

##### INTERFACE GRAFICA #####

tela_inicial = Tk()
tela_inicial.title("Super Trunfo Pokemon")
tela_inicial.geometry("1280x720")
tela_inicial.resizable(False, False)
tela_inicial.config(background="Black")

# Funções para mostrar e esconder janelas
def mostrar_janela(janela):
    janela.deiconify()
    
def esconder_janela(janela):
    janela.withdraw()

##### FUNCOES #####
def regras_jogo():
    esconder_janela(tela_inicial)
    mostrar_janela(tela_regras)

def historico():
    esconder_janela(tela_inicial)
    mostrar_janela(tela_historico)

def jogar():
    esconder_janela(tela_inicial)
    mostrar_janela(tela_jogar)

##### JANELAS AUXILIARES #####

# Tela de Regras
tela_regras = Toplevel(tela_inicial)
tela_regras.title("Regras do Jogo")
tela_regras.geometry("1280x720")
tela_regras.resizable(False, False)
tela_regras.config(background="Black")
esconder_janela(tela_regras)

# Botão de voltar na tela de regras
Button(tela_regras, text="Voltar", command=lambda: (esconder_janela(tela_regras), mostrar_janela(tela_inicial)), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.03, rely=0.03, anchor=CENTER)

# Tela de Histórico
tela_historico = Toplevel(tela_inicial)
tela_historico.title("Histórico")
tela_historico.geometry("1280x720")
tela_historico.resizable(False, False)
tela_historico.config(background="Black")
esconder_janela(tela_historico)

# Botão de voltar na tela de histórico
Button(tela_historico, text="Voltar", command=lambda: (esconder_janela(tela_historico), mostrar_janela(tela_inicial)), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.03, rely=0.03, anchor=CENTER)

# Tela de Jogar
tela_jogar = Toplevel(tela_inicial)
tela_jogar.title("Jogar")
tela_jogar.geometry("1280x720")
tela_jogar.resizable(False, False)
tela_jogar.config(background="Black")
esconder_janela(tela_jogar)

# Botão de voltar na tela de jogar
Button(tela_jogar, text="Voltar", command=lambda: (esconder_janela(tela_jogar), mostrar_janela(tela_inicial)), font=("Georgia", 18), bg="Black", fg="White").place(relx=0.03, rely=0.03, anchor=CENTER)

##### COMPONENTES #####
#logo#
imagem_inicio1 = PhotoImage(file="imagens/Mewtwo.png")
imagem_inicio1 = imagem_inicio1.zoom(3,3)
img_1 = Label(image=imagem_inicio1, bg= "Black" )

imagem_inicio2 = PhotoImage(file= "imagens/mew.png")
imagem_inicio2 = imagem_inicio2.zoom(3,3)
img_2 = Label(image= imagem_inicio2, bg= "Black")

imagem = PhotoImage(file="imagens/logo.png")
imagem = imagem.zoom(1,1)
logo = Label(image=imagem, bg= "Black")

botao_jogar = Button(tela_inicial, text="Jogar", font=("Georgia", 18), bg="Black", fg="White", command=jogar)
botao_historico = Button(tela_inicial, text="Histórico", font=("Georgia", 18), bg="Black", fg="White", command=historico)
botao_regras = Button(tela_inicial, text="Regras", font=("Georgia", 18), bg="Black", fg="White", command=regras_jogo)

##### CENTRALIZANDO OS COMPONENTES #####
# Ajustando as posições dos botões
img_1.place(relx= 0.2, rely= 0.5, anchor=CENTER)
img_2.place(relx= 0.9, rely= 0.5, anchor=CENTER)
logo.place(relx= 0.5, rely= 0.25, anchor=CENTER)

botao_jogar.place(relx=0.5, rely=0.5, anchor=CENTER)
botao_historico.place(relx=0.5, rely=0.6, anchor=CENTER)
botao_regras.place(relx=0.5, rely=0.7, anchor=CENTER)

tela_inicial.mainloop()
