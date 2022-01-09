from Crypto.Cipher import AES
from secrets import token_bytes
from tkinter import *
import threading
screen = Tk()
screen.geometry("500x450")
screen.title("Enkriptimi AES")


mesazhi = StringVar()
llojiEnc = StringVar()

Label(text = "Enkriptimi Me AES", bg="lightblue", width="300", height="2", font = ("Arial", 15)).pack()
Label(text = "").pack()
Label(text = "Zgjedhni njërin opsion për enkriptim: ").pack()
Radiobutton(screen, text="128 bit", variable = llojiEnc,  value=16).pack()
Radiobutton(screen, text="192 bit", variable = llojiEnc, value=24).pack()
Radiobutton(screen, text="256 bit", variable = llojiEnc, value=32).pack()
Label(text = "Mesazhi: ").pack()
Entry(textvariable = mesazhi).pack()
Label(text = "").pack()
