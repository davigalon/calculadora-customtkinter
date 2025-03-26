import customtkinter as ctk
from math import isclose
import PIL

class Calculadora:

    def __init__(self, master):
        self.master = master
        
        image = PIL.Image.open("image.png")
        background_image = ctk.CTkImage(image, size=(1920, 1080))
        self.background = ctk.CTkLabel(self.master, text="", image=background_image)
        self.background.place(x=0, y=0)

        self.frame = ctk.CTkFrame(self.master)
        self.varVisor = ctk.StringVar(value="0")
        self.expressao = str()
        self.expressao_ativa = bool()

        default_width = 80
        default_height = 60
        default_padx = 2
        default_pady = 2
        n_row = 0

        # Entrada
        self.entryVisor = ctk.CTkEntry(self.frame, textvariable=self.varVisor, justify="right", font=("Arial", 40))
        self.entryVisor.grid(row=n_row, columnspan=4, sticky="we", padx=10, pady=10)

        n_row += 1
        self.mframe = ctk.CTkFrame(self.frame)

        self.btnMC = ctk.CTkButton(self.mframe, text="MC", font=("Arial", 14), width=60, height=40, fg_color="transparent")
        self.btnMC.grid(row=0, column=0, padx=default_padx, pady=default_pady)

        self.btnMR = ctk.CTkButton(self.mframe, text="MR", font=("Arial", 14), width=60, height=40, fg_color="transparent")
        self.btnMR.grid(row=0, column=1, padx=default_padx, pady=default_pady)

        self.btnM1 = ctk.CTkButton(self.mframe, text="M+", font=("Arial", 14), width=60, height=40, fg_color="transparent")
        self.btnM1.grid(row=0, column=2, padx=default_padx, pady=default_pady)

        self.btnM2 = ctk.CTkButton(self.mframe, text="M-", font=("Arial", 14), width=60, height=40, fg_color="transparent")
        self.btnM2.grid(row=0, column=3, padx=default_padx, pady=default_pady)

        self.btnMS = ctk.CTkButton(self.mframe, text="MS", font=("Arial", 14), width=60, height=40, fg_color="transparent")
        self.btnMS.grid(row=0, column=4, padx=default_padx, pady=default_pady)

        self.mframe.grid(row=n_row, column=0, columnspan=5, pady=5)

        # Primeira Linha
        n_row += 1
        self.btnPorcentagem = ctk.CTkButton(self.frame, text="%", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25")
        self.btnPorcentagem.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnClearEntry = ctk.CTkButton(self.frame, text="CE", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25")
        self.btnClearEntry.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnClear = ctk.CTkButton(self.frame, text="C", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.limpar())
        self.btnClear.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnDeletar = ctk.CTkButton(self.frame, text="←", font=("Arial", 20), width=default_width, height=default_height, fg_color="red", hover_color="red4", command=self.deletar)
        self.btnDeletar.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Segunda Linha
        n_row += 1
        self.btnDerivada = ctk.CTkButton(self.frame, text="1/x", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25")
        self.btnDerivada.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnPotencia = ctk.CTkButton(self.frame, text="x²", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.potencia())
        self.btnPotencia.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnRaiz = ctk.CTkButton(self.frame, text="²√x", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.raiz())
        self.btnRaiz.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnDivisao = ctk.CTkButton(self.frame, text="/", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.operador("/"))
        self.btnDivisao.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Terceira Linha
        n_row += 1
        self.btnSete = ctk.CTkButton(self.frame, text="7", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("7"))
        self.btnSete.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnOito = ctk.CTkButton(self.frame, text="8", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("8"))
        self.btnOito.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnNove = ctk.CTkButton(self.frame, text="9", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("9"))
        self.btnNove.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnMultiplicar = ctk.CTkButton(self.frame, text="x", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.operador("*"))
        self.btnMultiplicar.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Quarta Linha
        n_row += 1
        self.btnQuatro = ctk.CTkButton(self.frame, text="4", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("4"))
        self.btnQuatro.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnCinco = ctk.CTkButton(self.frame, text="5", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("5"))
        self.btnCinco.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnSeis = ctk.CTkButton(self.frame, text="6", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("6"))
        self.btnSeis.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnSubtrair = ctk.CTkButton(self.frame, text="-", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.operador("-"))
        self.btnSubtrair.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Quinta Linha
        n_row += 1
        self.btnUm = ctk.CTkButton(self.frame, text="1", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("1"))
        self.btnUm.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnDois = ctk.CTkButton(self.frame, text="2", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("2"))
        self.btnDois.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnTres = ctk.CTkButton(self.frame, text="3", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("3"))
        self.btnTres.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnSomar = ctk.CTkButton(self.frame, text="+", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.operador("+"))
        self.btnSomar.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        # Sexta Linha
        n_row += 1
        self.btnInverter = ctk.CTkButton(self.frame, text="-/+", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=self.inverter)
        self.btnInverter.grid(row=n_row, column=0, padx=default_padx, pady=default_pady)

        self.btnZero = ctk.CTkButton(self.frame, text="0", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("0"))
        self.btnZero.grid(row=n_row, column=1, padx=default_padx, pady=default_pady)

        self.btnVirgula = ctk.CTkButton(self.frame, text=",", font=("Arial", 20), width=default_width, height=default_height, fg_color="gray25", command=lambda: self.digitar("."))
        self.btnVirgula.grid(row=n_row, column=2, padx=default_padx, pady=default_pady)

        self.btnCalcular = ctk.CTkButton(self.frame, text="=", font=("Arial", 20), width=default_width, height=default_height, command=self.calcular)
        self.btnCalcular.grid(row=n_row, column=3, padx=default_padx, pady=default_pady)

        self.frame.pack()

    def deletar(self):
        if len(self.varVisor.get()) == 1:
            return self.varVisor.set("0")
        self.varVisor.set(
            self.varVisor.get()[0:-1]
        )

    def formatar(self, num):
        if num % 1 == 0:
            return int(num)
        
        if isclose(num, round(num, 1)):
            if round(num, 1) % 1 == 0: return int(round(num))
            return round(num, 1)

        return num

    def digitar(self, valor):
        if self.varVisor.get() == "0":
            return self.varVisor.set(valor)
        
        if self.expressao_ativa:
            self.expressao_ativa = False
            return self.varVisor.set(valor)
        
        return self.varVisor.set(self.varVisor.get()+valor)

    def limpar(self): self.varVisor.set("0")

    def operador(self, metodo):
        self.expressao = self.varVisor.get() + metodo
        self.expressao_ativa = True

    def calcular(self):
        self.expressao += self.varVisor.get()
        self.varVisor.set(
            self.formatar(eval(self.expressao))
        )
        self.expressao = ""

    def raiz(self):
        self.varVisor.set(
            self.formatar(
                float(self.varVisor.get())**0.5
            )    
        )

    def potencia(self): 
        self.varVisor.set(
            self.formatar(
                float(self.varVisor.get())**2
            )    
        )

    def inverter(self):
        self.varVisor.set(
            self.formatar(
                float(self.varVisor.get()) * -1
            )
        )


def main():
    ctk.set_appearance_mode("dark")

    root = ctk.CTk()
    root.title("Calculadora 2.0")
    app = Calculadora(root)

    root.mainloop()

if __name__ == '__main__':
    main()
