import Tkinter, itertools
# coords are counted from top left (right,down)

OFFSET = 150   # o is an offset by both x and y screen coords
s = 3    # s is a size of a 'pixel' by both x and y coords
Z_SHIFT = -0.3
[MAX_X, MAX_Y, MAX_Z] = [10, 10, 10]


if __name__ == "__main__":
    top = Tkinter.Tk()

    C = Tkinter.Canvas(top, bg="gray", height=250, width=300)
    for x, y, z in itertools.product(range(MAX_X), range(MAX_Y), range(MAX_Z)):
        C.create_rectangle(OFFSET+x*s+z*Z_SHIFT,
			OFFSET+y*s+z*Z_SHIFT,
			OFFSET+s+x*s+z*Z_SHIFT,
			OFFSET+s+y*s+z*Z_SHIFT, fill="red")

    C.pack()
    top.mainloop()
    

