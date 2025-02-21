from utils.functions.adaptedDijkstra import dijkstra
from time import sleep
import random

class Terminal():
    """
    Represents a terminal that can perform network operations such as ping and traceroute.

    Attributes:
    -----------
        current_vertex (Vertex):
            The current vertex (or host) from which network operations will be performed.
    """

    def __init__(self, initial_vertex=None):
        """
        Initializes the Terminal with a given starting vertex.

        Parameters:
        -----------
            initial_vertex (Vertex):
                The vertex from which network operations (ping, traceroute) will originate.
        """

        if (initial_vertex == None):
            raise ValueError("Initial vertex or vertex map not provided")
        
        self.current_vertex = initial_vertex

    def navigate_to(self, new_vertex=None):
        """
        Changes the current vertex (or host) to a new one, simulating movement or repositioning
        in the graph.

        Parameters:
        -----------
            new_vertex (Vertex):
                The new vertex to become the current vertex.
        """

        if new_vertex == None:
            raise ValueError("New origin vertex is not provided")
        
        self.current_vertex = new_vertex

    def ping(self, destiny=None, graph=None, vertex_map=None) -> list:
        """
        Simulates the 'ping' command from the current_vertex to a destination vertex.
        This method calculates the total travel time (using Dijkstra), adds small random
        variations, and prints a simplified output similar to the 'ping' command.

        Parameters:
        -----------
            destiny (Vertex):
                The destination vertex to be pinged.
            graph (Graph):
                The graph object that contains vertices and links.
            vertex_map (list):
                The list of vertices and their memory adress.
        """

        if (self.current_vertex is None) or (destiny is None) or (graph is None) or (vertex_map is None):
            raise ValueError("New host, graph, destiny and vertex map need to be provided")
        
        times = []
        for i in range(4):
            trace_time = 0

            # Going
            pointer = vertex_map[self.current_vertex]
            while pointer.identifier != destiny:
                trace_time += pointer.routing_table[destiny][1][1]
                pointer = vertex_map[pointer.next_hop(destiny)]

            # Coming back
            pointer = vertex_map[destiny]
            while pointer.identifier != self.current_vertex:
                trace_time += pointer.routing_table[self.current_vertex][1][1]
                pointer = vertex_map[pointer.next_hop(self.current_vertex)]

            times.append(float((trace_time * 1000) + random.uniform(0.1, 0.4)))

        variance = sum((t - sum(times) / len(times))**2 for t in times) / len(times)
        minimal = round(min(times), 2)
        avarage = round((sum(times)/len(times)), 2)
        maximal = round((max(times)), 2)
        mdev = round((variance ** 0.5), 2)

        print(f'\nPING {destiny} 60 data bytes\n')

        output = [f'60 bytes from {destiny}: icmp_seq=1 ttl=64 time={times[0]:.2f} ms',
            f'60 bytes from {destiny}: icmp_seq=2 ttl=64 time={times[1]:.2f} ms',
            f'60 bytes from {destiny}: icmp_seq=3 ttl=64 time={times[2]:.2f} ms',
            f'60 bytes from {destiny}: icmp_seq=4 ttl=64 time={times[3]:.2f} ms\n',
            ]   
        
        for i in range(len(output)):
            sleep(times[i] / 10)
            print(output[i])

        print(f'4 packets transmitted, 4 received, 0% packet loss, time {sum(times):.2f}ms')
        print(f'rtt min/avg/max/mdev = {minimal}/{avarage}/{maximal}/{mdev} ms\n')

    def traceroute(self, destiny=None, graph=None, vertex_map=None):
        """
        Simulates a 'traceroute' from the current_vertex to the destiny vertex, 
        showing each hop along the path.

        Parameters:
        -----------
            destiny (Vertex):
                The destination vertex to trace the route to.
            graph (Graph):
                The graph object that contains vertices and links.
            vertex_map (list):
                The list of vertices and their memory adress.
        """

        if (destiny is None) or (graph is None) or (vertex_map is None):
            raise ValueError("Need a destiny, graph and vertex map to run traceroute")
        
        print(f"\nTracing route to {destiny} over a maximum of 30 hops:\n")

        hop_count = 1
        hop_time_package = 0
        pointer = vertex_map[self.current_vertex]
        while pointer.identifier != destiny and hop_count <= 30:
            
            actual_hope_time_going = pointer.routing_table[destiny][1][1] * 1000
            hop_time_package += actual_hope_time_going

            actual_hope_time_comeback = vertex_map[pointer.next_hop(destiny)].routing_table[pointer.identifier][1][1] * 1000
            hop_time_package += actual_hope_time_comeback

            sleep(hop_time_package / 10)
            
            print((f'{hop_count}     {round(hop_time_package + random.uniform(0.1, 0.4), 2)} ms     {round(hop_time_package + random.uniform(0.1, 0.4), 2)} ms    {round(hop_time_package + random.uniform(0.1, 0.4), 2)} ms    {pointer.routing_table[destiny][1][0]}'))

            pointer = vertex_map[pointer.next_hop(destiny)]
            hop_count += 1

            if hop_count > 30:
                print('\nMax hops reached')

        print('\nTrace complete.\n')