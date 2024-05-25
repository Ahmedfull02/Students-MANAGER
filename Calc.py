# import of libraries
import tkinter as tk

from tkinter import ttk

from feet_meter import calc


#Functions section 
def calc():
    
    

# Window , Frame declaration

root = tk.Tk()
root.title("Scientific calculator")
# root.geometry("400x600")

#Frame = ttk.Frame(root,padding="10 10 20 20")

# Calc Screen

screen = tk.Label(text='screen').grid(row=0,column=0,columnspan=5,pady=5)

# Button : Numbers and operation

for i in range(1,4):
    for j in range(1,4):
        tk.Button(text=i*j,width=5).grid(row=i,column=j,padx=5,pady=5)
    
button_mul = tk.Button(text="x",width=5).grid(row=1,column=4,padx=10,pady=5)
button_sos = tk.Button(text="-",width=5).grid(row=2,column=4,padx=10,pady=5)
button_sum = tk.Button(text="+",width=5).grid(row=3,column=4,padx=10,pady=5)
button_div = tk.Button(text="/",width=5).grid(row=4,column=4,padx=10,pady=5)
button_sqrt = tk.Button(text="sqrt",width=5).grid(row=4,column=1,padx=5,pady=5)
button_equa = tk.Button(text="=",width=5,command=calc).grid(row=4,column=4,padx=5,pady=5)



root.mainloop()