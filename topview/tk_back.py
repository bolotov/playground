import Tkinter

top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="gray", height=250, width=300)

arc = C.create_rectangle(10,20,30,40, fill="red")

C.pack()
top.mainloop()
