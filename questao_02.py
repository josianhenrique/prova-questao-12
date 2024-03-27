import tkinter as tk
from tkinter import messagebox

def imprimir_nome_maiusculo():
    nome = entry_nome.get()  # Obtém o nome inserido pelo usuário
    nome_maiusculo = nome.upper()  # Converte o nome para maiúsculas
    messagebox.showinfo("Nome em Maiúsculas", f"Nome em maiúsculas: {nome_maiusculo}")  # Exibe o nome em maiúsculas

# Cria a janela principal
root = tk.Tk()
root.title("Converter para Maiúsculas")

# Cria um rótulo e uma entrada para o nome
label_nome = tk.Label(root, text="Digite o nome da pessoa:")
label_nome.pack()

entry_nome = tk.Entry(root)
entry_nome.pack()

# Cria um botão para converter o nome para maiúsculas
botao_converter = tk.Button(root, text="Converter para Maiúsculas", command=imprimir_nome_maiusculo)
botao_converter.pack()

# Executa o loop principal da janela
root.mainloop()


