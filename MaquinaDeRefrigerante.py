class MaquinaDeRefrigerante:
    def __init__(self):
        self.estado = "AGUARDANDO_MOEDAS"
        self.valor_inserido = 0.0
        self.preco_refrigerante = 0.0
        self.refrigerante_escolhido = ""

    def iniciar(self):
        while self.estado != "ENTREGA_DE_REFRIGERANTE":
            if self.estado == "AGUARDANDO_MOEDAS":
                print("Insira moedas de 0.25, 0.50 ou 1.00 (0 para encerrar): ")
                entrada = input()
                if entrada == "0":
                    self.estado = "ESCOLHA_DE_REFRIGERANTE"
                else:
                    moeda = entrada.replace(',', '.')
                    try:
                        moeda = float(moeda)
                        if moeda in [0.25, 0.50, 1.00]:
                            self.valor_inserido += moeda
                        else:
                            print("Moeda não aceita.")
                    except ValueError:
                        print("Entrada inválida. Use números válidos ou 0 para encerrar.")

            elif self.estado == "ESCOLHA_DE_REFRIGERANTE":
                print("Escolha um refrigerante (Fanta Uva, Fanta Laranja, Sprite, Coca-Cola, Coca Zero): ")
                self.refrigerante_escolhido = input()
                if self.refrigerante_escolhido not in ["Fanta Uva", "Fanta Laranja", "Sprite", "Coca-Cola", "Coca Zero"]:
                    print("Refrigerante não disponível.")
                else:
                    # Defina o preço com base na escolha do refrigerante
                    if self.refrigerante_escolhido == "Fanta Uva":
                        self.preco_refrigerante = 2.00
                    elif self.refrigerante_escolhido == "Fanta Laranja":
                        self.preco_refrigerante = 2.50
                    elif self.refrigerante_escolhido == "Sprite":
                        self.preco_refrigerante = 3.00
                    elif self.refrigerante_escolhido == "Coca-Cola":
                        self.preco_refrigerante = 3.50
                    elif self.refrigerante_escolhido == "Coca Zero":
                        self.preco_refrigerante = 5.00

                    if self.valor_inserido >= self.preco_refrigerante:
                        self.entregar_refrigerante()
                    else:
                        print("Valor insuficiente. Insira mais moedas.")

            elif self.estado == "ENTREGA_DE_REFRIGERANTE":
                if self.refrigerante_escolhido:
                    print(f"Entregando {self.refrigerante_escolhido}")
                    troco = self.valor_inserido - self.preco_refrigerante
                    if troco > 0:
                        print(f"Entregando troco de {troco:.2f} reais.")
                    # Reinicie a máquina para uma nova compra
                    self.estado = "AGUARDANDO_MOEDAS"
                    self.preco_refrigerante = 0.0
                    self.refrigerante_escolhido = ""

        print("Obrigado por usar a máquina de refrigerante!")

    def entregar_refrigerante(self):
        self.estado = "ENTREGA_DE_REFRIGERANTE"  # Defina o estado como "ENTREGA_DE_REFRIGERANTE"
        if self.refrigerante_escolhido:
            print(f"Entregando {self.refrigerante_escolhido}")
            troco = self.valor_inserido - self.preco_refrigerante
            if troco > 0:
                print(f"Entregando troco de {troco:.2f} reais.")
            # Não é mais necessário reiniciar a máquina aqui

if __name__ == "__main__":
    maquina = MaquinaDeRefrigerante()
    maquina.iniciar()
