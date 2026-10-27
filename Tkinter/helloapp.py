import tkinter as tk
from tkinter import ttk

class HelloApp:
    def __init__(self, raiz):
        raiz.title("Um simples olá!")
        self.label = ttk.Label(raiz, text="Clique no botao para dizer olá")
        self.label.pack(pady=20)

        self.texto_padrao = "Digite seu nome aqui"
        self.entrada = tk.Entry(raiz, fg="gray", width=30)
        self.entrada.insert(0, self.texto_padrao)
        self.entrada.pack(pady=20)
        self.entrada.bind("<FocusIn>", self.limpar)
        self.entrada.bind("<FocusOut>", self.restaurar)

        botao = tk.Button(raiz, text="clique aqui", command=self.clicado)
        botao.pack(pady=10)

    def clicado(self):
        self.label.config(text=f"Olá, {self.entrada.get()}!")

    def limpar(self, _):
            if self.entrada.get() == self.texto_padrao:
                self.entrada.delete(0, tk.END)
                self.entrada.config(fg="black")
    
    def restaurar(self, _):
        if not self.entrada.get():
            self.entrada.insert(0, self.texto_padrao)
            self.entrada.config(fg="gray")

if __name__ == "__main__":
    raiz = tk.Tk()
    HelloApp(raiz)
    raiz.mainloop()