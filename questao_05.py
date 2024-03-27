import tkinter as tk
from tkinter import messagebox

def mostrar_mes_correspondente():
    # Obtém o número inserido pelo usuário
    numero = int(entry_numero.get())

    # Determina o mês correspondente usando match case
    mes = match numero:
        case 1:
            "Janeiro"
        case 2:
            "Fevereiro"
        case 3:
            "Março"
        case 4:
            "Abril"
        case 5:
            "Maio"
        case 6:
            "Junho"
        case 7:
            "Julho"
        case 8:
            "Agosto"
        case 9:
            "Setembro"
        case 10:
            "Outubro"
        case 11:
            "Novembro"
        case 12:
            "Dezembro"
        case _:
            "Número inválido"

    # Exibe o mês correspondente
    messagebox.showinfo("Mês Correspondente", f"O mês correspondente ao número {numero} é: {mes}")

# Cria a janela principal
root = tk.Tk()
root.title("Mês do Ano")

# Cria um rótulo e uma entrada para o número
label_numero = tk.Label(root, text="Digite um número de 1 a 12:")
label_numero.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

# Cria um botão para mostrar o mês correspondente
botao_mostrar = tk.Button(root, text="Mostrar Mês Correspondente", command=mostrar_mes_correspondente)
botao_mostrar.pack()

# Executa o loop principal da janela
root.mainloop()
