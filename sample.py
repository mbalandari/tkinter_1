import tkinter

root = tkinter.Tk()
root.title('Label')
root.iconbitmap('1.ico')
root.geometry('700x350')
root.resizable(0,0)
root.config(bg='black')

label_1 = tkinter.Label(root, text='Hello Label!')
label_1.pack()

label_2 = tkinter.Label(root, text='The second Label eva!', font=('Arial', 18, 'bold'))
label_2.pack()

root.mainloop()