from utils.functions.defineLinkProperties import define_link_properties
from utils.structures.vertex import Vertex
from utils.structures.graph import Graph

def construct_graph(major_subnets, conections_in_same_router, host_subnets) -> tuple[Graph, dict]:
    """
    Constructs a graph from multiple adjacency structures.

    This function builds a `Graph` object using:
    - `major_subnets`: Links between main network components (routers/switches).
    - `conections_in_same_router`: Links within the same router/switch.
    - `host_subnets`: Links between switches and their connected hosts.

    Parameters:
    -----------
    major_subnets (dict):
        - Keys (str): Main vertices (routers, switches).
        - Values (tuple of str): Adjacent vertices connected to the key.
        
    conections_in_same_router (dict):
        - Keys (str): Routers/switches with multiple internal links.
        - Values (tuple of str): Other interfaces within the same router.

    host_subnets (dict):
        - Keys (str): Switches of edge layer (E1, E2, etc.).
        - Values (tuple of str): Hosts directly connected to the switch.

    Returns:
    --------
    graph:
        A `Graph` object representing the network topology.
    vertex_map:
        A dictionary containing all the `Vertex` objects.
    """

    graph = Graph()
    vertex_map = {}

    def get_or_create_vertex(vertex_id):
        if vertex_id not in vertex_map:
            vertex_map[vertex_id] = Vertex(vertex_id)
        return vertex_map[vertex_id]

    for main_vertex, adj_vertices in major_subnets.items():
        main_vm = get_or_create_vertex(main_vertex)
        link = define_link_properties("major subnet")
        for adj in adj_vertices:
            adj_vm = get_or_create_vertex(adj)
            graph.link_vertices(main_vm, adj_vm, link)

    for main_vertex, adj_vertices in conections_in_same_router.items():
        main_vm = get_or_create_vertex(main_vertex)
        link = define_link_properties("same router")
        for adj in adj_vertices:
            adj_vm = get_or_create_vertex(adj)
            graph.link_vertices(main_vm, adj_vm, link)

    for switch, hosts in host_subnets.items():
        switch_vm = get_or_create_vertex(switch)
        link = define_link_properties("host subnet")
        for host in hosts:
            host_vm = get_or_create_vertex(host)
            graph.link_vertices(switch_vm, host_vm, link)

    return graph, vertex_map