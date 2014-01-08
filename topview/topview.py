import Tkinter, itertools
# coords are counted from top left (right,down)

o = 150   # o is an offset by both x and y screen coords
s = 3    # s is a size of a 'pixel' by both x and y coords

if __name__ == "__main__":
    top = Tkinter.Tk()

    C = Tkinter.Canvas(top, bg="gray", height=250, width=300)
    for x, y, z in itertools.product(range(10), range(10), range(10)):
        C.create_rectangle(o+x*s-z*0.3,o+y*s-z*0.3,o+s+x*s-z*0.3,o+s+y*s-z*0.3, fill="red")

    C.pack()
    top.mainloop()
    
