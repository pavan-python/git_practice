from tkinter import *

main = Tk()
main.title('test')
main.geometry('500x300')
label1 = Label(main, text = 'Enter first Name: ')
label1.grid(row=0, column=0)

def submit():
    pass


def reset():
    greet1 = 'Rested'
    text1.config(text=greet1)
    text1.delete(0,END)
    text2.config(text = greet1)
    text2.delete(0, END)


text1 = Entry(main)
text1.grid(row=0, column=1)

label2 = Label(main, text = 'Enter last Name: ')
label2.grid(row=1, column=0)

text2 = Entry(main)
text2.grid(row=1, column=1)

btn1 = Button(main, text='Submit', padx=5, pady=5, command=submit)
btn1.grid(row=2, column=1)
btn2 = Button(main, text='Reset', padx=5, pady=5, command=reset)
btn2.grid(row=2, column=2)


main.mainloop()