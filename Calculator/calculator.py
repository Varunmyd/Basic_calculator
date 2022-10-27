from tkinter import *
import parser
from math import factorial
root=Tk()
root.title("Calculator")
root.geometry("800x800")
display=Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

#input user
i=0
def get_variable(num):
    global i
    display.insert(i,num)

    i+=1
def all_clear():
    display.delete(0,END)
def undo():
    full_string=display.get()
    if len(full_string):
        new_string =full_string[:-1]
        all_clear()
        display.insert(0,new_string)
def get_opertr(opr):
    global i
    lngth=len(opr)
    display.insert(i,opr)
    i+=1
def calctn():
    full_string=display.get()
    try:
        a=parser.expr(full_string).compile()
        reslt=eval(a)
        all_clear()
        display.insert(0,reslt)

    except Exception:
        all_clear()
        display.insert(0,"Syntax error")
def recur(x):
    if x==1:
        return 1
    else:
        return x*recur(x-1)

def fact():
    input=display.get()

    reslt=recur(int(input))
    all_clear()
    display.insert(0,reslt)
# def fact():
#     entire_string = display.get()
#     try:
#         result = factorial(int(entire_string))
#         all_clear()
#         display.insert(0,result)
#     except Exception:
#         all_clear()
#         display.insert(0,"Error")




#adding button
Button(root,text="7",width=2,height=2,command=lambda :get_variable(7)).grid(row=3,column=0)
Button(root,text="8",width=2,height=2,command=lambda :get_variable(8)).grid(row=3,column=1)
Button(root,text="9",width=2,height=2,command=lambda :get_variable(9)).grid(row=3,column=2)
Button(root,text="4",width=2,height=2,command=lambda :get_variable(4)).grid(row=4,column=0)
Button(root,text="5",width=2,height=2,command=lambda :get_variable(5)).grid(row=4,column=1)
Button(root,text="6",width=2,height=2,command=lambda :get_variable(6)).grid(row=4,column=2)
Button(root,text="1",width=2,height=2,command=lambda :get_variable(1)).grid(row=5,column=0)
Button(root,text="2",width=2,height=2,command=lambda :get_variable(2)).grid(row=5,column=1)
Button(root,text="3",width=2,height=2,command=lambda :get_variable(3)).grid(row=5,column=2)
Button(root,text="0",width=2,height=2,command=lambda :get_variable(0)).grid(row=6,column=1)
Button(root,text="+",width=2,height=2,command=lambda :get_opertr('+')).grid(row=5,column=3)
Button(root,text="-",width=2,height=2,command=lambda :get_opertr('-')).grid(row=5,column=4)
Button(root,text="*",width=2,height=2,command=lambda :get_opertr('*')).grid(row=4,column=3)
Button(root,text="/",width=2,height=2,command=lambda :get_opertr('/')).grid(row=4,column=4)
Button(root,text="=",bg="blue",width=2,height=2,command=lambda :calctn()).grid(row=6,column=4)
Button(root,text="(",bg='black',fg='white',width=2,height=2,command=lambda :get_opertr('(')).grid(row=2,column=2)
Button(root,text=")",bg='black',fg='white',width=2,height=2,command=lambda :get_opertr(')')).grid(row=2,column=3)
Button(root,text="%",width=2,height=2,command=lambda :get_opertr('/100')).grid(row=6,column=0)
Button(root,text="AC",bg='red',width=2,height=2,command=lambda :all_clear()).grid(row=3,column=4)
Button(root,text="C",bg='red',width=2,height=2,command=lambda :undo()).grid(row=3,column=3)
Button(root,text="^2",bg='black',fg='white',width=2,height=2,command=lambda :get_opertr('**2')).grid(row=2,column=4)
Button(root,text="exp",bg='black',fg='white',width=2,height=2,command=lambda :get_opertr('**')).grid(row=2,column=1)
Button(root,text="x!",bg='black',fg='white',width=2,height=2,command=lambda :fact()).grid(row=2,column=0)
Button(root,text=".",width=2,height=2,command=lambda :get_variable(".")).grid(row=6,column=2)
Button(root,text="pi",width=2,height=2,command=lambda :get_opertr('3.14')).grid(row=6,column=3)

root.mainloop()
