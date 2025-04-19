import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Dialog (caixa de dialogo)''' # aula 08

def abrir():
    dialog = ctk.CTkInputDialog(title="Caixa de dialogo.", text="Digite seu nome completo.") # função que cria a caixa

btn = ctk.CTkButton(janela, text="Abrir caixa de dialogo", command=abrir()) # botão para abrir a função
btn.pack()

janela.mainloop() # inicializa a janela
