import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Switch (botão liga e desliga)''' # aula 16

switch_var = ctk.StringVar(value="on")

def event():
    if switch_var.get() == "Ativado":
        ctk.set_appearance_mode("Light")     # para mudar o modo da aplicação
    elif switch_var.get() == "Desativado":
        ctk.set_appearance_mode("Dark")
    else:
        ctk.set_appearance_mode("System")

btn = ctk.CTkSwitch(janela, text="Tema", variable=switch_var, command=event, onvalue="Ativado",
                    offvalue="Desativado").pack() # para criar o botão

janela.mainloop() # inicializa a janela
