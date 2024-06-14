from tkinter import *
from tkinter import messagebox

##### INTERFACE GRAFICA #####
tela_inicial = Tk()
tela_inicial.title("Super Trunfo Pokemon")
tela_inicial.geometry("450x300+400+200")
tela_inicial.resizable(False,False)
tela_inicial.config(background="Black")


##### COMPONENTES #####
botao_jogar = Button(tela_inicial, text = "Jogar")
botao_historico = Button(tela_inicial, text = "Histórico")
botao_regras = Button(tela_inicial, text = "Regras")

##### POSICAO DOS COMPONENTES #####
botao_jogar.grid(row= 1, column= 0, padx= (50,0), pady= (15,0))
botao_historico.grid(row= 2, column= 0, padx= (50,0), pady= (15,0))
botao_regras.grid(row= 3, column= 0, padx= (50,0), pady= (15,0))
