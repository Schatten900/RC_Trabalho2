from utils.structures.link import Link

def define_link_properties(vertex) -> Link:
    """
    Defines and returns the link properties for a given vertex.

    This function assigns a `Link` object to a given vertex based on predefined 
    distance and transmission rate values. The properties of the link vary 
    depending on the type of vertex.

    Parameters:
    -----------
    vertex (str): 
        The vertex for which the link properties should be defined.

    Returns:
    --------
    Link: 
        An instance of the `Link` class containing:
        - `distance` (int): The physical distance of the link in meters.
        - `transmissionRate` (int): The transmission rate of the link in bits per second (bps).
    """
    
    if vertex == 'CORE':
        link = Link(
            distance = 1000000,  # 1000 KM
            transmissionRate = 100000000  # 100 MB/s
        )
    elif vertex in ('A1', 'A2'):
        link = Link(
            distance = 1000000000,  # 1000 KM
            transmissionRate = 1000000000  # 1000 MB/s
        )
    elif vertex in ('E1', 'E4'):
        link = Link(
            distance = 10000,  # 10 KM
            transmissionRate = 300000000  # 300 MB/s
        )
    elif vertex in ('E2', 'E3'):
        link = Link(
            distance = 30000,  # 30 KM
            transmissionRate = 200000000  # 200 MB/s
        )
    else:
        raise ValueError(f"Vertex '{vertex}' not recognized in link definitions.")

    return link