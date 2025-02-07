class Link():
    """
    Represents a link in a graph, containing information about the distance 
    to another point and the transmission rate of the associated link.

    Attributes:
    -----------
        distance (float): The length of the link (e.g., in kilometers or meters).
        transmissionRate (float): The transmission rate of the associated link (e.g., in Mbps).

    Methods:
    --------
        1 - __init__(distance: float, transmissionRate: float): 
                Initializes a link object with the given distance and transmission rate values.
        2 - calculate_transmission_delay(packet_size: float) -> float:
                Computes the transmission delay based on the given packet size.
        3 - calculate_propagation_delay() -> float:
                Computes the propagation delay based on the distance in fiber optics.
        4 - calculate_delay(packet_size: float) -> float:
                Computes the total delay (transmission + propagation).
    """

    SPEED_OF_LIGHT_FIBER = 2e8  #(200,000,000 m/s)

    def __init__(self, distance=None, transmissionRate=None):
        """
        Initializes a link with a given distance and transmission rate.

        Parameters:
        -----------
            distance (float): 
                The lenght of the link in meters.
            transmissionRate (float): 
                The transmission rate of the associated link in bits per second.
        """

        if (distance == None) or (transmissionRate == None):
            raise ValueError("Both distance and transmissionRate must be provided")
        
        self.distance = distance
        self.transmissionRate = transmissionRate
    
    def calculate_transmission_delay(self, packet_size: float) -> float:
        """
        Calculates the transmission delay, which is the time required to transmit 
        all bits of a packet over the given transmission rate.

        Parameters:
        -----------
            packet_size (float): 
                The size of the packet in bits.

        Returns:
        --------
            float: The transmission delay in seconds.
        """
        
        return packet_size / self.transmissionRate

    def calculate_propagation_delay(self) -> float:
        """
        Calculates the propagation delay, which is the time it takes for the signal to travel 
        through the fiber optic cable.

        Returns:
        --------
            float: The propagation delay in seconds.
        """

        return self.distance / self.SPEED_OF_LIGHT_FIBER

    def calculate_delay(self, packet_size: float) -> float:
        """
        Calculates the total delay, which is the sum of transmission and propagation delays.

        Parameters:
        -----------
            packet_size (float): 
                The size of the packet in bits.

        Returns:
        --------
            float: The total delay in seconds.
        """
        
        return self.calculate_transmission_delay(packet_size) + self.calculate_propagation_delay()