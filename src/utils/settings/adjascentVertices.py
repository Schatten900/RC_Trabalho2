"""
This dictionary adjacent_vertices represents a graph where each key is a vertex, 
and the corresponding value is a tuple containing its adjacent (connected) vertices.

Structure:
-----------
- The keys represent main vertices (such as "CORE", "A1", "A2", "E1", etc.).
- The values are tuples containing the adjacent vertices connected to the key.

Graph Description:
-------------------
- "CORE" is connected to "A1" and "A2".
- "A1" is connected to "E1" and "E2".
- "A2" is connected to "E3" and "E4".
- "E1" to "E4" are connected to multiple "H" vertices, representing different hosts.
"""

adjacent_vertices = {
    "CORE" : (
        "A1", "A2"
        ),
    "A1" : (
        "E1", "E2"
        ),
    "A2" : (
        "E3", "E4"
        ),
    "E1" : (
        "H55", "H56", "H57", "H58", "H59", "H60", "H69", "H70",
        "H61", "H62", "H63", "H64", "H65", "H66", "H67", "H68",
        "H71", "H72", "H73", "H74", "H75", "H76", "H77", "H78"
        ),
    "E2" : (
        "H31", "H32", "H33", "H34", "H35", "H36", "H37", "H38", 
        "H39", "H40", "H41", "H42", "H43", "H44", "H45", "H46", 
        "H47", "H48", "H49", "H50", "H51", "H52", "H53", "H54"
        ),
    "E3" : (
        "H1",  "H2",  "H3",  "H4",  "H5",
        "H6",  "H7",  "H8",  "H9",  "H10",  
        "H11", "H12", "H13", "H14", "H15"
        ),
    "E4" : (
        "H16", "H17", "H18", "H19", "H20",
        "H21", "H22", "H23", "H24", "H25", 
        "H26", "H27", "H28", "H29", "H30"
        )
    }