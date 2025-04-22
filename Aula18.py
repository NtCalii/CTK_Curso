import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''RadioButton''' # aula 18

radio_var = ctk.IntVar(value=0)

def radio_event():
    print(radio_var.get())

btn1 = ctk.CTkRadioButton(janela, text="Masculino", command=radio_event, variable=radio_var, value=1)# criar o botão
btn1.pack()
btn2 = ctk.CTkRadioButton(janela, text="Feminino", command=radio_event, variable=radio_var, value=2) # criar o botão
btn2.pack()

janela.mainloop() # inicializa a janela
