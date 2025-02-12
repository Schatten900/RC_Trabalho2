class Vertex:
    """
    Represents an vertex in a graph, identified by a unique identifier.

    Attributes:
    -----------
        identifier (str): 
            A unique identifier for the vertex.

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