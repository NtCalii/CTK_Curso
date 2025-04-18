import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Customizando o tema''' # aula 03

janela._set_appearance_mode("dark") # muda o tema da janela

'''Criando nova janela''' # aula 04

def nova_janela(): # função para criar nova janela
    nova_janela = ctk.CTkToplevel(janela) # cria a nova janela
    nova_janela.geometry("200x200")

bnt_nova_janela = ctk.CTkButton(master=janela, text="Abrir nova janela", command=nova_janela()).place(x=300, y=100)

janela.mainloop() # inicializa a janela
