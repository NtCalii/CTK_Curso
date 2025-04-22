import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("200x100") # dimensão inicial
janela.maxsize(width=200, height=100) # tamanho max
janela.minsize(width=200, height=100) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

# janela.grid_columnconfigure() pode fazer configurações nela

'''Grid (Posicionamento de Widgets na  Janela)''' # aula 22

ctk.CTkLabel(janela, text="Texto 1").grid(row=0, column=0, padx=25) # divide em linhas e colunas

ctk.CTkLabel(janela, text="Texto 2").grid(row=0, column=1, padx=25) # podendo colocar em qual você quer

ctk.CTkLabel(janela, text="Texto 3").grid(row=1, column=0, padx=25) # igual uma planilha

ctk.CTkLabel(janela, text="Texto 4").grid(row=1, column=1, padx=25) # pode adicionar pad

ctk.CTkLabel(janela, text="Texto 5").grid(row=2, column=0, padx=25, sticky="w") # pode formatar elas

janela.mainloop() # inicializa a janela
