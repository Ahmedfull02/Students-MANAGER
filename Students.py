import json
from os import write
import tkinter
from tkinter import END, Frame, ttk, messagebox


# helps to show results as table
from tabulate import tabulate 


# read list of studentss from the file
def read_students():
    # Open the file in read mode
    with open('students.txt', 'r') as file:
        s = json.load(file)
    print("Dictionary is read from file succefully")
    return s

# Dictionary to store the data
Students = read_students()

# function to save the list to the file

def save_students():
    with open('students.txt','w') as file:
        json.dump(Students,file)
    messagebox.showinfo("Save","List saves succefully")

# This Function removes the entries after an action
def empty_entries():
    ID_entry.delete(0,END)
    name_entry.delete(0,END)


# This Function shows the list of studentss (Dictionnary)
def show_students(): 
    result.delete(1.0,END)
    headers = ["ID", "Name"]
    table = [[key, value['Name']] for key, value in Students.items()]
    result_text = tabulate(table, headers, tablefmt="plain")
    result.insert(END, result_text)
    

# This Function adds studentss to the studentss list (Dictionnary)
def add_students():
    id = ID_entry.get()
    Name = name_entry.get()
    id = id.upper()
    if Name == '':                              # verify entries if it is empty ,if so it shows an error message
        messagebox.showerror(title="Error", message="Please insert all entries .")

    elif id in Students:
        Students [id] = {'Name':Name}            # Updating an existing students
        messagebox.showinfo(title="Information", message="Students is updated.")
    else:
        Students [id] = {'Name':Name}            # Adding a new students
        messagebox.showinfo(title="Information", message="Students is added succesfuly.")
    empty_entries()


    
def search_students():
    id = ID_entry.get()
    id = id.upper()
    result.delete(1.0,END)
    if id == '':                                 # verify ID entry if it is empty ,if so it shows an error message  (Name is not necessary) 
        messagebox.showerror(title="Error", message="Please insert the ID .")

    elif id in Students:
        headers = ["ID", "Name"]                 # showing a message to user of studentss existing in the list
        messagebox.showinfo(title="Information", message="Students is found.")
        table = []
        for key , value in Students.items(): # Showing the students in text area
            if key == id:
                table.append([key, value['Name']])
        result_text = tabulate(table, headers, tablefmt="plain")
        result.insert(END, result_text)
        
    else:
        messagebox.showinfo(title="Information", message="Students not found.")
    
    empty_entries()
    

    
def delete_student():
    id = ID_entry.get()
    # confirmation message to alert user  
    answer = messagebox.askquestion(title="Confirmation", message="Are you sure you want to delete the students?")
    if answer == "yes":
        if id == '':                    # verify ID entry if it is empty ,if so it shows an error message  (Name is not necessary)
            messagebox.showerror(title="Error", message="Please insert ID of students.")
        elif id not in Students:
            messagebox.showerror(title="Error", message="Students not found")
        else :
            for key in Students:
                if key == id:
                    del Students[id] 
                    messagebox.showinfo(title="Information", message="Students is deleted succesfuly.")
                    show_students()
    else:
        messagebox.showinfo(title="Information", message="The action cancelled.")
    empty_entries()
        

# Creating the window and title of window 


root = tkinter.Tk()
root.title('Students MANAGER')

result = tkinter.Text(root,height=10)
result.grid(row=6,column=0,columnspan=2,padx=5,pady=5)

# all labels 
ID_label        = ttk.Label(root,text='ID : ')  
name_label      = ttk.Label(root,text='Name : ')

ID_label        .grid(row=0,column=0,padx=40,pady=20)
name_label      .grid(row=1,column=0,padx=40,pady=20)


# all entries
ID_entry        = ttk.Entry(root,width=20)
name_entry      = ttk.Entry(root,width=20)
ID_entry.       grid(row=0,column=1,padx=40,pady=20)
name_entry.     grid(row=1,column=1,padx=40,pady=20)

# all buttons
add_button      = ttk.Button(root,text='Add / modify a students'   ,command=add_students)   
search_button   = ttk.Button(root,text='Search student',command=search_students)
delete_button   = ttk.Button(root,text='delete student',command=delete_student)
show_all_button = ttk.Button(root,text='Show list of students',command= lambda : show_students())
save_button     = ttk.Button(root,text='Save list of students',command= save_students)

add_button      .grid(row=3,column=0,padx=40,pady=20)
search_button   .grid(row=3,column=1,padx=40,pady=20)
delete_button   .grid(row=4,column=0,padx=40,pady=20)
show_all_button .grid(row=4,column=1,padx=40,pady=20)
save_button     .grid(row=5,columnspan=2,padx=40,pady=20)

add_button      .configure()
search_button   .configure()
delete_button   .configure()
show_all_button .configure()
save_button     .configure()

# function to show the window
root.mainloop()