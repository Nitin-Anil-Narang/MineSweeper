from tkinter import Button
import random
import settings
class Cell:
    all = []
    def __init__(self,x,y,is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        
        #Appending all the class instances to the "All" list
        Cell.all.append(self) 

    
    def create_btn_object(self,location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>',self.left_click)
        btn.bind('<Button-3>',self.right_click)
        self.cell_btn_object = btn

    def left_click(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def get_cell_axis(self,x,y):
        # Return cell object based on X and Y
        for cell in Cell.all:
            if cell.x ==x and cell.y == y:
                return cell

    @property
    def surrounded_cell(self):
        cells = [
            self.get_cell_axis(self.x,self.y-1),
            self.get_cell_axis(self.x-1,self.y-1),
            self.get_cell_axis(self.x-1,self.y+1),
            self.get_cell_axis(self.x+1,self.y),
            self.get_cell_axis(self.x+1,self.y-1),
            self.get_cell_axis(self.x+1,self.y+1),
            self.get_cell_axis(self.x-1,self.y),
            self.get_cell_axis(self.x,self.y+1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
        
    def show_cell(self):
        print(self.surrounded_cell)

    def show_mine(self):
        # logic to interrupt game and display lose for a player
        self.cell_btn_object.config(
            bg='red'
        )

    def right_click(self,event):
        print(event)
        print("I am the right click")

    @staticmethod
    def randomize_mine():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        # print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True


        # my_list  = ['Jim','MIchael','Dwight']
        # picked_names = random.sample(my_list,2)
        # print(picked_names)

    def __repr__(self):
        return f"Cell({self.x},{self.y})"