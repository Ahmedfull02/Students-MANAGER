import json
from os import write
import tkinter
from tkinter import END, ttk, messagebox

# helps to show results as table
from tabulate import tabulate # type: ignore


# the list of studentss
Students = {
    'E1' : {'Name':'John Johnson'},
    'E2' : {'Name':'David Garcia'},
    'E3' : {'Name':'Michael Miller'},
    'E4' : {'Name':'James Davis'},
    'E5' : {'Name':'Robert Brown'}
}

# Dictionary to write

# Open a file in write mode

with open('students.txt', 'w') as file:
    # Write each key-value pair on a new line
    json.dump(Students,file)

print("Dictionary written to file as plain text.")


