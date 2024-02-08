import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import random


class CheapestLinkTSP:
    def __init__(self, master, num_vertices):
        self.master = master
        self.master.title("Cheapest Link TSP")
        self.num_vertices = num_vertices
        self.graph = self.generate_random_graph()

        self.canvas_frame = ttk.Frame(self.master)
        self.canvas_frame.grid(row=0, column=0)

        self.canvas = FigureCanvasTkAgg(self.plot_graph(), master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()

        ttk.Button(self.master, text="Run Cheapest Link", command=self.run_cheapest_link).grid(row=1, column=0)

    def generate_random_graph(self):
        graph = nx.complete_graph(self.num_vertices)
        for (u, v, d) in graph.edges(data=True):
            d['weight'] = random.randint(1, 10)  # Assign random weights for demonstration
        return graph

    def plot_graph(self):
        plt.clf()
        pos = nx.circular_layout(self.graph)
        nx.draw_networkx_nodes(self.graph, pos)
        nx.draw_networkx_labels(self.graph, pos)
        nx.draw_networkx_edges(self.graph, pos, width=1.0, alpha=0.5, edge_color='b')
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        return plt.gcf()

    def run_cheapest_link(self):
        start_vertex = random.choice(list(self.graph.nodes))
        minimum_spanning_tree, total_weight = self.cheapest_link_algorithm(start_vertex)
        self.highlight_minimum_spanning_tree(minimum_spanning_tree, start_vertex, total_weight)

    def cheapest_link_algorithm(self, start_vertex):
        edges = list(self.graph.edges(data=True))
        edges.sort(key=lambda x: x[2]['weight'])  # Sort edges by weight in ascending order

        minimum_spanning_tree = []
        total_weight = 0
        vertices_with_three_edges = set()

        for edge in edges:
            u, v, data = edge

            # Check for the condition (b) - skip the edge if it results in three edges from a single vertex
            if u in vertices_with_three_edges and v in vertices_with_three_edges:
                continue

            set_u = self.find_set(u, minimum_spanning_tree)
            set_v = self.find_set(v, minimum_spanning_tree)

            if set_u is None or set_v is None or set_u != set_v:
                minimum_spanning_tree.append((u, v, data['weight']))
                total_weight += data['weight']

                # Add vertices to the set with more than two edges if applicable
                if len(self.graph.edges(u)) > 2:
                    vertices_with_three_edges.add(u)
                if len(self.graph.edges(v)) > 2:
                    vertices_with_three_edges.add(v)

        return minimum_spanning_tree, total_weight

    def find_set(self, vertex, minimum_spanning_tree):
        for set_ in minimum_spanning_tree:
            if vertex in set_:
                return set_
        return None

    def highlight_minimum_spanning_tree(self, minimum_spanning_tree, start_vertex, total_weight):
        plt.clf()
        pos = nx.circular_layout(self.graph)
        nx.draw_networkx_nodes(self.graph, pos, nodelist=[start_vertex], node_color='y', node_size=700)
        nx.draw_networkx_labels(self.graph, pos)
        nx.draw_networkx_edges(self.graph, pos, width=1.0, alpha=0.5, edge_color='b')
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        nx.draw_networkx_edges(self.graph, pos, edgelist=minimum_spanning_tree, edge_color='r', width=2.0)

        # Display total weight on the canvas
        self.canvas.get_tk_widget().create_text(20, 20, anchor=tk.NW, text=f'Total Weight: {total_weight}', font=('Arial', 12), fill='black')

        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = CheapestLinkTSP(root, num_vertices=5)
    root.mainloop()
