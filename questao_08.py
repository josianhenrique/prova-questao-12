import tkinter as tk

class Carro:
    def __init__(self, nome="", marca=""):
        self.__nome = nome
        self.__marca = marca

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

def exibir_carro():
    # Obtém os valores inseridos pelo usuário
    nome = entry_nome.get()
    marca = entry_marca.get()

    # Cria um objeto da classe Carro com os valores inseridos
    carro = Carro(nome, marca)

    # Exibe o nome e a marca do carro na caixa de texto
    texto_carro.configure(state='normal')
    texto_carro.delete('1.0', tk.END)  # Limpa o texto atual
    texto_carro.insert(tk.END, f"Nome: {carro.get_nome()}\nMarca: {carro.get_marca()}")  # Insere nome e marca
    texto_carro.configure(state='disabled')

# Cria a janela principal
root = tk.Tk()
root.title("Informações do Carro")

# Cria rótulos e entradas para o nome e a marca do carro
label_nome = tk.Label(root, text="Nome do Carro:")
label_nome.grid(row=0, column=0, padx=5, pady=5)

entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_marca = tk.Label(root, text="Marca do Carro:")
label_marca.grid(row=1, column=0, padx=5, pady=5)

entry_marca = tk.Entry(root)
entry_marca.grid(row=1, column=1, padx=5, pady=5)

# Cria um botão para exibir as informações do carro
botao_exibir = tk.Button(root, text="Exibir Carro", command=exibir_carro)
botao_exibir.grid(row=2, columnspan=2, padx=5, pady=5)

# Cria uma caixa de texto para exibir as informações do carro
texto_carro = tk.Text(root, width=30, height=5)
texto_carro.grid(row=3, columnspan=2, padx=5, pady=5)
texto_carro.configure(state='disabled')

# Cria uma instância da classe Carro com valores padrão
carro_padrao = Carro("Fusca", "Volkswagen")
entry_nome.insert(0, carro_padrao.get_nome())  # Insere o nome padrão na entrada
entry_marca.insert(0, carro_padrao.get_marca())  # Insere a marca padrão na entrada

# Executa o loop principal da janela
root.mainloop()
