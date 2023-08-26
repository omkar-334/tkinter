import pandas as pd
import tkinter  as tk 
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
my_w = tk.Tk()
my_w.geometry("300x300")  # Size of the window 
my_w.title('PTK')

my_font1=('times', 12, 'bold')
l1 = tk.Label(my_w,text='Read File & create DataFrame',
    width=30,font=my_font1)  
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Browse File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 
t1=tk.Text(my_w,width=40,height=5)
t1.grid(row=3,column=1,padx=5)

def upload_file():
    f_types = [('CSV files',"*.csv"),('All',"*.*")]
    file = filedialog.askopenfilename(filetypes=f_types)
    l1.config(text=file) # display the path 
    df=pd.read_excel(file) # create DataFrame
    str1="Rows:" + str(df.shape[0])+ "\nColumns:"+str(df.shape[1])
    #print(str1)
    t1.insert(tk.END, str1)
my_w.mainloop()  