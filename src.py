from tkinter import *
from time import sleep
import random

class Application:
    
    def __init__(self,master):

        self.heights = [5, 2, 1, 8, 4]
        self.blocks = []
        self.width = 60 # width of individual blocks
        self.aligner = 30
        self.margin = 30
        self.length = 500
        self.breadth = 360 # width of window
        self.bars = 5
        self.master = master

        self.canvas = Canvas(master,height=self.length,width=self.breadth)
        self.canvas.pack()
        
        for height in self.heights :
            block = {"height" : height }
            block['rect'] = self.canvas.create_rectangle(self.aligner,550-50*height,self.aligner+self.width,550, fill="green")
            block['color'] = 'green'
            self.blocks.append(block)
            self.aligner += self.width

        slider_x = Scale(master, from_=5 , to=500, orient = HORIZONTAL, bg="blue",command = self.wid)
        slider_x.pack(side=TOP)

        bubble_sort_button = Button(master,text = "Click to Bubble sort", command=self.bubble_sort_show)
        bubble_sort_button.pack(side=BOTTOM)

        insertion_sort_button = Button(master,text = "Click to Insertion sort", command=self.insertion_sort_show)
        insertion_sort_button.pack(side=BOTTOM)
    
        selection_sort_button = Button(master,text = "Click to Selection sort", command=self.selection_sort_show)
        selection_sort_button.pack(side=BOTTOM)

    def clean_color(self):
        for block in self.blocks:
            block['color'] = 'green'
        

    def show(self,time = 0.001):
        self.canvas.delete(ALL)
        w = self.width
        rect_begin = 30
        for block in self.blocks:
            self.canvas.create_rectangle(rect_begin,550-50*block["height"],rect_begin+w,550, fill=block['color'])
            rect_begin += w
        sleep(time)
            

    def bubble_sort_show(self):
        self.bubble_sort()
        self.show()

    def insertion_sort_show(self):
        self.insertion_sort()
        self.show()

    def selection_sort_show(self):
        self.selection_sort()
        self.show()

    def draw(self):
        self.canvas.delete(ALL)
        self.aligner = self.margin
        self.width = (self.breadth - self.margin*2)/self.bars
        for height in self.heights :
            block = {"height" : height }
            block['rect'] = self.canvas.create_rectangle(self.aligner,550-50*height,self.aligner+self.width,550, fill="green")
            block['color'] = 'green'
            self.blocks.append(block)
            self.aligner += self.width
        self.master.update()


    def wid(self,e):
        self.bars = int(int(e)/5)
    #     print(bars)
        self.blocks = []
        self.heights = []
        for i in range(self.bars):
            h = random.uniform(0.1,0.98)*10
            self.heights.append(h)
        self.draw()



    def bubble_sort(self):
        # We set swapped to True so the loop looks runs at least once
        swapped = True
        while swapped:
            self.clean_color()
            self.show()
            swapped = False
            for i in range(len(self.blocks) - 1):
                self.clean_color()
                self.blocks[i]['color']='blue'
                self.show()
                self.master.update()

                if self.blocks[i]["height"] > self.blocks[i + 1]["height"]:

                    self.master.update()
                    self.blocks[i+1]['color']='orange'
                    self.show()
                    
                    # Swap the elements
                    self.blocks[i], self.blocks[i + 1] = self.blocks[i + 1], self.blocks[i]
                    self.master.update()
                    
                    self.show()
                    # Set the flag to True so we'll loop again
                    swapped = True
        
        self.clean_color()
        self.show()


    def insertion_sort(self):
        for i in range(1, len(self.blocks)): # start at 1 because index 0 must be already sorted
            self.clean_color()
            self.blocks[i]['color'] = 'blue'
            self.show()
            self.master.update()

            j = i
            while self.blocks[j]['height'] < self.blocks[j-1]['height'] and j > 0 : # while block is not in the right place
                
                self.blocks[j], self.blocks[j-1] = self.blocks[j-1], self.blocks[j] # swap the two blocks
                j -= 1
                
                self.clean_color()
                self.blocks[j]['color'] = 'blue' # reset the colors and make the moved block blue
                self.master.update()
                self.show()

        self.clean_color()
        self.show()


    def selection_sort(self):
        for i in range(len(self.blocks)) :
            self.clean_color()
            self.blocks[i]['color'] = 'blue'
            self.show()
            self.master.update()

            min_pos = 0
            min_val = 1000
            for j in range(i, len(self.blocks)) : # start at i because everything before was already looked at
                self.clean_color()
                self.blocks[j]['color'] = 'orange'
                self.blocks[min_pos]['color'] = 'red'
                self.blocks[i]['color'] = 'blue'
                
                self.show()
                self.master.update()
                
                if self.blocks[j]['height'] < min_val :
                    min_val = self.blocks[j]['height']
                    min_pos = j
                    
                    self.blocks[j]['color'] = 'red'

                    self.show()
                    self.master.update()

            j = min_pos
            while self.blocks[j]['height'] < self.blocks[j-1]['height'] and j > 0 :                
                self.blocks[j], self.blocks[j-1] = self.blocks[j-1], self.blocks[j] # swap the two blocks
                j -= 1

                self.clean_color()
                self.blocks[i]['color'] = 'blue'
                self.blocks[j]['color'] = 'red'

                self.show()
                self.master.update()

        self.clean_color()
        self.show()
                
root = Tk()

app = Application(root)

root.mainloop()

