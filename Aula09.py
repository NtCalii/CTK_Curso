import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Option Menu (menu de opções)''' # aula 09

ctk.CTkLabel(janela, text="Escolha o seu mês de nascimento: ", font=("arial bold", 14)).pack() # apenas um texto

mes = ctk.CTkOptionMenu(janela, values=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
                                  "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]) # criar o menu
mes.pack()
mes.set("Opções") # coloca um texto ilustrativo no botão do menu

janela.mainloop() # inicializa a janela
