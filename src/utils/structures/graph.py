import math
from collections import defaultdict
from utils.functions.adaptedDijkstra import dijkstra


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
            raise ValueError(f"The provided vertices {vertex1} and {vertex2} are already linked")
        
        #Possivelmente adicionar o melhor caminho ate esse vertice
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
    
    def construct_routing_table(self, start):
        """
        Creates a routing table for the given starting vertex.

        Returns:
        Dictionary mapping each destination to a tuple (next_hop, cost).
        """

        routing_table = {}

        for dest in self.links:
            if dest == start:
                continue

            path_info = dijkstra(self, start, dest)

            if not path_info:  
                routing_table[dest] = (None, math.inf)
                continue
            
            if len(path_info) > 1:
                next_hop = path_info[1][0]
            else:
                next_hop = None

            total_cost = path_info[-1][1]  

            routing_table[dest] = (next_hop, total_cost)

        return routing_table
    
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

    def print_router(self,start):
        """
        Prints the routing table in a readable format.
        """
        
        if start not in self.links:
            print(f"Vertex {start.identifier} is not in the graph.")
            return
        
        print("\routing table:")
        routing_table = self.construct_routing_table(start)

        for dest, (next_hop, cost) in routing_table.items():
            if next_hop:
                print(f"Destination: {dest.identifier}, Next Hop: {next_hop.identifier}, Cost: {cost}s")
            else:
                print(f"Destination: {dest.identifier}, No Route Available")