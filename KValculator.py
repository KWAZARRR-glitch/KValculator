import tkinter as tk
import math 

def press(key):
    if key == '=':
        result = eval(screen.get())
        screen.delete(0, 'end')
        screen.insert(0, result)
    elif key == 'c':
        screen.delete(0, 'end')
    elif key == '√':
        x = float(screen.get())
        screen.delete(0, 'end')
        screen.insert(0, math.sqrt(x))
    else:
        screen.insert('end', key)

root = tk.Tk()
root.title('KValculator')
screen = tk.Entry(root,
                  font=('Arial', 28),
                  justify='right')
screen.grid(row=0, column=0, columnspan=4)

keys = ['c', '√', '(', ')', 
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', ',', '=', '+']

for i, key in enumerate(keys):
    btn =tk.Button(
        root, text=key, width=4,
        font=('Arial', 20), 
        command=lambda k=key:
             press(k))
    btn.grid(row=i // 4+1,
              column=i % 4)
root.mainloop()    
