import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal'''

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário
janela.iconify() # fecha a janela
janela.deiconify() # abre a janela

janela.mainloop() # inicializa a janela
