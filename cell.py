from tkinter import Button,Label
import random
import settings
class Cell:
    all = []
    cell_count_label_object = None
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
            # text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>',self.left_click)
        btn.bind('<Button-3>',self.right_click)
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=(f"Cells Left:{settings.CELL_COUNT}"),
            width=12,
            height=4,
            bg='black',
            fg='white',
            font=('',30)
        )
        Cell.cell_count_label_object = lbl

    def left_click(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cell:
                    cell_obj.show_cell()
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

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cell:
            if(cell.is_mine):
                counter += 1
        
        return counter

    def show_cell(self):
        # print(self.surrounded_cell)
        # print(self.surrounded_cells_mines_length)
        self.cell_btn_object.config(text = self.surrounded_cells_mines_length)
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