import tkinter
from tkinter import END, ttk, messagebox

# helps to show results as table
from tabulate import tabulate


# This Function removes the entries after an action
def empty_entries():
    ID_entry.delete(0,END)
    name_entry.delete(0,END)


# This Function shows the list of students (Dictionnary)
def show_students(): 
    result.delete(1.0,END)
    headers = ["ID", "Name"]
    table = [[key, value['Name']] for key, value in Student.items()]
    result_text = tabulate(table, headers, tablefmt="plain")
    result.insert(END, result_text)
    

# This Function adds students to the students list (Dictionnary)
def add_student():
    id = ID_entry.get()
    Name = name_entry.get()
    id = id.upper()
    if Name == '':                              # verify entries if it is empty ,if so it shows an error message
        messagebox.showerror(title="Error", message="Please insert all entries .")

    elif id in Student:
        Student [id] = {'Name':Name}            # Updating an existing student
        messagebox.showinfo(title="Information", message="Student is updated.")
    else:
        Student [id] = {'Name':Name}            # Adding a new student
        messagebox.showinfo(title="Information", message="Student is added succesfuly.")
    empty_entries()


    
def search_student():
    id = ID_entry.get()
    id = id.upper()
    result.delete(1.0,END)
    if id == '':                                 # verify ID entry if it is empty ,if so it shows an error message  (Name is not necessary) 
        messagebox.showerror(title="Error", message="Please insert the ID .")

    elif id in Student:
        headers = ["ID", "Name"]                 # showing a message to user of students existing in the list
        messagebox.showinfo(title="Information", message="Student is found.")
        table = []
        for key , value in Student.items(): # Showing the student in text area
            if key == id:
                table.append([key, value['Name']])
        result_text = tabulate(table, headers, tablefmt="plain")
        result.insert(END, result_text)
        
    else:
        messagebox.showinfo(title="Information", message="Student not found.")
    
    empty_entries()
    

    
def delete_student():
    id = ID_entry.get()
    # confirmation message to alert user  
    answer = messagebox.askquestion(title="Confirmation", message="Are you sure you want to delete the student?")
    if answer == "yes":
        if id == '':                    # verify ID entry if it is empty ,if so it shows an error message  (Name is not necessary)
            messagebox.showerror(title="Error", message="Please insert ID of student.")
        elif id not in Student:
            messagebox.showerror(title="Error", message="Student not found")
        else :
            for key in Student:
                if key == id:
                    del Student[id] 
                    messagebox.showinfo(title="Information", message="Student is deleted succesfuly.")
                    show_students()
    else:
        messagebox.showinfo(title="Information", message="The action cancelled.")
    empty_entries()
        

# the list of students
Student = {
    'E1' : {'Name':'John Johnson'},
    'E2' : {'Name':'David Garcia'},
    'E3' : {'Name':'Michael Miller'},
    'E4' : {'Name':'James Davis'},
    'E5' : {'Name':'Robert Brown'}
}

# Creating the window and title of window 

root = tkinter.Tk()
root.title('Students MANAGER')

# text area that showes list

result = tkinter.Text(root,height=10)
result.grid(row=5,column=0,columnspan=2,padx=5,pady=5)

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
add_button      = ttk.Button(root,text='Add / modify a student'   ,command=add_student)   
search_button   = ttk.Button(root,text='Search a student',command=search_student)
delete_button   = ttk.Button(root,text='delete this student',command=delete_student)
show_all_button = ttk.Button(root,text='Show list of students',command= lambda : show_students())

add_button      .grid(row=3,column=0,padx=40,pady=20)
search_button   .grid(row=3,column=1,padx=40,pady=20)
delete_button   .grid(row=4,column=0,padx=40,pady=20)
show_all_button .grid(row=4,column=1,padx=40,pady=20)


# function to show the window
root.mainloop()