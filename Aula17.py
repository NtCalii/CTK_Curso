import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''CheckBox''' # aula 17

check_var = ctk.StringVar(value="off") # começa no off

box = ctk.CTkCheckBox(janela, text="CheckBox", variable=check_var, onvalue="on", offvalue="off").pack() # cria a caixa

janela.mainloop() # inicializa a janela
