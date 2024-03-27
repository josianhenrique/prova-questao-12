import tkinter as tk

def mostrar_numeros():
    # Cria uma string para armazenar os números
    numeros_str = ""

    # Loop for para iterar sobre os números de 220 a 440
    for numero in range(220, 441):
        numeros_str += str(numero) + "\n"

    # Exibe os números na caixa de texto
    texto_numeros.configure(state='normal')
    texto_numeros.delete('1.0', tk.END)  # Limpa o texto atual
    texto_numeros.insert(tk.END, numeros_str)  # Insere os números
    texto_numeros.configure(state='disabled')

# Cria a janela principal
root = tk.Tk()
root.title("Números de 220 a 440")

# Cria uma caixa de texto para exibir os números
texto_numeros = tk.Text(root, width=20, height=15)
texto_numeros.pack()

# Cria um botão para mostrar os números
botao_mostrar = tk.Button(root, text="Mostrar Números", command=mostrar_numeros)
botao_mostrar.pack()

# Executa o loop principal da janela
root.mainloop()
