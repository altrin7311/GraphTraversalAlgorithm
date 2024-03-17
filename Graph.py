import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def visualize_graph(graph, pos, connected_text, current_node=None):
    # Draw the graph with a circular layout for better aesthetics
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=800, node_color='skyblue', edge_color='gray', font_size=10, width=2.0)

    if current_node is not None:
        # Highlight the current node
        nx.draw_networkx_nodes(graph, pos, nodelist=[current_node], node_color='red', node_size=1000)

    # Display arrows with blunt edges
    for edge in graph.edges:
        arrow_pos = pos[edge[0]], pos[edge[1]]
        plt.arrow(*arrow_pos[0], arrow_pos[1][0] - arrow_pos[0][0], arrow_pos[1][1] - arrow_pos[0][1],
                  shape='full', lw=0, length_includes_head=True, head_width=0.05, overhang=0.2, color='red')

    # Display text indicating whether the graph is connected
    plt.text(0.95, 0.95, connected_text, horizontalalignment='right', verticalalignment='top', transform=ax.transAxes, fontsize=17, color='blue')

if __name__ == "__main__":
    graph = nx.Graph()
    input_values = []

    while True:
        edge_str = input("Enter an edge as 'node1 node2' (or type 'done' to finish): ")
        if edge_str.lower() == 'done':
            break

        try:
            node1, node2 = map(int, edge_str.split())
            graph.add_edge(node1, node2)
            input_values.extend([node1, node2])

        except ValueError:
            print("Invalid input. Please enter two space-separated integers.")

    # Calculate positions using circular layout for better aesthetics
    pos = nx.circular_layout(graph)

    fig, ax = plt.subplots(figsize=(10, 10))
    connected_text = ""

    connected_components = list(nx.connected_components(graph))
    if len(connected_components) == 1:
        connected_text = "Connected"
    else:
        connected_text = "Not Connected"

    # Remove the frame and set the background color
    ax.set_axis_off()
    fig.patch.set_facecolor('white')  # Set background color

    def update(frame):
        ax.clear()
        current_node = frame
        exploration_edges = list(nx.dfs_edges(graph, source=current_node))
        visualize_graph(graph, pos, connected_text, current_node)
        nx.draw_networkx_edges(graph, pos, edgelist=exploration_edges, edge_color='red', width=2.5, ax=ax)

    ani = FuncAnimation(fig, update, frames=list(graph.nodes), repeat=False, interval=1000)
    plt.show()
