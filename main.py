import customtkinter as ctk


class Calculadora:

    def __init__(self, master):
        self.master = master
        self.frame = ctk.CTkFrame(self.master)

        self.expressao = str()
        self.expressao_ativa = bool()

        default_width = 80
        default_height = 60
        default_padx = 2
        default_pady = 2
        n_row = 0

        # Entrada
        self.entryResultado = ctk.CTkEntry(self.frame, justify="right", font=("Arial", 40))
        self.entryResultado.grid(columnspan=4, sticky="we", padx=10, pady=10)

        # Primeira Linha
        n_row += 1
        self.btnPorcentagem = ctk.CTkButton(self.frame, text="%", font=("Arial", 20), width=default_width, height=default_height, fg_color=("gray25"))
        self.btnPorcentagem.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnClearEntry = ctk.CTkButton(self.frame, text="CE", font=("Arial", 20), width=default_width, height=default_height)
        self.btnClearEntry.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnClear = ctk.CTkButton(self.frame, text="C", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.limpar())
        self.btnClear.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnDeletar = ctk.CTkButton(self.frame, text="←", font=("Arial", 20), width=default_width, height=default_height, fg_color="red", hover_color="red4")
        self.btnDeletar.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Segunda Linha
        n_row += 1
        self.btnDerivada = ctk.CTkButton(self.frame, text="1/x", font=("Arial", 20), width=default_width, height=default_height)
        self.btnDerivada.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnPotencia = ctk.CTkButton(self.frame, text="x²", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.potencia())
        self.btnPotencia.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnRaiz = ctk.CTkButton(self.frame, text="²√x", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.raiz())
        self.btnRaiz.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnDivisao = ctk.CTkButton(self.frame, text="/", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.operador("/"))
        self.btnDivisao.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Terceira Linha
        n_row += 1
        self.btnSete = ctk.CTkButton(self.frame, text="7", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("7"))
        self.btnSete.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnOito = ctk.CTkButton(self.frame, text="8", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("8"))
        self.btnOito.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnNove = ctk.CTkButton(self.frame, text="9", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("9"))
        self.btnNove.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnMultiplicar = ctk.CTkButton(self.frame, text="x", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.operador("*"))
        self.btnMultiplicar.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Quarta Linha
        n_row += 1
        self.btnQuatro = ctk.CTkButton(self.frame, text="4", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("4"))
        self.btnQuatro.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnCinco = ctk.CTkButton(self.frame, text="5", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("5"))
        self.btnCinco.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnSeis = ctk.CTkButton(self.frame, text="6", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("6"))
        self.btnSeis.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnSubtrair = ctk.CTkButton(self.frame, text="-", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.operador("-"))
        self.btnSubtrair.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Quinta Linha
        n_row += 1
        self.btnUm = ctk.CTkButton(self.frame, text="1", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("1"))
        self.btnUm.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnDois = ctk.CTkButton(self.frame, text="2", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("2"))
        self.btnDois.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnTres = ctk.CTkButton(self.frame, text="3", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("3"))
        self.btnTres.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnSomar = ctk.CTkButton(self.frame, text="+", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.operador("+"))
        self.btnSomar.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Sexta Linha
        n_row += 1
        self.btnInverter = ctk.CTkButton(self.frame, text="-/+", font=("Arial", 20), width=default_width, height=default_height)
        self.btnInverter.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnZero = ctk.CTkButton(self.frame, text="0", font=("Arial", 20), width=default_width, height=default_height, command=lambda: self.digitar("0"))
        self.btnZero.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnVirgula = ctk.CTkButton(self.frame, text=",", font=("Arial", 20), width=default_width, height=default_height)
        self.btnVirgula.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnCalcular = ctk.CTkButton(self.frame, text="=", font=("Arial", 20), width=default_width, height=default_height, command=self.calcular)
        self.btnCalcular.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        self.frame.pack()

    def digitar(self, num):
        if self.entryResultado._text == "0":
            return self.entryResultado.configure(text=num)
        
        if self.expressao_ativa:
            self.expressao_ativa = False
            return self.entryResultado.configure(text=num)
        
        return self.entryResultado.configure(text=self.entryResultado._text+num)

    def limpar(self): self.entryResultado.configure(text="0")

    def operador(self, metodo):
        self.expressao = self.entryResultado._text + metodo
        self.expressao_ativa = True

    def raiz(self): self.entryResultado.configure(text=int(self.entryResultado._text)**0.5)

    def potencia(self): self.entryResultado.configure(text=int(self.entryResultado._text)**2)

    def calcular(self):
        self.expressao += self.entryResultado._text
        self.entryResultado.configure(text=str(eval(self.expressao)))
        self.expressao = ""


def main():
    ctk.set_appearance_mode("dark")

    root = ctk.CTk()
    root.title("Calculadora 2.0")
    app = Calculadora(root)

    root.mainloop()

if __name__ == '__main__':
    main()
