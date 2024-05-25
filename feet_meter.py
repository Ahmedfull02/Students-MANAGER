import tkinter as tk
from tkinter import StringVar, ttk


def calc():
    f = entry_feet.get()
    f = float(f)
    meter.set((int(0.3048 * f* 10000.0 + 0.5)/10000.0))

#declare the window   
root = tk.Tk()
root.title("feet to meter")

entry_feet = tk.Entry(root,width=15)

label_feet = tk.Label(text="feet")

label_equivalent = tk.Label(text="is equivalent to")

label_meter = tk.Label(text="meter")

meter = StringVar()
label_res = tk.Label(textvariable=meter)

label_feet = tk.Label(text="feet")
button_res = tk.Button(text="Calculate",command=calc)

entry_feet.grid(column=2,row=1,padx=5,pady=5)
label_feet.grid(column=3,row=1,padx=5,pady=5)
label_meter.grid(row=2,column=3,padx=5,pady=5)
label_res.grid(row=2,column=2,padx=5,pady=5)
label_equivalent.grid(row=2,column=1,padx=5,pady=5)
button_res.grid(row=3,column=3,padx=5,pady=5)




root.mainloop()

