import tkinter as tk
from tkinter import messagebox

def mostrar_dia_semana():
    # Obtém o número inserido pelo usuário
    numero = int(entry_numero.get())

    # Determina o dia da semana correspondente
    if numero == 1:
        dia_semana = "Domingo"
    elif numero == 2:
        dia_semana = "Segunda-feira"
    elif numero == 3:
        dia_semana = "Terça-feira"
    elif numero == 4:
        dia_semana = "Quarta-feira"
    elif numero == 5:
        dia_semana = "Quinta-feira"
    elif numero == 6:
        dia_semana = "Sexta-feira"
    elif numero == 7:
        dia_semana = "Sábado"
    else:
        messagebox.showerror("Erro", "Número inválido. Por favor, insira um número de 1 a 7.")
        return

    # Exibe o dia da semana correspondente
    messagebox.showinfo("Dia da Semana", f"O dia da semana correspondente ao número {numero} é: {dia_semana}")

# Cria a janela principal
root = tk.Tk()
root.title("Dia da Semana")

# Cria um rótulo e uma entrada para o número
label_numero = tk.Label(root, text="Digite um número de 1 a 7:")
label_numero.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

# Cria um botão para mostrar o dia da semana correspondente
botao_mostrar = tk.Button(root, text="Mostrar Dia da Semana", command=mostrar_dia_semana)
botao_mostrar.pack()

# Executa o loop principal da janela
root.mainloop()
