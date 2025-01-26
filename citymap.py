import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
city_map = nx.Graph()

# Add nodes (intersections)
city_map.add_nodes_from([
    (1, {"name": "Intersection 1"}),
    (2, {"name": "Intersection 2"}),
    (3, {"name": "Intersection 3"}),
    (4, {"name": "Intersection 4"}),
    (5, {"name": "Intersection 5"})
])

# Add edges (roads) with distances
city_map.add_weighted_edges_from([
    (1, 2, 7),
    (1, 3, 9),
    (1, 6, 14),
    (2, 3, 10),
    (2, 4, 15),
    (3, 4, 11),
    (3, 6, 2),
    (4, 5, 6),
    (5, 6, 9)
])

# Find the shortest path between two intersections
start = 1
end = 5
shortest_path = nx.shortest_path(city_map, source=start, target=end, weight='weight')
path_length = nx.shortest_path_length(city_map, source=start, target=end, weight='weight')

print(f"The shortest path from Intersection {start} to Intersection {end} is: {shortest_path}")
print(f"The length of this path is: {path_length}")

# Draw the graph
pos = nx.spring_layout(city_map)
nx.draw(city_map, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(city_map, 'weight')
nx.draw_networkx_edge_labels(city_map, pos, edge_labels=labels)
plt.show()
