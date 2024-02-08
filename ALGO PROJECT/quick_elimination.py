import tkinter as tk
from math import sqrt

NUM_POINTS = 20
SLOWDOWN_PER_STEP = 500  # Adjust the speed of visualization

win = tk.Tk()
win.title("QuickHull Visualization")
win.geometry("800x600")  # Adjust the window size

canvas = tk.Canvas(win, width=800, height=500, bg="white")  # Adjust the canvas size
canvas.pack()

pointList = []

def add_point(event):
    x, y = event.x, event.y
    pointList.append([x, y])
    draw_point([x, y], size=6)  # Adjust the size of the points

def generate_convex_hull():
    global pointList
    pointList.sort(key=lambda p: p[0])  # Sort points based on x-coordinate
    ch_result = quickHull(pointList)
    print("Final Convex Hull Points: ")
    print(ch_result)

def quickHull(pList):
    for i in pList:
        draw_point(i, size=6)  # Adjust the size of the points

    convexHullList = quickHullHelper(pList)

    print("Convex Hull Points: ")
    print(convexHullList)

    return convexHullList

def quickHullHelper(pList):
    if len(pList) <= 1:
        return pList

    leftPoint, rightPoint = pList[0], pList[-1]
    convexHullList = [leftPoint, rightPoint]

    draw_point(leftPoint, color="yellow", size=8)  # Adjust the size of the points
    draw_point(rightPoint, color="yellow", size=8)  # Adjust the size of the points
    draw_line(leftPoint, rightPoint)
    win.update()
    win.after(SLOWDOWN_PER_STEP)

    upperHullPoints = upperHull(leftPoint, rightPoint, pList)
    lowerHullPoints = upperHull(rightPoint, leftPoint, pList)

    convexHullList += upperHullPoints
    convexHullList += lowerHullPoints

    return convexHullList

def upperHull(a, b, pList):
    if len(pList) == 0:
        return []

    upperHullPoints = []
    resultPoints = []

    maxDis = 0.0
    furthestPoint = []

    for p in pList:
        if isRight(a, b, p):  # Adjusted to find points on the right side
            upperHullPoints.append(p)
            pDis = findDistance(a, b, p)
            print(pDis)
            if pDis > maxDis:
                maxDis = pDis
                furthestPoint = p
    print("Max Distance = ", maxDis)
    print("Furthest Point is ", furthestPoint)

    if furthestPoint:
        resultPoints.append(furthestPoint)
        draw_point(furthestPoint, color="yellow", size=8)  # Adjust the size of the points
        draw_line(a, furthestPoint)
        draw_line(b, furthestPoint)
        win.update()
        win.after(SLOWDOWN_PER_STEP)

    region1 = upperHull(a, furthestPoint, upperHullPoints)
    region3 = upperHull(furthestPoint, b, upperHullPoints)

    resultPoints += region1
    resultPoints += region3

    return resultPoints

def draw_point(p, color="blue", size=4):  # Adjust the default size of the points
    x, y = p[0], p[1]
    canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
    win.update()
    win.update_idletasks()
    win.after(SLOWDOWN_PER_STEP)

def draw_line(a, b):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    canvas.create_line(ax, ay, bx, by)
    win.update()
    win.update_idletasks()
    win.after(SLOWDOWN_PER_STEP)

def findDistance(a, b, p):
    ax, ay, bx, by = a[0], a[1], b[0], b[1]
    px, py = p[0], p[1]
    d = (abs(((bx - ax) * (ay - py)) - ((ax - px) * (by - ay)))) / sqrt((pow((bx - ax), 2)) + (pow((by - ay), 2)))
    return d

def isRight(a, b, c):
    ax, ay, bx, by, cx, cy = a[0], a[1], b[0], b[1], c[0], c[1]
    z = ((bx - ax) * (cy - ay)) - ((cx - ax) * (by - ay))
    return z < 0  # Adjusted to check if a point is on the right side

canvas.bind("<Button-1>", add_point)

generate_button = tk.Button(win, text="Generate Convex Hull", command=generate_convex_hull)
generate_button.pack()

win.mainloop()
