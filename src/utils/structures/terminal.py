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

        if initial_vertex == None:
            raise ValueError("Initial vertex is not provided")
        
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

    def ping(self, destiny=None, graph=None) -> list:
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
        """

        if (self.current_vertex is None) or (destiny is None) or (graph is None):
            raise ValueError("New host, graph and destiny need to be provided")
        
        base_time_sec_go = dijkstra(graph=graph, start=self.current_vertex, end=destiny)[-1][1]
        base_time_ms_go = base_time_sec_go * 1000

        base_time_sec_back = dijkstra(graph=graph, start=destiny, end=self.current_vertex)[-1][1]
        base_time_ms_back = base_time_sec_back * 1000

        times = []
        for i in range(4):
            times.append((base_time_ms_go + base_time_ms_back) + random.uniform(0.02, 0.01))

        variance = sum((t - sum(times) / len(times))**2 for t in times) / len(times)
        mdev = variance ** 0.5

        output = [
            f'PING {destiny.identifier} 60 data bytes',
            f'60 bytes from {destiny.identifier}: icmp_seq=1 ttl=64 time={times[0]:.2f} ms',
            f'60 bytes from {destiny.identifier}: icmp_seq=2 ttl=64 time={times[1]:.2f} ms',
            f'60 bytes from {destiny.identifier}: icmp_seq=3 ttl=64 time={times[2]:.2f} ms',
            f'60 bytes from {destiny.identifier}: icmp_seq=4 ttl=64 time={times[3]:.2f} ms',
            '',
            f'--- {destiny.identifier} ping statistics ---',
            f'4 packets transmitted, 4 received, 0% packet loss, time {sum(times):.2f}ms',
            f'rtt min/avg/max/mdev = {min(times):.2f}/{sum(times) / len(times):.2f}/{max(times):.2f}/{mdev:.2f} ms',
            ''
        ]

        for i in range(len(output)):
            if (i <= 4) and (i > 0):
                sleep(times[i - 1] / 1000)

            print(output[i])

    def traceroute(self, destiny=None, graph=None):
        """
        Simulates a 'traceroute' from the current_vertex to the destiny vertex, 
        showing each hop along the path.

        Parameters:
        -----------
            destiny (Vertex):
                The destination vertex to trace the route to.
            graph (Graph):
                The graph object that contains vertices and links.
        """

        if (destiny is None) or (graph is None):
            raise ValueError("Need a destiny and graph to run traceroute")

        path_info = dijkstra(graph=graph, start=self.current_vertex, end=destiny)
        path_info.pop(0)
        
        output = []
        for index, path in enumerate(path_info):
            string = f"{index+1}    {(path[1] * 1000) + random.uniform(0.02, 0.01):.2f}ms    {(path[1] * 1000) + random.uniform(0.1, 0.2):.2f}ms    {(path[1] * 1000) + random.uniform(0.1, 0.2):.2f}ms    {path[0]}"
            output.append(string)

        print(f"Tracing route to {destiny.identifier} over a maximum of 30 hops:\n")

        i = 1
        for i in range(len(output)):
            sleep(path_info[i][1])
            print(output[i])

            if i > 30:
                print("Maximum hops reached")
                break

        print('\nTrace complete.\n')