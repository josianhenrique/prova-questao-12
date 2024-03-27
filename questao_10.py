import tkinter as tk

def exibir_lista():
    # Obtém os elementos da lista e os exibe na caixa de texto
    for linguagem in lista_demo:
        texto_lista.insert(tk.END, linguagem + "\n")

# Lista de demonstração
lista_demo = ["Java", "Python", "C#"]

# Cria a janela principal
root = tk.Tk()
root.title("Exibição de Lista")

# Cria uma caixa de texto para exibir os elementos da lista
texto_lista = tk.Text(root, width=20, height=5)
texto_lista.pack()

# Chama a função para exibir a lista ao iniciar o programa
exibir_lista()

# Executa o loop principal da janela
root.mainloop()
