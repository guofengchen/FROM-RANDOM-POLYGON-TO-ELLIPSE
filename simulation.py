#coding: utf-8

"""Small fun simulation script for paper FROM RANDOM POLYGON TO ELLIPSE: AN EIGENANALYSIS
@author:chenguofeng08qh@gmail.com
"""
import Tkinter
import random
import time

def simulation(event):
    points = []
    for i in range (30):
        x = random.uniform(0,1000)
        y = random.uniform(0,800)
        points.append([x,y])
    n = len(points)
    for i in range(n):
        w.create_rectangle(points[i][0],points[i][1],points[i][0],points[i][1], fill ="red")
        w.create_line(points[i][0],points[i][1],points[(i+1)%n][0],points[(i+1)%n][1],fill="red", dash=(4, 4))
    for times in range(300):
        temppoints = []    
        for i in range (n):
            x = (points[i][0] + points[(i+1)%n][0])/2.0 
            y = (points[i][1] + points[(i+1)%n][1])/2.0
            w.create_rectangle(x,y,x,y, fill ="red")
            temppoints.append([x,y])
        points = temppoints
        w.delete("all")
        for i in range(n):
            w.create_line(points[i][0],points[i][1],points[(i+1)%n][0],points[(i+1)%n][1],fill="red", dash=(4, 4))
root = Tkinter.Tk()
w = Tkinter.Canvas(root, width=1280, height=9600, bg = 'white')
w.pack()

root.minsize(1000,800)
root.maxsize(1000,800)
root.bind('<Button-1>', simulation)
root.title("Press on the scene to do the simulation again!")
root.mainloop()

