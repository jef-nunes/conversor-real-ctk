import customtkinter as ctk
import sys
from tkinter import messagebox
from PIL import Image 
from pathlib import Path

# Listar paths de imagens a serem carregadas com PIL
path_imagens = ["./images/imagem_1.jpg"]

# Verificar se as imagens existem
for x in path_imagens:
    if not Path(x).exists():
        print(f"Erro: A imagem {x} não pode ser encontrada.")
        sys.exit(1)
        
# Carregar as imagens com PIL
pil_imagem_1 = Image.open(path_imagens[0])

# Converte o valor em real para dolar
# e exibe uma mensagem com o resultado
def converter_real():
    real_input = float(valor_real_entry.get())
    resultado = real_input * 0.17
    messagebox.showinfo("Real em Dólar",f"R${round(, 2)} equivalem a US${round(formula, 2)}")

# Criar e personalizar janela da aplicação
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.resizable(width=False,height=False)
janela.geometry("400x400")
janela.title("Converter Real")
if Path("./images/icone.ico").exists():
    janela.iconbitmap("./images/icone.ico")

# Criar e personalizar componentes
titulo_label = ctk.CTkLabel(master=janela,font=("verdana",24,"bold"),text="Converter Real")
imagem_1_image = ctk.CTkImage(light_image=pil_imagem_1,dark_image=pil_imagem_1,size=(200,200))
imagem_1_label = ctk.CTkLabel(master=janela,image=imagem_1_image,text="")
valor_real_label = ctk.CTkLabel(master=janela,text="Valor em R$",font=("verdana",18,"bold"))
valor_real_entry = ctk.CTkEntry(master=janela)
converter_button = ctk.CTkButton(master=janela,text="Converter",command=converter_real)

# Posicionar componentes
titulo_label.pack(padx=10,pady=10)
imagem_1_label.pack(padx=10,pady=10)
valor_real_label.pack(padx=10,pady=10)
valor_real_entry.pack(padx=10,pady=10)
converter_button.pack(padx=10,pady=10)

# Rodar
janela.mainloop()
