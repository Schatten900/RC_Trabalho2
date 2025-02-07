import heapq
import math

def dijkstra(graph, start, end):
    """
    Finds the shortest-time path in 'graph' between 'start' and 'end'.
    Avoids comparing Vertex objects by including a tie-breaker in the heap.

    Parameters:
    -----------
    graph: 
        An object that has 'graph.links' where 'links' is a dict of the form:
            { Vertex: [(Vertex, Link), (Vertex, Link), ...], ... }
    start: Vertex
        The starting vertex.
    end: Vertex
        The target vertex.

    Returns:
    --------
    path_info: list of (Vertex, float)
        A list of tuples (vertex, accumulated_cost). The last vertex in the
        list is 'end' with the total cost to get there. If no path is found,
        returns an empty list.

    Obs:
    ----
    - We assume 'Link.calculate_delay(packet_size_bits)' returns the time
      (in seconds) to traverse that link with a given packet size.
    - We set a fixed packet size of 60 bytes = 480 bits here, but you can
      change it if you like.
    """

    PACKET_SIZE_BITS = 60 * 8  # 60 bytes

    dist = {}
    prev = {}

    for vertex in graph.links.keys():
        dist[vertex] = math.inf

    dist[start] = 0.0

    pq = []
    count = 0 
    heapq.heappush(pq, (0.0, count, start))

    visited = set()

    while pq:
        current_cost, _, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        if u == end:
            break

        for (neighbor, link) in graph.links[u]:
            edge_time = link.calculate_delay(PACKET_SIZE_BITS)
            new_cost = current_cost + edge_time

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                prev[neighbor] = u
                count += 1
                heapq.heappush(pq, (new_cost, count, neighbor))

    if math.isinf(dist[end]):
        return []

    path_vertices = []
    cur = end
    while cur in prev:
        path_vertices.append(cur)
        cur = prev[cur]
    path_vertices.append(start)
    path_vertices.reverse()

    path_info = []
    accumulated = 0.0
    path_info.append((path_vertices[0].identifier, accumulated))

    for i in range(len(path_vertices) - 1):
        u = path_vertices[i]
        v = path_vertices[i + 1]
        link_uv = _find_link(graph, u, v)
        if not link_uv:
            return []
        delta = link_uv.calculate_delay(PACKET_SIZE_BITS)
        accumulated += delta
        path_info.append((v.identifier, accumulated))

    return path_info


def _find_link(graph, u, v):
    """
    Helper function that returns the Link object connecting u->v (if any).
    """
    for (adj_vertex, link) in graph.links[u]:
        if adj_vertex == v:
            return link
    return None