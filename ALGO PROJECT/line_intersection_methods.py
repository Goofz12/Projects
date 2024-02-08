import tkinter as tk
import math
import random
import timeit

dt = 200
    
def drawlinesec(a,b,canvas):
    canvas.create_line(a[0], a[1], b[0], b[1], fill="blue", tags="liness")
    canvas.after(dt)
    canvas.update()

def euclid_dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def choosepoints(algorithm):
    window = tk.Toplevel(app)
    window.title(algorithm)
    canvas = tk.Canvas(window, width=800, height=600, bg='white')
    canvas.pack()

    points = []

    def add_point(event):
        x, y = event.x, event.y
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="pink")
        canvas.create_text(x, y-10,text=f"{x},{y}", fill="black")
        points.append((x,y))

    canvas.bind("<Button-1>", lambda event: add_point(event))
   
    






def choosenearpoints(algorithm):
    window = tk.Toplevel(app)
    window.title(algorithm)
    canvas = tk.Canvas(window, width=800, height=600, bg='white')
    canvas.pack()

    points = []

    

def cross(a, b, c):
    return (c[0] - a[0])*(b[1] - a[1])  - (b[0] - a[0])*(c[1] - a[1])



def lineintersectionalgo(algorithm):
    window = tk.Toplevel(app)
    window.geometry("400x200")
    window.title(algorithm)
    
    button_line_intersection = tk.Button(window, text="CCW", command=lambda: linepoint("CCW"), bg='lightcoral', fg='black')
    button_line_intersection.pack()

    button_line_intersection = tk.Button(window, text="Slopes and Intercept Method", command=lambda: linepoint("Slopes and Intercept Method"), bg='lightcoral', fg='black')
    button_line_intersection.pack()

    button_line_intersection = tk.Button(window, text="Parametric Method", command=lambda: linepoint("Parametric Method"), bg='lightcoral', fg='black')
    button_line_intersection.pack()



def findDistance(a: list, b: list, p: list):
    #rewriting coordinates for simply geometric syntax
    ax, ay, bx, by = a[0], a[1], b[0], b[1]
    px, py = p[0], p[1]
    d = 0
    d = (abs(((bx - ax) * (ay - py)) - ((ax - px) * (by - ay)))) / math.sqrt((pow((bx - ax), 2)) + (pow((by - ay), 2)))
    return d

def isLeft(a: list, b: list, c: list) -> bool:
    #rewriting coordinates for simply geometric syntax
    ax, ay, bx, by, cx, cy = a[0], a[1], b[0], b[1], c[0], c[1]

    #we will take point a and point b and do the cross product of these points
    z = ((bx - ax) * (cy - ay)) - ((cx - ax) * (by - ay))

    if z > 0:
        return True
    else:
        return False
    
def linepoint(algorithm):
    window = tk.Toplevel(app)
    window.title(algorithm)
    canvas = tk.Canvas(window, width=800, height=600, bg='white')
    canvas.pack()

    
    points = []
    

    def add_point(event):
        
        if len(points)<4:
            x, y = event.x, event.y
            canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="pink")
            canvas.create_text(x, y-10,text=f"{x},{y}", fill="black")
            points.append((x,y))
            
            if len(points)%2==0:
                drawlinesec(points[-1],points[-2],canvas)
                
        else:
            label1 = tk.Label(window, text="Cannot take more than 4 points", bg='red1')  
            label1.pack()
       

    canvas.bind("<Button-1>", lambda event: add_point(event))
    button_find_hull = tk.Button(window, text=f"Check if the lines intersect", command=lambda: chooseinterslgo(algorithm,window,points), bg='lightblue', fg='black')  # Set button background and foreground (text) colors
    button_find_hull.pack()
    button_find_hull = tk.Button(window, text=f"Reset Points", command=lambda: reseting(algorithm,window,canvas,points), bg='lightblue', fg='black')  # Set button background and foreground (text) colors
    button_find_hull.pack()

def reseting(algorithm,window,canvas,points):
    points.clear()
    canvas.delete("all")
    
    def add_point(event):
        
        if len(points)<4:
            x, y = event.x, event.y
            canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="pink",tag = "all")
            canvas.create_text(x, y-10,text=f"{x},{y}", fill="black",tag = "all")
            points.append((x,y))
            
            if len(points)%2==0:
                drawlinesec(points[-1],points[-2],canvas)
                
        else:
            label1 = tk.Label(window, text="Cannot take more than 4 points", bg='red1')  
            label1.pack()
       
    canvas.bind("<Button-1>", lambda event: add_point(event))
    algos1[algorithm](points, window)

def chooseinterslgo(algorithm,window,points):
    algos1[algorithm](points, window)

