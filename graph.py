class Graph:
    def __init__(self):
        """
        Creates an empty graph
        """
        self.going_data = {}
        self.coming_data = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex into the graph
        """
        self.going_data[vertex] = set()
        self.coming_data[vertex] = set()

    def add_edge(self, start, end):
        """
        Adds an edge between two vertices that are connected
        """
        self.going_data[start].add(end)
        self.going_data[end].add(start)
        self.coming_data[end].add(start)
        self.coming_data[start].add(end)

    def degree(self, vertex):
        """
        Returns the degree given a vertex
        """
        return len(self.coming_data[vertex])
    
    def incident_vertices(self, vertex):
        """
        Returns a list of the vertices that a given vertex is pointing to
        """
        return self.going_data[vertex]

    def remove_vertex(self, vertex):
        """
        Removes a vertex from the graph
        """
        
    def edges(self):
        
        return_list = []
        for k, v in self.going_data.items():
            for v_ in v:
                return_list.append((k, v_))

        return return_list


    