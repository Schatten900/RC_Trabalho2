from utils.functions.defineLinkProperties import define_link_properties
from utils.structures.vertex import Vertex
from utils.structures.graph import Graph

def construct_graph(adjacent_vertices) -> Graph | dict:
    """
    Constructs a graph from an adjacency list representation.

    This function creates a `Graph` object using an adjacency list (`adjacent_vertices`). 
    Each vertex in the graph is instantiated as a `Vertex` object, and connections 
    between vertices are established based on the provided adjacency structure.

    The function also assigns link properties to each main vertex using 
    `define_link_properties()`, which defines the transmission distance and rate.

    Parameters:
    -----------
    adjacent_vertices (dict):
        A dictionary representing the adjacency list of the graph, where:
        - Keys (str): Main vertices.
        - Values (tuple of str): The adjacent vertices connected to the key.

    Returns:
    --------
    graph:
        A `Graph` object representing the constructed structure.
    vertex_map:
        A dict that contains the vertices of the graph.
    """

    graph = Graph()
    vertex_map = {}

    for mainVertex, adjsVertices in adjacent_vertices.items():
        link = define_link_properties(mainVertex)

        if mainVertex not in vertex_map:
            vertex_map[mainVertex] = Vertex(mainVertex)

        vm = vertex_map[mainVertex]

        for v in adjsVertices:
            if v not in vertex_map:
                vertex_map[v] = Vertex(v)
            
            adjV = vertex_map[v] 
            graph.link_vertices(vm, adjV, link)

    return graph, vertex_map