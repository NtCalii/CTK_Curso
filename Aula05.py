import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''frame''' # aula 05

frame1 = ctk.CTkFrame(master=janela, width=200, height=330).place(x=10, y=60)
frame2 = ctk.CTkFrame(janela, width=200, height=330).place(x=230, y=60)
frame3 = ctk.CTkFrame(master=janela, width=200, height=330).place(x=450, y=60)

janela.mainloop() # inicializa a janela
