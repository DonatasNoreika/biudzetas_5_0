import tkinter as tk
from biudzetas import Biudzetas


class PagrindinisLangas:
    def __init__(self, master):
        self.biudzetas = Biudzetas()
        self.master = master
        self.master.title("Biudžetas")
        self.master.geometry("420x400")
        self.master.config(padx=20, pady=20)
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text="Įvesti pajamas", command=self.atidaryti_pajamu_langa)
        self.button2 = tk.Button(self.frame, text="Įvesti išlaidas", command=self.atidaryti_islaidu_langa)
        self.button3 = tk.Button(self.frame, text="Ištrinti įrašą", command=self.gui_istrinti_irasa)
        self.zurnalas = tk.Listbox(self.frame, width=50)
        self.balansas_label = tk.Label(self.frame, text=f"Balansas: {self.biudzetas.gauti_balansa()}")
        self.balansas_label.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.zurnalas.pack(pady=20)
        self.zurnalas.insert(tk.END, *self.biudzetas.zurnalas)
        self.frame.pack()

    def atidaryti_pajamu_langa(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = PajamuLangas(self.newWindow, self.biudzetas, self)

    def atidaryti_islaidu_langa(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = IslaiduLangas(self.newWindow, self.biudzetas, self)

    def update_zurnalas_balansas(self):
        self.zurnalas.delete(0, tk.END)
        self.zurnalas.insert(tk.END, *self.biudzetas.zurnalas)
        self.balansas_label['text'] = f"Balansas: {self.biudzetas.gauti_balansa()}"

    def gui_istrinti_irasa(self):
        indeksas = self.zurnalas.curselection()[0]
        self.biudzetas.istrinti_irasa(indeksas)
        self.update_zurnalas_balansas()


class PajamuLangas:
    def __init__(self, master, biudzetas, pagrindinis_langas):
        self.pagrindinis_langas = pagrindinis_langas
        self.master = master
        self.biudzetas = biudzetas
        self.master.title("Biudžetas: įvesti pajamas")
        self.master.geometry("320x150")
        self.master.config(padx=20, pady=20)
        self.suma_label = tk.Label(self.master, text="Suma")
        self.suma_entry = tk.Entry(self.master)
        self.siuntejas_label = tk.Label(self.master, text="Siuntejas")
        self.siuntejas_entry = tk.Entry(self.master)
        self.info_label = tk.Label(self.master, text="Papildoma informacija")
        self.info_entry = tk.Entry(self.master)
        self.ivesti_button = tk.Button(self.master, text="Įvesti", command=self.gui_ivesti_pajamas)
        self.suma_label.grid(row=0, column=0)
        self.suma_entry.grid(row=0, column=1)
        self.siuntejas_label.grid(row=1, column=0)
        self.siuntejas_entry.grid(row=1, column=1)
        self.info_label.grid(row=2, column=0)
        self.info_entry.grid(row=2, column=1)
        self.ivesti_button.grid(row=3, columnspan=2)

    def gui_ivesti_pajamas(self):
        suma = float(self.suma_entry.get())
        siuntejas = self.siuntejas_entry.get()
        info = self.info_entry.get()
        self.biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
        self.pagrindinis_langas.update_zurnalas_balansas()
        self.master.destroy()


class IslaiduLangas:
    def __init__(self, master, biudzetas, pagrindinis_langas):
        self.pagrindinis_langas = pagrindinis_langas
        self.master = master
        self.biudzetas = biudzetas
        self.master.title("Biudžetas: įvesti išlaidas")
        self.master.geometry("320x150")
        self.master.config(padx=20, pady=20)
        self.suma_label = tk.Label(self.master, text="Suma")
        self.suma_entry = tk.Entry(self.master)
        self.budas_label = tk.Label(self.master, text="Mokėjimo būdas")
        self.budas_entry = tk.Entry(self.master)
        self.isigyta_label = tk.Label(self.master, text="Įsigyta prekė/paslauga")
        self.isigyta_entry = tk.Entry(self.master)
        self.info_label = tk.Label(self.master, text="Papildoma informacija")
        self.info_entry = tk.Entry(self.master)
        self.ivesti_button = tk.Button(self.master, text="Įvesti", command=self.gui_ivesti_islaidas)
        self.suma_label.grid(row=0, column=0)
        self.suma_entry.grid(row=0, column=1)
        self.budas_label.grid(row=1, column=0)
        self.budas_entry.grid(row=1, column=1)
        self.isigyta_label.grid(row=2, column=0)
        self.isigyta_entry.grid(row=2, column=1)
        self.info_label.grid(row=3, column=0)
        self.info_entry.grid(row=3, column=1)
        self.ivesti_button.grid(row=4, columnspan=2)

    def gui_ivesti_islaidas(self):
        suma = float(self.suma_entry.get())
        budas = self.budas_entry.get()
        isigyta = self.isigyta_entry.get()
        info = self.info_entry.get()
        self.biudzetas.prideti_islaidu_irasa(suma, budas, isigyta, info)
        self.pagrindinis_langas.update_zurnalas_balansas()
        self.master.destroy()


def main():
    langas = tk.Tk()
    app = PagrindinisLangas(langas)
    langas.mainloop()


if __name__ == "__main__":
    main()
