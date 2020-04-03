from tkinter import *
from time import sleep
import random
class Application:
    
    def __init__(self,master):

        self.heights= [5, 2, 1, 8, 4]
        self.blocks = []
        self.width = 60
        self.aligner = 30
        self.margin = 30
        self.length=500
        self.breadth=360
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

        processor_button = Button(master,text = "Click to Bubble sort", command=self.sort_show)
        processor_button.pack(side=BOTTOM)
    
    


    def clean_color(self):
        for block in self.blocks:
            block['color']='green'
        

    def show(self,time = 0.001):
        self.canvas.delete(ALL)
        w = self.width
        a = 30
        for block in self.blocks:
            self.canvas.create_rectangle(a,550-50*block["height"],a+w,550, fill=block['color'])
            a += w
        sleep(time)
            

    def sort_show(self):
        self.bubble_sort()
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
   

root = Tk()

app = Application(root)

root.mainloop()









