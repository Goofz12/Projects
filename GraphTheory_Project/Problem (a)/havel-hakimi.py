import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

# Create a simple graph with 12 vertices
G = nx.cycle_graph(10)

# Create a Tkinter window
root = tk.Tk()
root.title("Simple Graph Visualization")

# Function to close the Tkinter window
def close_window():
    root.destroy()

# Function to apply the Havel-Hakimi algorithm
def havel_hakimi():
    global degrees
    # Get the degrees of the graph
    degrees = list(dict(G.degree()).values())

    # Sort the degrees in descending order
    degrees.sort(reverse=True)

    # Check if the sequence is graphical
    if all(degrees):
        update_graph()
        havel_hakimi_step()
    else:
        print("No graphical representation exists for the given degree sequence.")

# Function to apply one step of the Havel-Hakimi algorithm
def havel_hakimi_step():
    global degrees
    # If any degree is greater than or equal to zero, continue
    if any(degrees):
        # Arrange in descending order
        degrees.sort(reverse=True)
        print(f"Current Degree Sequence: {degrees}")
        root.after(1000, lambda: subtract_one(degrees))
    else:
        print("Graphical representation exists.")

# Function to subtract one from the degrees
# Function to subtract one from the degrees
def subtract_one(degrees):
    global G
    k = degrees.pop(0)
    degrees[:k] = [d - 1 for d in degrees[:k]]
    print(f"Current Degree Sequence: {degrees}")
    update_graph()
    root.after(1000, lambda: havel_hakimi_step())


# Function to update the graph visualization
def update_graph():
    # Update the graph with the new degrees
    nx.set_node_attributes(G, dict(enumerate(degrees, start=1)), 'degree')

    # Update the visualization
    ax.clear()
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', ax=ax)

    # Refresh the canvas
    canvas.draw()

# Matplotlib figure
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

# Draw the graph
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', ax=ax)

# Add the Matplotlib canvas to the Tkinter window
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Add a button to apply Havel-Hakimi algorithm
havel_button = tk.Button(root, text="Apply Havel-Hakimi", command=havel_hakimi)
havel_button.pack(side=tk.TOP)

# Add a label for displaying results
# result_label = tk.Label(root, text="")  # Commented out the result_label

# Add a button to close the window
close_button = tk.Button(root, text="Close", command=close_window)
close_button.pack(side=tk.BOTTOM)

# Run the Tkinter event loop
root.mainloop()
