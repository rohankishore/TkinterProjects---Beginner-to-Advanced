from customtkinter import *
from tkinter import messagebox

r = CTk()
r.geometry("800x600")

CTkLabel(r, text="SIGN UP", text_font=("Zona Pro", 18)).pack(ipady=15)

CTkLabel(r, text="Email:", text_font=("Zona Pro", 12)).place(x=15, y=70)
CTkEntry(r, text_font="Zona", width=450).place(x=200, y=70)

CTkLabel(r, text="Username:", text_font=("Zona Pro", 12)).place(x=15, y=140)
CTkEntry(r, text_font="Zona", width=450).place(x=200, y=140)

CTkLabel(r, text="Mobile:", text_font=("Zona Pro", 12)).place(x=15, y=210)
CTkEntry(r, text_font="Zona", width=450).place(x=200, y=210)

CTkLabel(r, text="Password:", text_font=("Zona Pro", 12)).place(x=15, y=280)
CTkEntry(r, text_font="Zona", width=450).place(x=200, y=280)

CTkLabel(r, text="Confirm Password:", text_font=("Zona Pro", 12)).place(x=15, y=350)
CTkEntry(r, text_font="Zona", width=450).place(x=200, y=350)

def get():
    messagebox.showinfo(title="success!", message="User successfully registered.")

CTkLabel(r, text="Gender:", text_font=("Zona Pro", 12)).place(x=15, y=420)
CTkCheckBox(r, text="Male", text_font="Zona").place(x=240, y=420)
CTkCheckBox(r, text="Female", text_font="Zona").place(x=420, y=420)

CTkButton(r, text="Sign Up", text_font="Zona", command=get).place(x=330, y=510)


r.mainloop()
