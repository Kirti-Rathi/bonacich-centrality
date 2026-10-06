import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import mmread


def bonacich_centrality(G, alpha=1, beta=0.02, direction="out", node=None):
    # A = adjacency matrix
    A = nx.to_numpy_array(G, dtype=float)

    # For directed graphs, choose incoming or outgoing connections
    if direction == "in":
        A = A.T
    elif direction != "out":
        raise ValueError("direction must be 'in' or 'out'")

    n = len(G)

    I = np.eye(n)
    ones = np.ones(n)

    # Raw Bonacich centrality:
    # c = α(I − βA)^(-1) A1
    c = alpha * np.linalg.inv(I - beta * A) @ A @ ones

    # Euclidean normalization
    norm = np.linalg.norm(c, ord=2)

    if norm != 0:
        c = c / norm

    nodes = list(G.nodes())

    centrality = {
        node_id: c[i]
        for i, node_id in enumerate(nodes)
    }

    # If a specific node is requested
    if node is not None:
        if node not in G:
            raise ValueError(f"Node '{node}' is not present in the graph.")

        return centrality[node]

    # Otherwise return centrality of entire network
    return centrality


def print_top_5(centrality):
    # Sort nodes according to centrality, highest first
    sorted_nodes = sorted(
        centrality.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nTop 5 nodes:")
    print("-----------------------------")
    print("Rank\tNode\tCentrality")

    for rank, (node, value) in enumerate(sorted_nodes[:5], start=1):
        print(f"{rank}\t{node}\t{value:.6f}")


def visualize_network(G, centrality, title):
    # Layout
    pos = nx.spring_layout(G, seed=42)

    # Node sizes proportional to centrality
    values = np.array(list(centrality.values()))

    # Scale centrality values for visualization
    node_sizes = 300 + 1500 * (values / values.max())

    # Draw network
    plt.figure(figsize=(10, 8))

    nx.draw_networkx_edges(
        G,
        pos,
        alpha=0.3,
        arrows=G.is_directed()
    )

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_sizes,
        alpha=0.8
    )

    # Find top 5 nodes
    top_5 = sorted(
        centrality.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    top_nodes = [node for node, value in top_5]

    # Label only top 5 nodes
    labels = {
        node: str(node)
        for node in top_nodes
    }

    nx.draw_networkx_labels(
        G,
        pos,
        labels=labels,
        font_size=10,
        font_weight="bold"
    )

    plt.title(title)
    plt.axis("off")
    plt.show()


# 1. Zachary's Karate Club

G = nx.karate_club_graph()

print("========================================")
print("ZACHARY'S KARATE CLUB")
print("========================================")

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

centrality = bonacich_centrality(
    G,
    alpha=1,
    beta=0.02
)

print_top_5(centrality)

visualize_network(
    G,
    centrality,
    "Zachary's Karate Club - Bonacich Centrality"
)


# 2. Dolphin Social Network

D = nx.read_gml("dolphins.gml", label="id")

print("\n========================================")
print("DOLPHIN NETWORK")
print("========================================")

print("Number of nodes:", D.number_of_nodes())
print("Number of edges:", D.number_of_edges())

centrality_dolphins = bonacich_centrality(
    D,
    alpha=1,
    beta=0.02
)

print_top_5(centrality_dolphins)

visualize_network(
    D,
    centrality_dolphins,
    "Dolphin Social Network - Bonacich Centrality"
)


# 3. Football Network

A_football = mmread(
    "football.mtx",
    spmatrix=False
).toarray()

# Keep the network directed
F = nx.from_numpy_array(
    A_football,
    create_using=nx.DiGraph
)

print("\n========================================")
print("FOOTBALL NETWORK")
print("========================================")

print("Number of nodes:", F.number_of_nodes())
print("Number of edges:", F.number_of_edges())

centrality_football = bonacich_centrality(
    F,
    alpha=1,
    beta=0.02,
    direction="out"
)

print_top_5(centrality_football)

visualize_network(
    F,
    centrality_football,
    "Football Network - Bonacich Centrality"
)


# 4. Political Books Network

A_polbooks = mmread(
    "polbooks.mtx",
    spmatrix=False
).toarray()

# Polbooks is an undirected network
P = nx.from_numpy_array(
    A_polbooks,
    create_using=nx.Graph
)

print("\n========================================")
print("POLBOOKS NETWORK")
print("========================================")

print("Number of nodes:", P.number_of_nodes())
print("Number of edges:", P.number_of_edges())

centrality_polbooks = bonacich_centrality(
    P,
    alpha=1,
    beta=0.02
)

print_top_5(centrality_polbooks)

visualize_network(
    P,
    centrality_polbooks,
    "Political Books Network - Bonacich Centrality"
)