from tkinter import *
from tkinter import messagebox

##### INTERFACE GRAFICA #####
tela_inicial = Tk()
tela_inicial.title("Super Trunfo Pokemon")
tela_inicial.geometry("1280x720")
tela_inicial.resizable(False,False)
tela_inicial.config(background="Black")


##### COMPONENTES #####
botao_jogar = Button(tela_inicial, text = "Jogar", font= ("Georgia", 18), bg= "Black", fg= "White", highlightcolor= "Purple")
botao_historico = Button(tela_inicial, text = "Histórico", font= ("Georgia", 18), bg= "Black", fg= "White", highlightcolor= "Purple")
botao_regras = Button(tela_inicial, text = "Regras", font= ("Georgia", 18), bg= "Black", fg= "White", highlightcolor= "Purple")

##### POSICAO DOS COMPONENTES #####
botao_jogar.grid(row= 5, column= 0, padx= (50,0), pady= (15,0))
botao_historico.grid(row= 6, column= 0, padx= (50,0), pady= (15,0))
botao_regras.grid(row= 7, column= 0, padx= (50,0), pady= (15,0))



tela_inicial.mainloop()