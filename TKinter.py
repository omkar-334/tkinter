import pandas
import tkinter as tk

cols_main=[1,2,3,7,11,12,13]
summer=pandas.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
    converters={'Cell':str,'Adm':str},
    usecols=cols_main)

cols_overall=[17,18,19,20]
cols_old=[22,23,24,25]
cols_new=[27,28,29,30]

overall=pandas.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
	usecols=cols_overall)
toverall=overall.transpose()

old=pandas.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
	usecols=cols_old)
told=old.transpose()

new=pandas.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
	usecols=cols_new)
tnew=new.transpose()

window = tk.Tk()
window.title('Loyola High School')
window.geometry('975x400')
window.configure(bg='#A2DCEE')
bcwin=tk.Frame(window, background="red")

def search_df(*event):
    search_result=summer.loc[summer["Name"].str.contains(e1_value.get(),
                               na=False, #ignore the cell's value is Nan
                               case=False)] #case insensitive
    e2.delete(0, "end")
    e3.delete(0, "end")
    t1.delete("1.0", "end")
    t2.delete("1.0", "end")
    t3.delete("1.0", "end")
    t4.delete("1.0", "end")
    t1.insert(tk.END,search_result)
lbl1=tk.Label(window, text="Enter Student Name",bg='#A2DCEE', fg='#7339AB', font=("Calibri", 9),bd=0)
lbl1.place(x=10,y=10)
#Creates the entry box and link the e1_value to the variable
e1_value=tk.StringVar()
e1=tk.Entry(window, textvariable=e1_value,bg='#C6CDFF')
e1.place(x=10,y=30)
#execute the search_df function when you hit the "enter" key and put an event
#parameter
e1.bind("<Return>", search_df)

#Creates a text box
t1=tk.Text(window,height=30,width=150)
t1.place(x=150,y=0)
#Creates a button
b1=tk.Button(window,
             text='Search',
             command=search_df)

b1.place(x=35,y=50)

def search_df2(*event):
    search_result=summer.loc[summer["Adm"].str.contains(e2_value.get(),
                               na=False, #ignore the cell's value is Nan
                               case=False)] #case insensitive
    searchoverall=(overall.loc[summer["Adm"].str.contains(e2_value.get(),
                               na=False, #ignore the cell's value is Nan
                               case=False)]).transpose() #case insensitive
    searchold=(old.loc[summer["Adm"].str.contains(e2_value.get(),
                               na=False, #ignore the cell's value is Nan
                               case=False)]).transpose() #case insensitive
    searchnew=(new.loc[summer["Adm"].str.contains(e2_value.get(),
                               na=False, #ignore the cell's value is Nan
                               case=False)]).transpose() #case insensitive
    e1.delete(0, "end")
    e3.delete(0, "end")
    t1.delete("1.0", "end")
    t2.delete("1.0", "end")
    t3.delete("1.0", "end")
    t4.delete("1.0", "end")
    t1.insert(tk.END,search_result)
    t2.insert(tk.END,searchoverall)
    t3.insert(tk.END,searchold)
    t4.insert(tk.END,searchnew)
lbl2=tk.Label(window, text="Enter Admission Number",bg='#A2DCEE', fg='#7339AB', font=("Calibri", 9))
lbl2.place(x=2,y=80)
#Creates the entry box and link the e1_value to the variable
e2_value=tk.StringVar()
e2=tk.Entry(window, textvariable=e2_value,bg='#C6CDFF')
e2.place(x=10,y=100)
#execute the search_df function when you hit the "enter" key and put an event
#parameter
e2.bind("<Return>", search_df2)

#Creates a button
b2=tk.Button(window,
             text='Search',
             command=search_df2)

b2.place(x=35,y=120)

def search_df3(*event):
    search_result=summer.loc[summer["Cell"].str.contains(e3_value.get(),
                               na=False, #ignore the cell's value is Nan
                               case=False)] #case insensitive
    e1.delete(0, "end")
    e2.delete(0, "end")
    t1.delete("1.0", "end")
    t2.delete("1.0", "end")
    t3.delete("1.0", "end")
    t4.delete("1.0", "end")
    t1.insert(tk.END,search_result)
lbl3=tk.Label(window, text="Enter Phone Number",bg='#A2DCEE', fg='#7339AB', font=("Calibri", 9))
lbl3.place(x=4,y=150)
#Creates the entry box and link the e1_value to the variable
e3_value=tk.StringVar()
e3=tk.Entry(window, textvariable=e3_value,bg='#C6CDFF')
e3.place(x=10,y=170)
#execute the search_df function when you hit the "enter" key and put an event
#parameter
e3.bind("<Return>", search_df3)

#Creates a button
b3=tk.Button(window,
             text='Search',
             command=search_df3)

b3.place(x=35,y=190)

t2=tk.Text(window,height=10,width=150)
t2.place(x=150,y=220)

t3=tk.Text(window,height=10,width=150)
t3.place(x=425,y=220)

t4=tk.Text(window,height=10,width=150)
t4.place(x=700,y=220)

window.mainloop() #end of the main window