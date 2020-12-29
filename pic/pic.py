from tkinter import *
from tkinter.filedialog import *
import json
import os

rows, cols = 39, 79
col, row = -1, -1
but_name, gx = '', 0

def save():
    global mat
    po = asksaveasfilename(defaultextension=".txt")
    with open(po, 'w') as fileo:
        for i in range(len(mat)):
            mat[i] = list(mat[i])
            if i == 0:
                mat[i].append(',')
                mat[i].append('\n')
            elif mat[i] != mat[-1] and i > 0:
                mat[i].append(',')
                mat[i].append('\n')
            mat[i] = ''.join(mat[i])
            fileo.write(mat[i])

def zap():
    string = ''
    for i in range(cols):
        string = string + '0'
    return string

def op():
    global mat
    mat = [zap() for i in range(rows)]
    po = askopenfilename()
    with open(po, 'r') as fileo:
        fileo = fileo.read()
        fileo = fileo.split(',\n')
        mat = fileo[:]
        gx = 0
        ggx = -1
        mas = []
        mt = mat[:]
        for i in mt:
            i = list(i)
        for i in mt:
            for j in i:
                if j != ',':
                    mas.append(j)
        for i in range(rows):
            for j in range(cols):
                gx += 1
                ggx += 1
                if mas[ggx] == '1':
                    exec(
'btn{0}.config(bg="white")\n'.format(gx))
                if mas[ggx] == '2':
                    exec(
'btn{0}.config(bg="gray")\n'.format(gx))
        
def och():
    global mat
    mat = [zap() for i in range(rows)]
    gx = 0
    for i in range(rows):
        for j in range(cols):
            gx += 1
            exec(
'btn{0}.config(bg="black")\n'.format(gx))

def changeBt(bt, row, col, color):
    b = list(mat[row])
    b[col] = "0"
    st = ""
    for i in b:
        st = st + i
    mat[row] = st
    bt.config(bg=color)

mat = [zap() for i in range(rows)]

root = Tk()
root.geometry("1100x600")
root.resizable(False, False)

mainmenu = Menu(root) 
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть", command=op)
filemenu.add_command(label="Сохранить", command=save)
filemenu.add_command(label="Очистить", command=och)
filemenu.add_command(label="Выход", command=lambda: os._exit(1))
        
mainmenu.add_cascade(label="Файл", menu=filemenu)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

for row_index in range(rows):
    Grid.rowconfigure(frame, row_index, weight=1)
    row += 1
    for col_index in range(cols):
        gx += 1
        but_name = 'btn' + str(gx)
        Grid.columnconfigure(frame, col_index, weight=1)
        col += 1
        exec(
'global {0}\n\
{0} = Button(frame, bg="black")\n\
{0}.bind("<Button-1>", lambda event: changeBt({0}, {2}, {3}, "white"))\n\
{0}.bind("<Button-3>", lambda event: changeBt({0}, {2}, {3}, "black"))\n\
{0}.grid(row=row_index, column=col_index, sticky=N+S+E+W)\n'.format(but_name, gx, row, col))
    col = -1

root.mainloop()
