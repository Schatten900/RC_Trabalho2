from utils.functions.adaptedDijkstra import dijkstra
from collections import defaultdict

class Graph:
    def __init__(self):
        """
        Initializes a graph structure with linked connections.
        
        Attributes:
        -----------
            links (dict): 
                A dictionary storing vertices as keys and a list of tuples 
                (linked vertex, link) as values.
        """

        self.links = defaultdict(list)
        self.vertices = []

    def link_vertices(self, vertex1, vertex2, link):
        """
        Links two vertices together through a shared link.
        OBS: The connections are bidirectional. 

        Parameters:
        -----------
            vertex1: 
                The first vertex to be linked.
            vertex2:
                The second vertex to be linked.
            link: 
                The link that connects the two vertices.
        """

        if self.is_linked(vertex1=vertex1, vertex2=vertex2):
            self.links[vertex1].remove(vertex2) 
            self.links[vertex2].remove(vertex1)
        
        self.links[vertex1].append((vertex2, link)) 
        self.links[vertex2].append((vertex1, link))            

    def is_linked(self, vertex1, vertex2) -> bool:
        """
        Checks if two vertices are already linked.

        Returns:
            bool: True if vertices are already linked, False if not.
        """

        connections = self.links[vertex1]
        for v, _ in connections:
            if v == vertex2:
                return True
        
        return False
    
    def construct_routings_tables(self, vertex_map):
        """
        Builds the routing table for each vertex in the graph.

        For each vertex in the graph, this function computes the shortest path 
        to all other vertices using Dijkstra's algorithm and stores the results 
        in the vertex's routing table.

        The routing table is updated with the shortest path from the current 
        vertex to every other vertex in the graph.

        Parameters:
        -----------
            None

        Returns:
        --------
            None
        """

        for i in range(len(self.vertices)):
            vertex = vertex_map[self.vertices[i]]

            for j in range(len(self.vertices)):
                vertex.routing_table[self.vertices[j]] = dijkstra(graph=self, start=vertex, end=vertex_map[self.vertices[j]])

    def print_graph(self):
        """
        Prints the graph structure in a readable format.
        """

        print("\nGraph Structure:")

        for vertex, connections in self.links.items():
            print(f"{vertex.identifier} ->")

            for adj_vertex, link in connections:
                distance = link.distance
                rate = link.transmissionRate
                print(f"    - Connected to: {adj_vertex.identifier}, Distance: {distance}m, Rate: {rate}bps")

        print()