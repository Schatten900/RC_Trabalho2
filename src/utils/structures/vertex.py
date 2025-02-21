class Vertex:
    """
    Represents an vertex in a graph, identified by a unique identifier.

    Attributes:
    -----------
        identifier (str): 
            A unique identifier for the vertex.
        routing_table : dict
            A dictionary that stores the shortest paths to other vertices.
            ex: {vertex1: [(next_hop, cost), (next_hop, cost), ...], ...}

    Methods:
    --------
        __init__(identifier: str):
            Initializes an vertex object with a unique identifier.
    """

    def __init__(self, identifier: str = None):
        """
        Initializes an vertex with a unique identifier.

        Parameters:
        -----------
            identifier (str): 
                A unique identifier for the vertex.
        """

        if identifier is None:
            raise ValueError("Identifier of vertex not provided")

        self.identifier = identifier
        self.routing_table = {}
    
    def next_hop(self, destiny):
        """
        Returns the next hop to a given destiny.

        Parameters:
        -----------
            destiny (Vertex):
                The destiny vertex to which the next hop is required.
        """

        if destiny not in self.routing_table:
            raise ValueError(f"Destiny {destiny} not in routing table")

        return self.routing_table[destiny][1][0]