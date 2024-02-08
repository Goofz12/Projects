import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

class BipartiteGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bipartite Graph Visualization")

        # Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()

        # Draw the bipartite graph
        self.draw_bipartite_graph()

        # Add the Matplotlib canvas to the Tkinter window
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add a button to close the window
        self.close_button = tk.Button(root, text="Close", command=self.close_window)
        self.close_button.pack(side=tk.BOTTOM)

    def draw_bipartite_graph(self):
        # Define vertices in two sets
        set1 = list(range(1, 6))  # Vertices 1 to 5
        set2 = list(range(6, 12))  # Vertices 6 to 11

        # Create a bipartite graph using NetworkX
        G = nx.Graph()
        G.add_nodes_from(set1, bipartite=0)
        G.add_nodes_from(set2, bipartite=1)

        edges = [(1, 7), (2, 8), (3, 6), (4, 10), (5, 9), (4, 11)]
        G.add_edges_from(edges)

        # Draw the bipartite graph
        pos_set1 = {v: (1, i) for i, v in enumerate(set1)}
        pos_set2 = {v: (2, i) for i, v in enumerate(set2)}
        pos = {**pos_set1, **pos_set2}

        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=400, node_color='skyblue', ax=self.ax)

        # Remove x and y axis labels
        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BipartiteGraphApp(root)
    root.mainloop()
