import networkx as nx
import matplotlib.pyplot as plt
import graph_search

GreatSac = nx.Graph()

GreatSac.add_node("Sacramento")
GreatSac.add_nodes_from(["Arden", "North Highlands", "Roseville", "Rocklin", "Folsom"])

edges = [("Sacramento", "Arden", {'distance': 8.6}),
         ("Arden", "North Highlands", {'distance': 6.9}),
         ("North Highlands", "Roseville", {'distance': 8}),
         ("Roseville", "Rocklin", {'distance': 619}),
         ("Rocklin", "Folsom", {'distance': 11.7}),
         ("Arden", "Folsom", {'distance': 17})]

GreatSac.add_edges_from(edges)

num_nodes = GreatSac.number_of_nodes()
print("number of nodes:", num_nodes)
num_edges = GreatSac.number_of_edges()
print("number of edges:", num_edges)
is_connected = nx.is_connected(GreatSac)
print("is connected?", is_connected)

degree_centrality = nx.degree_centrality(GreatSac)
print("Degree Centrality:", degree_centrality)
closeness_centrality = nx.closeness_centrality(GreatSac)
print("Closeness Centrality:", closeness_centrality)
betweenness_centrality = nx.betweenness_centrality(GreatSac)
print("Betweenness Centrality:", betweenness_centrality)

print("BFS: ")
graph_search.bfs_iterative(GreatSac, "Rocklin")
print("\nDFS: ")
graph_search.dfs_recursive(GreatSac, "Rocklin")

shortest_paths = nx.single_source_dijkstra_path(GreatSac, source="Sacramento", weight="distance")
print("\nshortest path:", shortest_paths)
shortest_path_lengths = nx.single_source_dijkstra_path_length(GreatSac, source="Sacramento", weight="distance")
print("shortest path lengths:", shortest_path_lengths)

nx.draw(GreatSac, with_labels=True)
plt.show()