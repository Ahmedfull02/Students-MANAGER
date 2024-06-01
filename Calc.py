# import of libraries

import tkinter as tk
from tkinter import ttk
import operator

import math






#Functions section 

# Fonction du calcul
def get_button(oper) :
    curr = expression_field.get()
    expression_field.delete(0,tk.END)
    expression_field.insert(tk.END,curr + str(oper))
    
    
def clear_entry():
    expression_field.delete(0,tk.END)

def change_sign():
    curr = expression_field.get()
    expression_field.delete(0,tk.END)
    if int(curr)>0 :
        expression_field.insert(tk.END,'-' + curr)
    else :
        curr_int = -(int(curr))
        expression_field.insert(tk.END,str(curr_int))
    

def calc_op():
    current_expression = expression_field.get()
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    output_stack = []
    op_stack = []
    for char in current_expression:
        if char.isdigit():
            output_stack.append(int(char))
        elif char in operators:
            while op_stack and op_stack[-1] in operators :
                operand2 = output_stack.pop()
                operand1 = output_stack.pop()
                result = operators[op_stack.pop()](operand1, operand2)
                output_stack.append(result)
                op_stack.append(char)
        elif char == '(':
            op_stack.append(char)
        elif char == ')':
            while op_stack and op_stack[-1] != '(':
                operand2 = output_stack.pop()
                operand1 = output_stack.pop()
                result = operators[op_stack.pop()](operand1, operand2)
                output_stack.append(result)
                op_stack.pop()  # Remove the '(' from the stack 
        else:
            raise ValueError("Invalid character in expression")
    while op_stack:
        operand2 = output_stack.pop()
        operand1 = output_stack.pop()
        result = operators[op_stack.pop()](operand1, operand2)
        output_stack.append(result)
    result = output_stack.pop()
    expression_field.delete(0, tk.END)
    expression_field.insert(0, str(result))
    current_expression = str(result) 

# Window , Frame declaration

root = tk.Tk()
root.title("Scientific calculator")
# root.geometry("400x600")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create a frame that fills the window

# Calc Screen

# screen = tk.Entry(root).grid(row=0,column=0,columnspan=6,rowspan=1)

expression_field = ttk.Entry(root, width=30)
expression_field.grid(columnspan=6,pady=20)

# Button : Numbers and operation
cmp = 1
for i in range(1,4):
    for j in range(1,4):
        ttk.Button(text=str(cmp),width=5,command=lambda num=cmp : get_button(str(num))).grid(row=i,column=j,padx=5,pady=5)
        cmp=cmp+1

button_signe = ttk.Button(text='-/+',width=5,command=        change_sign).grid(row=4,column=1,padx=10,pady=5)
button_0     = ttk.Button(text='0'  ,width=5,command=lambda : get_button('0')).grid(row=4,column=2,padx=10,pady=5)
button_virg  = ttk.Button(text='.'  ,width=5,command=lambda : get_button(str(cmp))).grid(row=4,column=3,padx=10,pady=5)

# Les operations :
button_mul   = ttk.Button(text="x"  ,width=5,command=lambda : get_button('*')).grid(row=1,column=4,padx=10,pady=5)
button_sos   = ttk.Button(text="-"  ,width=5,command=lambda : get_button('-')).grid(row=2,column=4,padx=10,pady=5)
button_sum   = ttk.Button(text="+"  ,width=5,command=lambda : get_button('+')).grid(row=3,column=4,padx=10,pady=5)
button_div   = ttk.Button(text="/"  ,width=5,command=lambda : get_button('/')).grid(row=4,column=4,padx=10,pady=5)
button_puiss = ttk.Button(text="^"  ,width=5,command=lambda : get_button("^")).grid(row=6,column=4,padx=5,pady=5)
button_equa  = ttk.Button(text="="  ,width=5,command=         calc_op).grid(row=6,column=5,padx=5,pady=5)

# les fonctions mathematique

button_fact = ttk.Button(text="n!"  ,width=5,command=lambda : get_button("n!" )).grid(row=4,column=5,padx=5,pady=5)
button_sin  = ttk.Button(text="Sin" ,width=5,command=lambda : get_button("Sin")).grid(row=5,column=1,padx=5,pady=5)
button_cos  = ttk.Button(text="Cos" ,width=5,command=lambda : get_button("Cos")).grid(row=5,column=2,padx=5,pady=5)
button_tan  = ttk.Button(text="Tan" ,width=5,command=lambda : get_button("Tan")).grid(row=5,column=3,padx=5,pady=5)
button_log  = ttk.Button(text="Log" ,width=5,command=lambda : get_button("Log")).grid(row=5,column=4,padx=5,pady=5)
button_ln   = ttk.Button(text="Ln"  ,width=5,command=lambda : get_button("Ln" )).grid(row=5,column=5,padx=5,pady=5)
button_sqrt = ttk.Button(text="sqrt",width=5,command=lambda : get_button("sqrt")).grid(row=6,column=1,padx=5,pady=5)
button_pi   = ttk.Button(text="PI"  ,width=5,command=lambda : get_button("PI" )).grid(row=6,column=2,padx=5,pady=5)
button_e    = ttk.Button(text="Exp" ,width=5,command=lambda : get_button("Exp")).grid(row=6,column=3,padx=5,pady=5)


# Autre fonctions

button_supp = ttk.Button(text='C'   ,width=5,           command=clear_entry      ).grid(row=1,column=5,padx=5,pady=5)
button_par1 = ttk.Button(text='('   ,width=5,command=lambda : get_button(str(cmp))).grid(row=2,column=5,padx=5,pady=5)
button_par2 = ttk.Button(text=')'   ,width=5,command=lambda : get_button(str(cmp))).grid(row=3,column=5,padx=5,pady=5)


root.mainloop()
