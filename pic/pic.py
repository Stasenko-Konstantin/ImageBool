from tkinter import *
from tkinter.filedialog import *
import json
import os

rows = 39
cols = 79
col = -1
row = -1
gx = 0
but_name = ''

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

def ext():
    os._exit(1)

def op():
    global mat
    och()
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
'btn{0}.config(bg="white")\n\
'.format(gx))
                if mas[ggx] == '2':
                    exec(
'btn{0}.config(bg="gray")\n\
'.format(gx))
        
def och():
    global mat
    mat = [zap() for i in range(rows)]
    gx = 0
    for i in range(rows):
        for j in range(cols):
            gx += 1
            exec(
'btn{0}.config(bg="black")\n\
'.format(gx))

mat = [zap() for i in range(rows)]

root = Tk()
root.geometry("1100x600")
root.resizable(False, False)

mainmenu = Menu(root) 
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть/Open", command=op)
filemenu.add_command(label="Сохранить/Save", command=save)
filemenu.add_command(label="Очистить/Clear", command=och)
filemenu.add_command(label="Выход/Exit", command=ext)
        
mainmenu.add_cascade(label="Файл/File", menu=filemenu)

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
def one{0}(event):\n\
    b = list(mat[{2}])\n\
    b[{3}] = "0"\n\
    st = ""\n\
    for i in b:\n\
        st = st + i\n\
    mat[{2}] = st\n\
    {0}.config(bg="black")\n\
def zero{0}(event):\n\
    b = list(mat[{2}])\n\
    b[{3}] = "1"\n\
    st = ""\n\
    for i in b:\n\
        st = st + i\n\
    mat[{2}] = st\n\
    {0}.config(bg="white")\n\
def two{0}(event):\n\
    b = list(mat[{2}])\n\
    b[{3}] = "2"\n\
    st = ""\n\
    for i in b:\n\
        st = st + i\n\
    mat[{2}] = st\n\
    {0}.config(bg="gray")\n\
{0} = Button(frame, bg="black")\n\
{0}.bind("<Button-1>", zero{0})\n\
{0}.bind("<Button-2>", two{0})\n\
{0}.bind("<Button-3>", one{0})\n\
{0}.grid(row=row_index, column=col_index, sticky=N+S+E+W)\n\
'.format(but_name, gx, row, col))
    col = -1

root.mainloop()
