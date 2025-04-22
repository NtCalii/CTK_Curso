import customtkinter as ctk # importar a biblioteca

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Slider''' # aula 14

def slider_value(value):
    value = int(value)   # função para mostrar o valor que o slider está
    print(value)

slider = ctk.CTkSlider(janela, from_=0, to=100, command=slider_value).pack() # para criar o slider

janela.mainloop() # inicializa a janela
