import tkinter as tk 


janela_inicial = tk. Tk()

botao_jogo = tk.Button(janela_inicial, text = "Jogar", command = iniciar_jogo)
botao_histórico = tk.Button(janela_inicial, text = "Histórico de Partidas", command = historico_partidas)
botao_regras = tk.Button(janela_inicial, text = "Regras do jogo", command = regras_jogo)

janela_inicial.mainloop