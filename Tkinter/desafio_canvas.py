import tkinter as tk
from tkinter import messagebox
import random

class DesafioCanvas:
    def __init__(self, raiz):
        self.cores = ["red", "blue", "pink", "green", "purple", "yellow", "white", "black", "gray", "cyan"]

        self.canvas = tk.Canvas(raiz, width=240, height=120)
        self.retangulo = self.canvas.create_rectangle(60, 20, 180, 100, fill="blue")
        self.canvas.pack(pady=10)
        tk.Button(raiz, text="Mudar de Cor", command=self.mudar_cor).pack()
        tk.Button(raiz, text="Avisar", command=self.avisar).pack()

    def mudar_cor(self):
        self.canvas.itemconfig(self.retangulo, fill=random.choice(self.cores))

    def avisar(self):
        messagebox.showinfo("Aviso", "isso é um aviso")


if __name__ == "__main__":
    raiz = tk.Tk()
    DesafioCanvas(raiz)
    raiz.mainloop()