def intersectionccw(points,window):
    if len(points)<4:
        label1 = tk.Label(window, text="Choose 4 points", bg='red1')  
        label1.pack()
        return 0
    
    starttime = timeit.default_timer()
        
    test1 = cross(points[0],points[1],points[2]) * cross(points[0],points[1],points[3])
    test2 = cross(points[2],points[3],points[0]) * cross(points[2],points[3],points[1])
    
    if test1<=0 & test2<=0:
        label1 = tk.Label(window, text="Line Intersct", bg='lightgreen')  
        label1.pack()
        endtime = timeit.default_timer() - starttime
        label1 = tk.Label(window, text=f"Method CCW took {endtime:.5f} ms", bg='lightgreen')  
        label1.pack()
    else:
        label1 = tk.Label(window, text="Line DO NOT Intersct", bg='lightgreen')  
        label1.pack()
        endtime = timeit.default_timer() - starttime
        label1 = tk.Label(window, text=f"Method CCW took {endtime:.5f} ms", bg='lightgreen')  
        label1.pack()
        
def slopes(points,window):
    if len(points)<4:
        label1 = tk.Label(window, text="Choose 4 points", bg='red1')  
        label1.pack()
        return 0
    
    starttime = timeit.default_timer()
    slope1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) if (points[1][0] - points[0][0]) != 0 else float("inf")
    slope2 = (points[3][1] - points[2][1]) / (points[3][0] - points[2][0]) if (points[3][0] - points[2][0]) != 0 else float("inf")

    if slope1 != slope2:
        # Check if intersection point is within the range of both line segments
        intersect_x = (points[2][1] - points[0][1] + slope1 * points[0][0] - slope2 * points[2][0]) / (slope1 - slope2)
        intersect_y = slope1 * (intersect_x - points[0][0]) + points[0][1]

        if (
            min(points[0][0], points[1][0]) <= intersect_x <= max(points[0][0], points[1][0])
            and min(points[0][1], points[1][1]) <= intersect_y <= max(points[0][1], points[1][1])
            and min(points[2][0], points[3][0]) <= intersect_x <= max(points[2][0], points[3][0])
            and min(points[2][1], points[3][1]) <= intersect_y <= max(points[2][1], points[3][1])
        ):
            label2 = tk.Label(window, text="Line Intersct", bg='lightgreen')  
            label2.pack()
            endtime = timeit.default_timer() - starttime
            label1 = tk.Label(window, text=f"Method Slopes and Intercept took {endtime:.5f} ms", bg='lightgreen')  
            label1.pack()
            return 0

    label1 = tk.Label(window, text="Line DO NOT Intersct", bg='lightgreen')  
    label1.pack()
    endtime = timeit.default_timer() - starttime
    label1 = tk.Label(window, text=f"Method Slopes and Intercept took {endtime:.5f} ms", bg='lightgreen')  
    label1.pack()
    return 0

def parametric(points,window):
    if len(points)<4:
        label1 = tk.Label(window, text="Choose 4 points", bg='red1')  
        label1.pack()
        return 0
    
    starttime = timeit.default_timer()
    dx1 = points[1][0] - points[0][0]
    dy1 = points[1][1] - points[0][1]
    dx2 = points[3][0] - points[2][0]
    dy2 = points[3][1] - points[2][1]

    determinant = dx1 * dy2 - dx2 * dy1

    if determinant == 0:
        # The lines are parallel, and intersection is not possible
        label1 = tk.Label(window, text="Line DO NOT Intersct", bg='lightgreen')  
        label1.pack()
        endtime = timeit.default_timer() - starttime
        label1 = tk.Label(window, text=f"Method Parametric took {endtime:.5f} ms", bg='lightgreen')  
        label1.pack()
        return 0
        

    # Solve for t and s
    t = ((points[2][0] - points[0][0]) * dy2 - (points[2][1] - points[0][1]) * dx2) / determinant
    s = ((points[2][0] - points[0][0]) * dy1 - (points[2][1] - points[0][1]) * dx1) / determinant

    # Check if the values of t and s are in the range [0, 1]
    if 0 <= t <= 1 and 0 <= s <= 1:
        label2 = tk.Label(window, text="Line Intersct", bg='lightgreen')  
        label2.pack()
        endtime = timeit.default_timer() - starttime
        label1 = tk.Label(window, text=f"Method Parametric took {endtime:.5f} ms", bg='lightgreen')  
        label1.pack()
        return 0

    label1 = tk.Label(window, text="Line DO NOT Intersct", bg='lightgreen')  
    label1.pack()
    endtime = timeit.default_timer() - starttime
    label1 = tk.Label(window, text=f"Method Parametric took {endtime:.5f} ms", bg='lightgreen')  
    label1.pack()
    return 0
    
algos1 = {"CCW" : intersectionccw,"Slopes and Intercept Method":slopes,"Parametric Method":parametric}
app = tk.Tk()
app.geometry("400x200")
app.title("Geometric Algorithms")


label = tk.Label(app, text="Homepage - Select an Algorithm", bg='lightgreen')  
label.pack()

button_line_intersection = tk.Button(app, text="Line Intersection", command=lambda: lineintersectionalgo("Line Intersection"), bg='lightcoral', fg='black')
button_line_intersection.pack()

app.mainloop()