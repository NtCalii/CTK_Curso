import customtkinter as ctk # importar a biblioteca
from PIL import Image # precisa importar o image do pil

janela = ctk.CTk() # cria a janela

'''Configurando a janela principal''' # aula 02

janela.title("App Teste") # muda o titulo da janela
janela.geometry("700x400") # dimensão inicial
janela.maxsize(width=700, height=400) # tamanho max
janela.minsize(width=700, height=400) # tamanho min
janela.resizable(width=False, height=False) # bloquear a mudanças de dimensão do usuário

'''Imagens''' # aula 13

img1 = ctk.CTkImage(light_image=Image.open("./Eldrin.jpg"), dark_image=Image.open("./Eldrin.jpg"),
                    size=(250, 250)) # para criar a variável da imagem

ctk.CTkLabel(janela, text=None, image=img1).pack() # colocando a imagem na tela

janela.mainloop() # inicializa a janela
