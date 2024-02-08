import tkinter as tk
import math
import random
import timeit

dt = 200

def draw_hull(hull, canvas):
    color = "red"
    canvas.delete("hull")
    for i in range(len(hull) - 1):
        x1, y1 = hull[i]
        x2, y2 = hull[i + 1]
        canvas.create_line(x1, y1, x2, y2, fill=color, tags="hull")
    canvas.after(dt)
    canvas.update()

def cross(a, b, c):
    return (c[0] - a[0]) * (b[1] - a[1]) - (b[0] - a[0]) * (c[1] - a[1])

def Monotonec(points, canvas):
    points = sorted(points)

    if len(points) <= 1:
        return points


    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    draw_hull(lower, canvas)
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    draw_hull(upper, canvas)
    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list.
    hull = []
    for p in lower[:-1]:
        hull.append(p)

    for p in upper:
        hull.append(p)

    draw_hull(hull, canvas)

def choosenearpoints(algorithm):
    window = tk.Toplevel(app)
    window.title(algorithm)
    canvas = tk.Canvas(window, width=800, height=600, bg='white')
    canvas.pack()

    points = []

    def add_point(event):
        x, y = event.x, event.y
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="pink")
        canvas.create_text(x, y - 10, text=f"{x},{y}", fill="black")
        points.append((x, y))

    canvas.bind("<Button-1>", lambda event: add_point(event))

    button_find_hull = tk.Button(window, text=f"Find Convex Hull", command=lambda: Monotonec(points, canvas),
                                bg='lightblue', fg='black')  # Set button background and foreground (text) colors
    button_find_hull.pack()

app = tk.Tk()
app.geometry("400x200")
app.title("Monotone Chain Algorithm")

label = tk.Label(app, text="Monotone Chain Algorithm", bg='lightgreen')
label.pack()

button_find_hull = tk.Button(app, text="Choose Points Manually", command=lambda: choosenearpoints("Monotone Chain"),
                             bg='lightblue', fg='black')  # Set button background and foreground (text) colors
button_find_hull.pack()

app.mainloop()
