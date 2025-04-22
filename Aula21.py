import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("400x300") # dimensão inicial
janela.maxsize(width=400, height=300) # tamanho max
janela.minsize(width=400, height=300) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Pack (Posicionamento de Widgets na  Janela)''' # aula 21

ctk.CTkLabel(janela, text="faça login".upper(), font=("arial bold", 40)).pack(pady=10) # centraliza no meio

ctk.CTkEntry(janela, placeholder_text="usuário...", width=250, height=45).pack(pady=20) # da um espaço no elemento

ctk.CTkEntry(janela, placeholder_text="senha...", width=250, height=45, show="*").pack() # centraliza no meio

ctk.CTkButton(janela, text="logar".upper(), width=250, height=45).pack(pady=30) # em cima e em baixo

janela.mainloop() # inicializa a janela
