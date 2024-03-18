from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
#settings OverWrite
root.config(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("MineSweeper")
root.resizable(False,False)

top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_prct(25)
    )
top_frame.place(x=0 ,y=0)

left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75),
)
left_frame.place(x=0,y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))

# btn1 =Button(
#     center_frame,
#     bg="blue",
#     text="First Button"
# )
# btn1.place(x=0,y=0)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,row=y
        )

Cell.randomize_mine()
#Checking the is_mine property
# for c in Cell.all:
#     print(c.is_mine)

# print(Cell.all)
# print(dir(Cell))

# Running the Window 
root.mainloop()