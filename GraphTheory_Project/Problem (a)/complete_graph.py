import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

# Create a complete graph with 12 vertices
G = nx.complete_graph(12)

# Create a Tkinter window
root = tk.Tk()
root.title("Complete Graph Visualization")

# Function to close the Tkinter window
def close_window():
    root.destroy()

# Matplotlib figure
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

# Draw the graph
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', edge_color='black', ax=ax)

# Add the Matplotlib canvas to the Tkinter window
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Add a button to close the window
close_button = tk.Button(root, text="Close", command=close_window)
close_button.pack(side=tk.BOTTOM)

# Run the Tkinter event loop
root.mainloop()