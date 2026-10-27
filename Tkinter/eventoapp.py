import tkinter as tk
from tkinter import ttk

class EventoApp:
    def __init__(self, raiz):
        raiz.title("Evento de botão")
        self.label = ttk.Label(raiz, text="Olá, Tkinter!")
        self.label.pack(pady=10)
        botao = ttk.Button(raiz, text="Clique em mim", command=self.clicado)
        botao.pack(pady=10)

    def clicado(self):
        self.label.config(text="botao clicado!")

if __name__ == "__main__":
    raiz = tk.Tk()
    EventoApp(raiz)
    raiz.mainloop()