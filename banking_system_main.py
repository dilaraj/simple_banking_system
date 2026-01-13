import tkinter as tk

root = tk.Tk()
root.title('First Tkinter Window')

name_var = tk.StringVar()
passw_var = tk.StringVar()

def submit():
    name = name_var.get()
    password = passw_var.get()

    print('The name is: ' + name)
    print('The password is: ' + password)

    name_var.set('')
    passw_var.set('')

#creating a label and entry for name and password wusing the widget label and entry
name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'bold'))

passw_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))
passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'bold'), show='*')

#creating btn using widget btn for submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

#placing elemtns using grid method
name_label.grid(row=0,column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

#performing infinite loop for window display
root.mainloop()