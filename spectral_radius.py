import argparse 
import networkx as nx
import numpy as np

def load_graph(path):
    """ 
    Load a graph from a file.
    """
    G = nx.read_edgelist(path)
    return G

def compute_adjacency_matrix(G):
    """ 
    Compute the adjacency matrix of a graph.
    """
    return nx.to_numpy_array(G)

def estimate_spectral_radius(adj_matrix):
    """ 
    Estimate the spectral radius of a graph.
    """
    return np.max(abs(np.linalg.eigvals(adj_matrix)))

def main():
    """ 
    handles CLI parsing and calling the other functions.  
    """ 
    parser = argparse.ArgumentParser( 
        description="Estimate the spectral radius of a graph."
    ) 

    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the edgelist file."
    ) 

    parser.add_argument(
        "--directed",
        action="store_true",
        help="Treat the graph as directed."
    )  

    parser.add_argument(
        "--sparse   ",
        action="store_true",
        help="Use sparse matrix representation."
    ) 

    args = parser.parse_args()
    
    G = load_graph(args.file)
    adj_matrix = compute_adjacency_matrix(G)
    spectral_radius = estimate_spectral_radius(adj_matrix)
    print(f"Spectral radius: {spectral_radius}")  
    



