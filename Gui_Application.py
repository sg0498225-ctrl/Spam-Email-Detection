import tkinter as tk
from tkinter import *
import pickle

# load model (umm hope path works)
try:
    m = pickle.load(open("../model/spam_model.pkl","rb"))
    v = pickle.load(open("../model/vectorizer.pkl","rb"))
except:
    print("model load error?? check paths.")
    m = None; v = None


# main spam check thing
def _go():
    t = txt.get("1.0", END).strip()
    if t=="":
        res_lbl.config(text="no text..", fg="orange")
        return

    x = v.transform([t])   # vectorize
    pr = m.predict(x)[0]

    if pr==1:
        res_lbl.config(text=" spam ", fg="red")
    else:
        res_lbl.config(text=" ham ", fg="green")



# gui part.. nothing fancy
root = tk.Tk()
root.title("spam? checker")
root.geometry("350x360")

Label(root, text="check spam msg", font=("Arial",14)).pack(pady=5)

txt = Text(root, height=7, width=33)
txt.pack(pady=5)

Button(root, text=" run ", command=_go).pack(pady=4)

res_lbl = Label(root, text="", font=("Arial",13))
res_lbl.pack(pady=10)

root.mainloop()