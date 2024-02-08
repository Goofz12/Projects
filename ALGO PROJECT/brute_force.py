import tkinter as tk
import random
import timeit
from functools import cmp_to_key


class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


def dist_sq(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise


def compare(p0, p1, p2):
    o = orientation(p0, p1, p2)
    if o == 0:
        if dist_sq(p0, p2) >= dist_sq(p0, p1):
            return -1
        else:
            return 1
    else:
        if o == 2:
            return -1
        else:
            return 1


def draw_convex_hull(lines, canvas, color="red"):
    # Clear previous convex hull lines and highlights
    canvas.delete("convex_hull")

    for i in range(len(lines) - 1):
        p1, p2 = lines[i], lines[i + 1]
        canvas.create_line(
            p1.x, p1.y, p2.x, p2.y, fill=color, width=2, tags="convex_hull"
        )

    # Connect first and last points with a line
    p1, p2 = lines[-1], lines[0]
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill=color, width=2, tags="convex_hull")

    # Highlight points that are part of the convex hull
    for point in lines:
        canvas.create_oval(
            point.x - 2,
            point.y - 2,
            point.x + 2,
            point.y + 2,
            fill=color,
            outline=color,
            tags="convex_hull",
        )


def display_time(time_text, canvas):
    # Clear canvas before displaying elapsed time
    canvas.delete("time_text")

    # Display elapsed time on the canvas
    canvas.create_text(
        250,
        480,
        text=time_text,
        fill="black",
        font=("Helvetica", 12),
        tags="time_text",
    )


def calculate_det(a, b, c):
    return (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x)


def convex_hull_method_1(canvas, points):
    def brute_force():
        if len(points) < 3:
            return
        sorted_points = sorted(points, key=lambda p: (p.x, p.y))
        n = len(sorted_points)
        convex_set = set()

        p0 = min(sorted_points, key=lambda point: (point.y, point.x))

        for i in range(n - 1):
            for j in range(i + 1, n):
                points_left_of_ij = points_right_of_ij = True
                for k in range(n):
                    if k != i and k != j:
                        det_k = calculate_det(
                            sorted_points[i], sorted_points[j], sorted_points[k]
                        )
                        if det_k > 0:
                            points_right_of_ij = False
                        elif det_k < 0:
                            points_left_of_ij = False
                        else:
                            if (
                                sorted_points[k].x < sorted_points[i].x
                                or sorted_points[k].x > sorted_points[j].x
                                or sorted_points[k].y < sorted_points[i].y
                                or sorted_points[k].y > sorted_points[j].y
                            ):
                                points_left_of_ij = points_right_of_ij = False
                                break

                if points_left_of_ij or points_right_of_ij:
                    convex_set.update([sorted_points[i], sorted_points[j]])

        sorted_convex_set = sorted(convex_set, key=lambda p: (p.x, p.y))
        sorted_convex_set = sorted(
            sorted_convex_set, key=cmp_to_key(lambda p1, p2: compare(p0, p1, p2))
        )
        return sorted_convex_set

    start_time = timeit.default_timer()
    hull_points = brute_force()
    end_time = timeit.default_timer()
    elapsed_time = (end_time - start_time) * 1000
    elapsed_time_text = f"Brute Force: {elapsed_time:.2f} ms"

    display_time(elapsed_time_text, canvas)
    draw_convex_hull(hull_points, canvas, "blue")


class PointGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Point Generator")

        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()

        self.generate_button = tk.Button(
            root, text="Generate Random Points", command=self.generate_points
        )
        self.generate_button.pack(pady=10)

        self.clear_button = tk.Button(
            root, text="Clear Canvas", command=self.clear_canvas
        )
        self.clear_button.pack(pady=10)

        self.manual_button = tk.Button(
            root, text="Enable Manual Point", command=self.toggle_manual_point
        )
        self.manual_button.pack(pady=10)

        # Horizontal layout for convex hull methods
        self.horizontal_buttons_frame = tk.Frame(root)
        self.horizontal_buttons_frame.pack()

        self.convex_hull_bf_button = tk.Button(
            self.horizontal_buttons_frame,
            text="Brute Force",
            command=lambda: self.run_algorithm(convex_hull_method_1),
        )
        self.convex_hull_bf_button.pack(side=tk.LEFT, padx=5)

        # Vertical layout for the rest of the buttons
        self.manual_point_enabled = False
        self.canvas.bind("<Button-1>", self.manual_point_click)

        self.points = []

    def run_algorithm(self, algorithm):
        algorithm(self.canvas, self.points)

    def generate_points(self):
        self.clear_canvas()
        self.points = []
        num_points = random.randint(10, 50)
        num_points = random.randint(25, 50)
        for _ in range(num_points):
            x = random.randint(110, 390)
            y = random.randint(110, 390)
            self.points.append(Point(x, y))
            self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.points = []  # Clear the list of points

    def toggle_manual_point(self):
        self.manual_point_enabled = not self.manual_point_enabled
        if self.manual_point_enabled:
            self.manual_button["text"] = "Disable Manual Point"
        else:
            self.manual_button["text"] = "Enable Manual Point"

    def manual_point_click(self, event):
        if self.manual_point_enabled:
            x, y = event.x, event.y
            self.points.append(Point(x, y))
            self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = PointGeneratorApp(root)
    root.mainloop()
