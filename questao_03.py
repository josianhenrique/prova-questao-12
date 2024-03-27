import tkinter as tk
from tkinter import messagebox

def ler_e_mostrar_valores():
    # Tenta ler as variáveis do arquivo
    try:
        with open("config.txt", "r") as arquivo:
            nome_maquina = arquivo.readline().strip()
            tempo_uso = int(arquivo.readline().strip())
            ligado = arquivo.readline().strip().lower() == "true"  # Converte para booleano
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado")
        return
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido para tempo de uso")
        return

    # Exibe os valores e seus tipos
    mensagem = (f"Nome da Máquina: {nome_maquina}\nTipo: {type(nome_maquina)}\n"
                f"Tempo de Uso: {tempo_uso}\nTipo: {type(tempo_uso)}\n"
                f"Ligado: {ligado}\nTipo: {type(ligado)}")
    messagebox.showinfo("Valores e Tipos", mensagem)

# Cria a janela principal
root = tk.Tk()
root.title("Leitura de Valores")

# Cria um botão para ler e mostrar os valores
botao_mostrar = tk.Button(root, text="Mostrar Valores e Tipos", command=ler_e_mostrar_valores)
botao_mostrar.pack()

# Executa o loop principal da janela
root.mainloop()

