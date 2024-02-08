import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import random

class NearestNeighborTSP:
    def __init__(self, master, num_vertices):
        self.master = master
        self.master.title("Nearest Neighbor TSP")
        self.num_vertices = num_vertices
        self.graph = self.generate_random_graph()

        self.canvas_frame = ttk.Frame(self.master)
        self.canvas_frame.grid(row=0, column=0)

        self.canvas = FigureCanvasTkAgg(self.plot_graph(), master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()

        ttk.Button(self.master, text="Run Nearest Neighbor", command=self.run_nearest_neighbor).grid(row=1, column=0)

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

    def run_nearest_neighbor(self):
        start_vertex = random.choice(list(self.graph.nodes))
        hamiltonian_cycle, total_weight = self.nearest_neighbor_algorithm(start_vertex)
        self.highlight_hamiltonian_cycle(hamiltonian_cycle, start_vertex, total_weight)

    def nearest_neighbor_algorithm(self, start_vertex):
        unvisited_vertices = set(self.graph.nodes)
        current_vertex = start_vertex
        hamiltonian_cycle = []
        total_weight = 0

        while unvisited_vertices:
            unvisited_neighbors = unvisited_vertices.intersection(self.graph.neighbors(current_vertex))
            if not unvisited_neighbors:
                break

            next_vertex = min(unvisited_neighbors, key=lambda v: self.graph[current_vertex][v]['weight'])
            edge_weight = self.graph[current_vertex][next_vertex]['weight']
            total_weight += edge_weight

            hamiltonian_cycle.append((current_vertex, next_vertex, edge_weight))
            unvisited_vertices.remove(current_vertex)
            current_vertex = next_vertex

        hamiltonian_cycle.append((hamiltonian_cycle[0][0], hamiltonian_cycle[0][1], hamiltonian_cycle[0][2]))  # Close the cycle
        return hamiltonian_cycle, total_weight

    def highlight_hamiltonian_cycle(self, hamiltonian_cycle, start_vertex, total_weight):
        plt.clf()
        pos = nx.circular_layout(self.graph)
        nx.draw_networkx_nodes(self.graph, pos)
        nx.draw_networkx_labels(self.graph, pos)
        nx.draw_networkx_edges(self.graph, pos, width=1.0, alpha=0.5, edge_color='b')
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        hamiltonian_edges = hamiltonian_cycle[:-1]  # Exclude the closing edge for highlighting
        nx.draw_networkx_edges(self.graph, pos, edgelist=hamiltonian_edges, edge_color='r', width=2.0)

        # Highlight the starting vertex in yellow
        nx.draw_networkx_nodes(self.graph, pos, nodelist=[start_vertex], node_color='y', node_size=700)

        # Display total weight on the canvas
        self.canvas.get_tk_widget().create_text(20, 20, anchor=tk.NW, text=f'Total Weight: {total_weight}', font=('Arial', 12), fill='black')

        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = NearestNeighborTSP(root, num_vertices=5)
    root.mainloop()
