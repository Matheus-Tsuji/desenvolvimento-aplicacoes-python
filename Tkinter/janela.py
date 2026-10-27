from pathlib import Path
from tkinter import Tk

janela = Tk()
janela.title("Nós amamos python!")
icone = Path(__file__).with_name("icon.ico")

if icone.exists():
    janela.iconbitmap(str(icone)) # Exemplo para Windows

width = 600
height = 300
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))

janela.geometry('%dx%d+%d+%d' % (width, height, x, y))
janela.mainloop()