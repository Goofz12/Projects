import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

class TripartiteGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tripartite Graph Visualization")

        # Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()

        # Draw the tripartite graph
        self.draw_tripartite_graph()

        # Add the Matplotlib canvas to the Tkinter window
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add a button to close the window
        self.close_button = tk.Button(root, text="Close", command=self.close_window)
        self.close_button.pack(side=tk.BOTTOM)

    def draw_tripartite_graph(self):
        # Define vertices in three sets
        set1 = list(range(1, 6))  # Vertices 1 to 5
        set2 = list(range(6, 12))  # Vertices 6 to 11
        set3 = list(range(12, 16))  # Vertices 12 to 15

        # Create a tripartite graph using NetworkX
        G = nx.Graph()
        G.add_nodes_from(set1, bipartite=0)
        G.add_nodes_from(set2, bipartite=1)
        G.add_nodes_from(set3, bipartite=2)

        # Connect vertices between set1 and set2
        edges_set1_set2 = [(1, 7), (2, 8), (3, 6), (4, 10), (5, 9), (4, 11)]
        G.add_edges_from(edges_set1_set2)

        # Connect vertices between set2 and set3
        edges_set2_set3 = [(6, 12), (7, 13), (8, 14), (9, 15), (10, 12), (11, 14)]
        G.add_edges_from(edges_set2_set3)

        # Connect vertices between set1 and set3
        edges_set1_set3 = [(1, 12), (2, 13), (3, 15), (4, 14), (5, 13)]
        G.add_edges_from(edges_set1_set3)

        # Draw the tripartite graph
        pos_set1 = {v: (i, 2) for i, v in enumerate(set1)}  # Position set1 as a row
        pos_set2 = {v: (i + 1, 1) for i, v in enumerate(set2)}  # Position set2 in the middle
        pos_set3 = {v: (i + 1, 0) for i, v in enumerate(set3)}  # Position set3 in the bottom
        pos = {**pos_set1, **pos_set2, **pos_set3}

        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=400, node_color='skyblue', ax=self.ax)

        # Remove x and y axis labels
        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TripartiteGraphApp(root)
    root.mainloop()
