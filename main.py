import tkinter as tk


def add_fild():


    print('press button')

window = tk.Tk()


x, y = 0, 0

entry = tk.Entry()
entry.grid(column=0, row=x)

btn = tk.Button(text='button', command=add_fild)
btn.grid(column=0, row=x+1)


window.mainloop()

