from asyncio.windows_events import NULL
from fileinput import filename
from importlib.resources import contents
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter
from tkinter import filedialog
import os
from turtle import width



def hiraku():
    idir = 'C:'
    filetype = [("テキスト","*.txt"), ("すべて","*")]
    file= tkinter.filedialog.askopenfilename(title = "ファイルを開く",filetypes = filetype, initialdir = idir)

    

    global globalfile
    globalfile=file

    filename.delete('1.0',END)
    filename.insert(INSERT,'path : '+globalfile+'\nfile : '+os.path.basename(globalfile))

    with open(file, 'r') as f:
        contents.delete('1.0',END)
        contents.insert(INSERT,f.read())
    



def hozonn():  
    global globalfile
    try:
        with open(globalfile, 'w') as f:
            f.write(contents.get('1.0',END))
    except (NameError,FileNotFoundError) as e:
            idir = 'C:'
            filetype = [("テキスト","*.txt"), ("すべて","*")]
            file =  filedialog.asksaveasfilename(initialdir = idir,title = "保存",filetypes =  filetype)
            print (file)

            
            globalfile=file

            filename.delete('1.0',END)
            filename.insert(INSERT,'path : '+globalfile+'\nfile : '+os.path.basename(globalfile))
            with open(file, 'w') as f:
               f.write(contents.get('1.0',END))
    

def hozonn2():
    idir = 'C:'
    filetype = [("テキスト","*.txt"), ("すべて","*")]
    file =  filedialog.asksaveasfilename(initialdir = idir,title = "保存",filetypes =  filetype)
    print (file)

    global globalfile
    globalfile=file

    filename.delete('1.0',END)
    filename.insert(INSERT,'path : '+globalfile+'\nfile : '+os.path.basename(globalfile))
    with open(file, 'w') as f:
        f.write(contents.get('1.0',END))


top=Tk()
top.title('コマンドプロンプトみたいなメモ帳')

contents=ScrolledText(bg="black",bd=10,blockcursor=True,insertbackground='gray',cursor='trek',fg='white',insertwidth=1,insertofftime=300, insertontime=200)
contents.pack(side=BOTTOM,expand=True,fill=BOTH)

filename=ScrolledText(bg="black",bd=10,height=1,blockcursor=True,insertbackground='gray',cursor='trek',fg='white',insertwidth=1,insertofftime=300, insertontime=200)
filename.pack(side=LEFT,expand=True,fill=BOTH)


Button(text='開く',command=hiraku).pack(side=RIGHT)
Button(text='保存',command=hozonn2).pack(side=RIGHT)
Button(text='上書き保存',command=hozonn).pack(side=RIGHT)


mainloop()