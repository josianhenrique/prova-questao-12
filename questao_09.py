import tkinter as tk

# Tupla de demonstração
tupla_demo = ("eu", "tu", "ele")

# Função para exibir os elementos da tupla na caixa de texto
def exibir_tupla():
    for elemento in tupla_demo:
        texto_tupla.insert(tk.END, elemento + "\n")

# Cria a janela principal
root = tk.Tk()
root.title("Exibição de Tupla")

# Cria uma caixa de texto para exibir os elementos da tupla
texto_tupla = tk.Text(root, width=20, height=5)
texto_tupla.pack()

# Chama a função para exibir a tupla ao iniciar o programa
exibir_tupla()

# Executa o loop principal da janela
root.mainloop()
