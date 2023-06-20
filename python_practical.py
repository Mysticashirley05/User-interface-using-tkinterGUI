import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import seaborn as sb

#importing data 
data=pd.read_csv("E:\semester 1\python lab\drugs_side_effects_drugs_com.csv")

#data cleaning
df=pd.DataFrame(data)                   
z=df.dropna()
k=z.drop_duplicates()
l=k.duplicated()

#creating user interface
def func():
    window1= tk.Tk()
    window1.title("DRUGS,SIDE EFFECTS AND MEDICAL CONDITION")
    text=Text(window1)
    window1.state("zoomed") 
    s=ttk.Style()
    s.theme_use('classic')
    s.configure("Treeview",bg="silver",fg="black")
    s.map("Treeview")
    data=pd.read_csv("E:\semester 1\python lab\drugs_side_effects_drugs_com.csv")
    d=pd.DataFrame(data)
    my_tree=ttk.Treeview(text)
    my_tree["column"]=list(df.columns)
    my_tree["show"]="headings"
    for column in my_tree["column"]:
        my_tree.heading(column,text=column)
    df_rows=df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("","end",values=row)
    text.pack(expand=True, fill=BOTH)
    my_tree.place(height=2000,width=1600)
    verscrlbar=ttk.Scrollbar(window,orient=VERTICAL,command=my_tree.yview)
    verscrlbar.pack(side=RIGHT,fill='y')
    my_tree.configure(yscrollcommand=verscrlbar.set)
    horscrlbar=ttk.Scrollbar(window1,orient=HORIZONTAL,command=my_tree.xview)
    horscrlbar.pack(side=BOTTOM,fill ='x')
    my_tree.configure(xscrollcommand=horscrlbar.set) 

#plotting
def graph():
    k.plot(kind="scatter",title="Rating vs No.of.reviews",x="rating",y="no_of_reviews")
    plt.show()
def graph1():
    k.plot(kind="hist")
    plt.show()
def graph2():
    k.plot(kind="line")
    plt.show()
def graph3():
    dataplot=sb.heatmap(k.corr(),annot=True)
    plt.show()
    

window= tk.Tk()
window.title("PYTHON")
window.state("zoomed")
window.configure(bg="cadet blue")

label=tk.Label(window,text="DRUGS,SIDE EFFECTS AND MEDICAL CONDITION",width=45,font=("Algerian",20),bg="cadet blue",fg="white")
label.place(x=400,y=70)

btn1=tk.Button(window,text="Data",width=30,font=("cambria",13),bg="white",fg="black",command=func)
btn1.place(x=600,y=150)

btn2=tk.Button(window,text="Rating vs No_of_reviews",width=30,font=("cambria",13),bg="white",fg="black",command=graph)
btn2.place(x=600,y=200)

btn3=tk.Button(window,text="Histogram",width=30,font=("cambria",13),bg="white",fg="black",command=graph1)
btn3.place(x=600,y=250)

btn4=tk.Button(window,text="Line plot",width=30,font=("cambria",13),bg="white",fg="black",command=graph2)
btn4.place(x=600,y=300)

btn5=tk.Button(window,text="Correlation",width=30,font=("cambria",13),bg="white",fg="black",command=graph3)
btn5.place(x=600,y=350)

window.mainloop()


