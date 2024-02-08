import tkinter as tk
import math
import time


class ConvexHullJarvisMarch(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.points = []
        self.drawing = False
        self.canvas = tk.Canvas(self, bg="white", width=500, height=500)
        self.canvas.pack(side=tk.TOP)
        button_panel = tk.Frame(self)
        draw_button = tk.Button(button_panel, text="Draw Lines", command=self.draw_lines)
        draw_button.pack(side=tk.LEFT)
        button_panel.pack(side=tk.BOTTOM)
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if not self.drawing:
            self.points.append((event.x, event.y))
            self.canvas.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill="blue")
            self.canvas.update()

    def draw_lines(self):
        if len(self.points) > 1:
            self.drawing = True

            hull = []
            po = None
            min_y = 0

            for point in self.points:
                if min_y < point[1]:
                    min_y = point[1]
                    po = point

            for point in self.points:
                self.canvas.create_oval(point[0] - 2, point[1] - 2, point[0] + 2, point[1] + 2, fill="blue")
                self.canvas.update()

            time.sleep(1)

            while True:
                hull.append(po)
                next_point = self.points[0]

                self.animate_in(po, next_point)
                for point_set in self.points:
                    c = self.ccw(point_set, next_point, po)
                    if next_point == po or c == -1 or (c == 0 and self.dist(po, point_set) > self.dist(po, next_point)):
                        self.animate_out(next_point, point_set)
                        self.animate_out(po, next_point)
                        next_point = point_set
                        self.animate_in(po, next_point)

                self.animate_in(po, next_point)
                po = next_point
                if po == hull[0]:
                    break

            for i in range(len(hull)):
                if i == len(hull) - 1:
                    break
                time.sleep(0.5)
                self.canvas.create_line(hull[i][0], hull[i][1], hull[i + 1][0], hull[i + 1][1], fill="blue")
                self.canvas.update()

            time.sleep(0.5)
            self.canvas.create_line(hull[-1][0], hull[-1][1], hull[0][0], hull[0][1], fill="blue")
            self.canvas.update()

    def animate_in(self, p1, p2):
        time.sleep(0.02)
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1])

    def animate_out(self, p1, p2):
        time.sleep(0.02)
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="white")

    def dist(self, po, next_point):
        return int(math.sqrt(math.pow(next_point[1] - po[1], 2) + math.pow(next_point[0] - po[0], 2)))

    def ccw(self, p1, p2, p3):
        num = (p3[1] - p2[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0


if __name__ == "__main__":
    app = ConvexHullJarvisMarch()
    app.mainloop()




















