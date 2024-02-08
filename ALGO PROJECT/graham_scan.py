import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation

class PointNode():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.degree = None
        self.plot = None

    def setDegree(self, degree):
        self.degree = degree

    def setPlot(self, plot):
        self.plot = plot

    def beSelected(self):
        self.plot.set_color("#ff7f0e")

    def beProcessed(self):
        self.plot.set_color("#d62728")

class Graham_scan():
    def __init__(self):
        self.firstPoint = None
        self.points = []
        self.points_stack = []
        self.segment_stack = []
        self.vector_stack = []
        self.ani = None

    def clearPoints(self):
        self.points.clear()

    def clearStructure(self):
        self.points_stack.clear()
        self.segment_stack.clear()
        self.vector_stack.clear()

    def clearPlot(self):
        plt.clf()
        plt.title("Data Distribution", fontsize=14)
        plt.xlabel('x axis', fontsize=10)
        plt.ylabel('y axis', fontsize=10)

        if self.points:
            min_x = min(point.x for point in self.points)
            max_x = max(point.x for point in self.points)
            min_y = min(point.y for point in self.points)
            max_y = max(point.y for point in self.points)

            plt.xlim(min_x - 100, max_x + 100)
            plt.ylim(min_y - 100, max_y + 100)

            for point in self.points:
                point.setPlot(plt.plot(point.x, point.y, 'o', ms=5, color='#1f77b4', alpha=1)[0])

        canvas.draw()

    def gen_data(self):
        self.clearPoints()
        self.clearPlot()

        tempY = 600
        for _ in range(points_num.get()):
            centerX = np.random.randint(-1000, 1000)
            centerY = np.random.randint(-1000, 1000)
            point = PointNode(centerX, centerY)
            point.setPlot(plt.plot(point.x, point.y, 'o', ms=5, color='#1f77b4', alpha=1)[0])

            if centerY <= tempY:
                tempY = centerY
                self.firstPoint = point

            self.points.append(point)

        canvas.draw()

    def start(self):
        self.ani = animation.FuncAnimation(fig=fig, func=self.update, frames=self.frames, init_func=self.init,
                                           interval=1200, blit=False, repeat=False)
        canvas.draw()

    def init(self):

        #remove the first point from the list
        self.points.remove(self.firstPoint)

        #calculate polar angles and sort
        for point in self.points:
            degree = math.degrees(math.atan2(point.y - self.firstPoint.y, point.x - self.firstPoint.x))
            point.setDegree(degree)

        self.points = sorted(self.points, key=lambda point: point.degree)
        # plotting the points and labels
        plt.text(self.firstPoint.x + 35, self.firstPoint.y - 25, "1")
        for index in range(points_num.get() - 1):
            point = self.points[index]
            plt.text(point.x + 35, point.y - 25, str(index + 2))

        #add the first point to the end of the sorted list
        self.points.append(self.firstPoint)

        #connect the lowest point with the second point in sorted order
        secondPoint = self.points[0]
        self.firstPoint.beSelected()
        secondPoint.beSelected()
        self.points_stack.append(self.firstPoint)
        self.points_stack.append(secondPoint)
        self.segment_stack.append(
            plt.plot([self.firstPoint.x, secondPoint.x], [self.firstPoint.y, secondPoint.y], color='#ff7f0e', alpha=1,
                     linestyle="solid")[0])
        self.vector_stack.append(np.array([secondPoint.x - self.firstPoint.x, secondPoint.y - self.firstPoint.y]))

        canvas.draw()

    def update(self, i):
        firstPoint = self.points_stack[-1] #last point added
        secondPoint = self.points[i] #current point being added

        vectorX = self.vector_stack[-1]
        #vector formed by adding first point and last point
        vectorY = np.array([secondPoint.x - firstPoint.x, secondPoint.y - firstPoint.y])

        #if <0 ) then cw
        while (np.cross(vectorX, vectorY) < 0):
            point = self.points_stack.pop()
            point.beProcessed()
            segment = self.segment_stack.pop()
            segment.remove()
            vector = self.vector_stack.pop()
            vector = None

            firstPoint = self.points_stack[-1]
            vectorX = self.vector_stack[-1]
            vectorY = np.array([secondPoint.x - firstPoint.x, secondPoint.y - firstPoint.y])

        #if > 0 then ccw
        if (np.cross(vectorX, vectorY) > 0):
            secondPoint.beSelected()
            self.points_stack.append(secondPoint)
            self.segment_stack.append(
                plt.plot([firstPoint.x, secondPoint.x], [firstPoint.y, secondPoint.y], color='#ff7f0e', alpha=1,
                         linestyle="solid")[0])
            self.vector_stack.append(np.array([secondPoint.x - firstPoint.x, secondPoint.y - firstPoint.y]))

    def frames(self):
        for i in range(1, points_num.get()):
            yield i

    def stop(self):
        self.ani.event_source.stop()
        self.clearStructure()
        self.clearPlot()

        for point in self.points:
            point.setPlot(None)

        for point in self.points:
            point.setPlot(plt.plot(point.x, point.y, 'o', ms=5, color='#1f77b4', alpha=1)[0])

        canvas.draw()

def disable(component):
    component['state'] = 'disable'

def enable(component):
    component['state'] = 'normal'

# GUI
window = tk.Tk()
window.geometry("1600x900")
window.resizable(False, False)
window.title("Graham-scan Algorithm ")
window.configure(bg='#E6E6FA')

points_num = tk.IntVar()
points_num.set(15)

setting1 = tk.Frame(window, bg="#F0FFF0")
setting1.pack(side='top', pady=10)
separator = ttk.Separator(window, orient='horizontal')
separator.pack(side='top', fill=tk.X)
setting2 = tk.Frame(window)
setting2.pack(side='top', pady=10)

fig = plt.figure(figsize=(9, 8))
fig.set_size_inches(4, 4)
canvas = FigureCanvasTkAgg(fig, setting2)
canvas.get_tk_widget().grid()

brain = Graham_scan()
brain.gen_data()

tk.Label(setting1, font=("Calibri", 15, "bold"), text="Number of points:", bg="#F0FFF0").pack(side='left', padx=5)
ent = tk.Entry(setting1, width=5, textvariable=points_num)
ent.pack(side='left')
btn1 = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Generate points', command=lambda: [brain.gen_data()])
btn1.pack(side='left', padx=(10, 5), pady=5)
btn2 = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Start finding convex hull',
                 command=lambda: [brain.start(), disable(btn1), disable(btn2), disable(ent), enable(btn3)])
btn2.pack(side='left', padx=(5, 10), pady=5)
btn3 = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Reset',
                 command=lambda: [brain.stop(), enable(btn1), enable(btn2), enable(ent), disable(btn3)])
btn3.pack(side='left', padx=(5, 10), pady=5)
btn3['state'] = 'disable'

window.mainloop()
