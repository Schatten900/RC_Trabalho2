"""
This script sets up a simple interactive environment to simulate network commands
(`ping`, `traceroute`, `clear`) on a graph of vertices. Each vertex in the graph
represents a network host, and links represent paths between hosts.

Usage:
------
1. The script initializes a `Graph` and a `Terminal` object with an initial vertex ("H1").
2. It then enters an infinite loop, presenting a prompt like `root@H1:~$ `.
3. Possible commands:
   - `ping <destiny>`:
       Checks reachability to a destination host using the `terminal.ping()` method.
   - `traceroute <destiny>`:
       Simulate traceroute to the given destination host using the `terminal.traceroute()` method.
   - `clear`:
       Clears the terminal screen.
   - `change to <new_host>`:
       Navigates to a new host by updating `terminal.current_vertex`.

Details:
--------
- `construct_graph(adjacent_vertices)`: Builds a Graph object from an adjacency list 
  (`adjacent_vertices`).
- `vertex_map`: A dictionary mapping string identifiers (e.g., "H1", "CORE") to actual
  Vertex objects in the graph.
- `Terminal`:
    - `ping(destiny, graph)`: Simulates ping output.
    - `traceroute(destiny, graph)`: Simulates traceroute output.
    - `navigate_to(new_vertex)`: Changes the current vertex on the terminal.

Example Commands:
----------------
    ping H2
    traceroute H5
    clear
    change to H10

Authors
-----------------
    - José Neto Souza
    - Luca Merigion
    - Carlos Cauã
"""

from utils.settings.adjascentVertices import major_subnets, conections_in_same_router, host_subnets, routers_ips
from utils.functions.constructGraph import construct_graph
from utils.structures.terminal import Terminal
from time import sleep
import os

os.system('cls' if os.name == 'nt' else 'clear')
graph, vertex_map = construct_graph(major_subnets, conections_in_same_router, host_subnets, 'fiber')
graph.construct_routings_tables(vertex_map)
terminal = Terminal(initial_vertex='172.16.10.1')

while True:
    str_input = input(f"root@{terminal.current_vertex}:~$ ")
    str_input = str_input.split()

    # PING
    if str_input[0] == 'ping':
        if str_input[1] in vertex_map:
            terminal.ping(destiny=str_input[1], vertex_map=vertex_map, graph=graph)
        else:
            print("The provided destiny dont exists in the network.\n")

    # CLEAR
    elif str_input[0] == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')

    # TRACEROUTE
    elif str_input[0] == 'traceroute':
        if str_input[1] in vertex_map:
            if str_input[1] not in routers_ips:
                terminal.traceroute(destiny=str_input[1], graph=graph, vertex_map=vertex_map)
            else:
                print("\nIt is not possible to trace the route to a router.\n")
        else:
            print("The provided destiny dont exists in the network.\n")

    # CHANGETO - Select a new host for the terminal
    elif str_input[0] == 'changeto':
        if str_input[1] in vertex_map:
            terminal.navigate_to(new_vertex=str_input[1])
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("The provided new host dont exists in the network.\n")

    # CHANGENETWORK - Select a new type of network
    elif str_input[0] == 'changenetwork':
        if (str_input[1] == 'fiber') or (str_input[1] == 'coaxial'):
            graph, vertex_map = construct_graph(major_subnets, conections_in_same_router, host_subnets, 'coaxial')
            graph.construct_routings_tables(vertex_map)

            os.system('cls' if os.name == 'nt' else 'clear')
            print('New type of network defined!')
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        else:
            print("The provided type of network is not available.\n")

    # Invalid command
    else:
        print("The provided comand is not recognized.")
        print('Try: "ping <destiny>", "traceroute <destiny>", "clear", "changenetwork <fiber or coaxial>" or "changeto <new host>"\n')