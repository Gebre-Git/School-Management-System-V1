from tkinter import*

root = Tk()
root.geometry("700x400")

def geometry(event):
    root.title("x = {0:2d}, y = {1:d}".format(event.x, event.y))
root.bind("<Motion>", geometry)

root.mainloop()