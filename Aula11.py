import customtkinter as ctk # importar a biblioteca
from tkinter import END

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Entry''' # aula 11

entry = ctk.CTkEntry(janela, placeholder_text="Digite seu nome:") # para criar a caixa do entry
entry.pack()

def pegar():
	print(entry.get())
ctk.CTkButton(janela, text="Pegar texto", command=pegar).pack() # para pegar o entry

def apagar():
	entry.delete(0, END)
ctk.CTkButton(janela, text="Apagar texto", command=apagar).pack() # para apagar o entry

janela.mainloop() # inicializa a janela
