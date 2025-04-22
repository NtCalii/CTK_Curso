import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Place (Posicionamento de Widgets na  Janela)''' # aula 20

ctk.CTkButton(janela, text="Botão 1").place(x=20, y=20) # eixo x horizontal e y vertical
ctk.CTkButton(janela, text="Botão 2").place(x=250, y=200) # mede em pixels
ctk.CTkButton(janela, text="Botão 3").place(relx=0.1, rely=0.2) # usa a relação da tela

janela.mainloop() # inicializa a janela
