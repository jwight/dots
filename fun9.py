import tkinter as tk
import random

class Application(tk.Frame):
    
   def DoOneTick(self):
        cell = random.randint(0,self.sideCells*self.sideCells-1)
        row = int(cell / self.sideCells)
        column = int(cell - row*self.sideCells)
        acolor = ["red", "blue", "yellow", "green", "brown", "orange"]
        color = acolor[random.randint(0,5)]
        self.i = self.i+1
        s = str(self.i)
        #s = s + " cell " + str(cell)
        self.v.set(s)
        if (self.o[cell] != 0):
           self.canvas.delete(self.o[cell])
           self.o[cell] = 0
        else:
           self.o[cell] = self.canvas.create_oval(column*self.cellSize+self.ofs, row*self.cellSize+self.ofs, (column+1)*self.cellSize+self.ofs, (row+1)*self.cellSize+self.ofs, fill=color, outline=color)
        if (self.running):
            self.after(1, self.DoOneTick)
                
   def Start(self):
        self.running = True
        self.DoOneTick()
    
   def Stop(self):
        self.running = False;

   def Once(self):
        self.running = False
        self.DoOneTick()
        
   def DrawGrid(self):
      if (self.showGrid).get():
          for i in range(0,self.sideCells*self.cellSize+1,self.cellSize):
             a = self.canvas.create_line(i+self.ofs,self.ofs,i+self.ofs,self.sideCells*self.cellSize+self.ofs)
             self.gridLine.append(a)
             b = self.canvas.create_line(self.ofs,i+self.ofs,self.cellSize*self.sideCells+self.ofs+1,i+self.ofs+1)
             self.gridLine.append(b)
      else:
         for i in self.gridLine:
            self.canvas.delete(i)
         self.gridLine.clear()
            
   def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.i = 0
        self.v = tk.StringVar()
        self.v.set(self.i)
        self.ofs = 20
        self.sideCells = 20
        self.cellSize = 20
        self.running = True
        self.showGrid = tk.IntVar()
        self.o = []
        for i in range(0,self.sideCells*self.sideCells):
           self.o.append(0)
        self.gridLine = []
      
        tk.Button(self, text="Once", command=self.Once).pack(side=tk.LEFT)
        tk.Button(self, text="Run", command=self.Start).pack(side=tk.LEFT)
        tk.Button(self, text="Stop", command=self.Stop).pack(side=tk.LEFT)
        tk.Checkbutton(self, text="Grid", variable=self.showGrid, command=self.DrawGrid).pack(side=tk.LEFT)
        tk.Label(self, textvariable=self.v).pack(side=tk.LEFT)
      
        self.canvas = tk.Canvas(root,width=self.sideCells*self.cellSize+30, height=self.sideCells*self.cellSize+30)
        self.canvas.pack()

root = tk.Tk()
root.title("fun 3")
app = Application(master=root)
tk.Button(text="Quit", command=root.destroy).pack(side=tk.BOTTOM)
root.mainloop()
