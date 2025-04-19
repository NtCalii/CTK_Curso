import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Tab view (abas no tkinter)''' # aula 06

tabview = ctk.CTkTabview(janela, width=400, corner_radius=20, border_color="red", border_width=3) # cria a tela
tabview.pack() # centraliza no meio

tabview.add("Nomes")
tabview.add("Idade") # adiciona a aba e o nome
tabview.add("Sexo")

tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idade").grid_columnconfigure(0, weight=1) # para reposicionar
tabview.tab("Sexo").grid_columnconfigure(0, weight=1)

'''Adicionando elementos'''

text = ctk.CTkLabel(tabview.tab("Nomes"), text="Nathan\nJeferson\nPriscila")
text.pack()

text2 = ctk.CTkLabel(tabview.tab("Idade"), text="19\n47\n43")  # para adicionar contúdo nas abas
text2.pack()

text3 = ctk.CTkLabel(tabview.tab("Sexo"), text="Masculino\nMasculino\nFeminino")
text3.pack()

janela.mainloop() # inicializa a janela
