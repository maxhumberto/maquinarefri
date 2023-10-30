import tkinter as tk
from tkinter import simpledialog, messagebox

class MaquinaDeRefrigeranteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Refrigerante")

        self.estado = "AGUARDANDO_MOEDAS"
        self.valor_inserido = 0.0
        self.preco_refrigerante = 0.0
        self.refrigerante_escolhido = ""

        self.criar_interface()

    def criar_interface(self):
        self.label_estado = tk.Label(self.root, text="Estado: AGUARDANDO MOEDAS")
        self.label_estado.pack()

        self.botao_moedas = tk.Button(self.root, text="Inserir Moedas", command=self.inserir_moedas)
        self.botao_moedas.pack()

        self.botao_escolher_refrigerante = tk.Button(self.root, text="Escolher Refrigerante", command=self.escolher_refrigerante)
        self.botao_escolher_refrigerante.pack()

        self.botao_entregar_refrigerante = tk.Button(self.root, text="Entregar Refrigerante", command=self.entregar_refrigerante)
        self.botao_entregar_refrigerante.pack()

        self.label_inserido = tk.Label(self.root, text="Valor Inserido: 0.0")
        self.label_inserido.pack()

    def inserir_moedas(self):
        if self.estado == "AGUARDANDO_MOEDAS":
            valor_moeda = simpledialog.askfloat("Inserir Moeda", "Insira o valor da moeda (0.25, 0.50 ou 1.00):")
            if valor_moeda is not None:
                if valor_moeda in [0.25, 0.50, 1.00]:
                    self.valor_inserido += valor_moeda
                    self.atualizar_interface()
                else:
                    messagebox.showerror("Erro", "Moeda não aceita. Insira 0.25, 0.50 ou 1.00.")

    def escolher_refrigerante(self):
        if self.estado == "ESCOLHA_DE_REFRIGERANTE":
            escolha = simpledialog.askstring("Escolher Refrigerante", "Escolha um refrigerante (Fanta Uva, Fanta Laranja, Sprite, Coca-Cola, Coca Zero):")
            if escolha is not None:
                if escolha in ["Fanta Uva", "Fanta Laranja", "Sprite", "Coca-Cola", "Coca Zero"]:
                    self.refrigerante_escolhido = escolha

    def entregar_refrigerante(self):
        if self.estado == "ENTREGA_DE_REFRIGERANTE":
            if self.refrigerante_escolhido:
                messagebox.showinfo("Entrega", f"Entregando {self.refrigerante_escolhido}")
                troco = self.valor_inserido - self.preco_refrigerante
                if troco > 0:
                    messagebox.showinfo("Troco", f"Entregando troco de {troco:.2f} reais.")
                self.estado = "AGUARDANDO_MOEDAS"
                self.preco_refrigerante = 0.0
                self.refrigerante_escolhido = ""
                self.atualizar_interface()

    def atualizar_interface(self):
        self.label_inserido.config(text=f"Valor Inserido: {self.valor_inserido:.2f}")
        self.label_estado.config(text=f"Estado: {self.estado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MaquinaDeRefrigeranteGUI(root)
    root.mainloop()