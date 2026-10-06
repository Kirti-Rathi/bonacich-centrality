# Bonacich Centrality Analysis

A Python implementation of **Bonacich Power Centrality** (Phillip Bonacich, 1987) for graph and network analysis, built using `NetworkX`, `NumPy`, `SciPy`, and `Matplotlib`.

This project calculates and visualizes Bonacich Centrality scores across famous network datasets, identifying influential nodes and patterns of connectivity in both directed and undirected graphs.

---

## Mathematical Overview

Bonacich Power Centrality measures a node's status or power based on the centralities of the nodes it is connected to. The raw centrality vector $\mathbf{c}$ is computed as:

$$\mathbf{c}(\alpha, \beta) = \alpha (I - \beta A)^{-1} A \mathbf{1}$$

Where:
- $A$ is the adjacency matrix of graph $G$.
- $I$ is the identity matrix of dimension $n \times n$.
- $\mathbf{1}$ is an $n \times 1$ vector of ones.
- $\alpha$ is a scaling parameter (default: `1`).
- $\beta$ is the attenuation factor (default: `0.02`), determining the relative importance of indirect vs. direct connections.
- For directed graphs, $A^T$ can be evaluated to measure **incoming** status (`direction="in"`) instead of **outgoing** influence (`direction="out"`).

The resulting centrality scores are normalized using the Euclidean norm ($L_2$ norm):

$$\hat{\mathbf{c}} = \frac{\mathbf{c}}{\|\mathbf{c}\|_2}$$

---

## 📁 Repository Structure

```
.
├── datasets/
│   ├── dolphins.gml         # Dolphin Social Network (GML format)
│   ├── football.mtx         # American College Football Network (Matrix Market format)
│   ├── polbooks.mtx         # Political Books Network (Matrix Market format)
│   └── reachability.txt.gz  # Reachability dataset
├── main.py                  # Core centrality calculation, evaluation & visualization script
├── .gitignore
└── README.md                # Project documentation
```

---

## 📊 Analyzed Datasets

The script runs analysis on the following sample networks:

1. **Zachary's Karate Club** ($n=34, m=78$)
   - Classic social network graph of a university karate club.
2. **Dolphin Social Network** ($n=62, m=159$)
   - Undirected social network of frequent associations between 62 dolphins living off Doubtful Sound, New Zealand.
3. **American College Football Network** ($n=115, m=615$)
   - Directed network representing games played between Division I college football teams.
4. **Political Books Network** ($n=105, m=441$)
   - Network of books about US politics published around the time of the 2004 presidential election, co-purchased by buyers on Amazon.com.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kirti-Rathi/bonacich-centrality.git
   cd bonacich-centrality
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install networkx numpy matplotlib scipy
   ```

---

## 💻 Usage

### Running the Script

To execute the network analysis and display the top 5 central nodes along with network graphs:

```bash
python main.py
```

### Using `bonacich_centrality` in Your Own Code

```python
import networkx as nx
from main import bonacich_centrality

# Create or load a graph
G = nx.karate_club_graph()

# Compute Bonacich Centrality for all nodes
centrality_scores = bonacich_centrality(G, alpha=1, beta=0.02)

# Query centrality for a specific node
node_0_score = bonacich_centrality(G, alpha=1, beta=0.02, node=0)
print(f"Node 0 Centrality: {node_0_score:.6f}")
```

#### Function Arguments

| Parameter | Type | Default | Description |
|---|---|---|---|
| `G` | `nx.Graph` or `nx.DiGraph` | *Required* | The NetworkX graph object. |
| `alpha` | `float` | `1` | Scaling parameter $\alpha$. |
| `beta` | `float` | `0.02` | Attenuation parameter $\beta$. Must satisfy $(I - \beta A)$ invertibility. |
| `direction` | `str` | `"out"` | For directed graphs: `"out"` for outgoing connections, `"in"` for incoming. |
| `node` | `hashable` | `None` | Optional. If provided, returns centrality for that specific node ID. |

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
