import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Label''' # aula 10

ctk.CTkLabel(janela, text="Este texto é estático") # printa na tela um texto estático

text_var = ctk.StringVar(value=input("Digite algo: ")) # variável para receber um input
lab = ctk.CTkLabel(janela, textvariable=text_var) # uma label que printa a variável e depois fica estática
lab.pack()

janela.mainloop() # inicializa a janela
