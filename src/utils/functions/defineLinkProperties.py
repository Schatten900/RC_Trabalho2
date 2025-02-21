from utils.structures.link import Link

def define_link_properties(type, SPEED) -> Link:
    """
    Assigns predefined link properties based on the type of network connection.

    This function returns a `Link` object with specific attributes such as 
    physical distance and transmission rate, which vary according to the 
    type of network connection. The link properties are categorized into 
    three types:

    - **Major Subnet**: Represents connections between core and aggregation 
      layers, typically long-distance high-speed links.
    - **Same Router**: Represents connections within the same router or 
      switch, with negligible distance and cost.
    - **Host Subnet**: Represents connections between switches and end hosts, 
      typically covering shorter distances with standard transmission rates.

    Parameters:
    -----------
    type (str): 
        The type of network connection. Accepted values are:
        - `"major subnet"`: Long-distance high-speed links.
        - `"same router"`: Internal router connections with minimal cost.
        - `"host subnet"`: Connections between edge switches and hosts.

    Returns:
    --------
    Link:
        An instance of the `Link` class containing:
        - `distance` (int): The physical distance of the link in meters.
        - `transmissionRate` (int): The transmission rate of the link in bits per second (bps).
    """
    
    if type == "major subnet":
        link = Link(
            distance = 700000,  # 700 KM
            transmissionRate = 1000000000,  # 1 GB/s
            SPEED = SPEED
        )
    elif type == "same router":
        link = Link(
            distance = 0,
            transmissionRate = 0,
            SPEED = SPEED
        )
    elif type == "host subnet":
        link = Link(
            distance = 10000,  # 10 KM
            transmissionRate = 500000000,  # 500 MB/s
            SPEED = SPEED
        )
    else:
        raise ValueError(f"Type of connection not recognized: {type}")

    return link