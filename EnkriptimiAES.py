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


plain = StringVar()
plain.set("")
cipher = StringVar()
cipher.set("")

def selected():
    return llojiEnc.get()

def put():

    key = token_bytes(int(selected()))


    def encrypt(msg):
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(msg.encode("ascii"))
        return nonce, ciphertext, tag

    
    def decrypt(nonce, ciphertext, tag):
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)
        try:
            cipher.verify(tag)
            return plaintext.decode('ascii')
        except:
            return False

    nonce, ciphertext, tag = encrypt(mesazhi.get())
    plaintext = decrypt(nonce, ciphertext, tag)

    cipher.set(f'Mesazhi i enkriptuar: {ciphertext}')
    if not plaintext:
        plain.set("Mesazhi eshte bosh!")
    else:
        plain.set(f'Mesazhi i dekriptuar: {plaintext}')

Button(text = "Enkripto", height="1", justify="center" , width = "10", command = put).pack()
Label(screen, textvariable=plain).pack()
Label(screen, textvariable=cipher).pack()
screen.mainloop()
