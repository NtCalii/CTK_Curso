import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''TextBox (caixa de texto)''' # aula 07

texto = ctk.CTkTextbox(janela, width=300, height=350, scrollbar_button_color="blue") # criando a caixa de texto
texto.pack()
texto.insert("0.0", "Titulo\n\n" + "Ola dev, estou treinando interfaces gráficas.\n\n"*20) # colocando conteúdo

janela.mainloop() # inicializa a janela
