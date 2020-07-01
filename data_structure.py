#   ***     IMPORTATIONS    ***
import numpy as np
import time

class sudoku:
    """
    Own sudoku structure created by @Diego Valcarce to be able to analyze properly the values and get the solution. Once it's created
    the sudoku object, will be created automatically 3 objects:

    + numpy array: will store the indexes of the sudoku (A1, A2 ..., B1, B2... like), this will be used to access easily (and qucikly)
        to all the indexes of the sudoku.
    + hash table (dict like): will store the real values of the sudoku, easy to access from the numpy array
    + graph: a non-directed simple implemented graph, used to travel around the posible solutions and implementate a backtracking algorithm
        to solve it
    """
    
    # ***       NON-DIRECTED GRAPH      ***
    class Graph:
        """
        Non directed graph implementation
        """
        def __init__(self):
            """
            Creates an empty graph. Data will be store as a 'JSON' (will be a dict of dicts):
            data = {
                "vertex": {
                    POS_VALUES = set(),         # Can't be modified, up until be sure a value can be dropped
                    degree = int,
                    try: int                    # The version of the data we are trying to check as a posible solution
                }
                ...
            }
            """
            self._data = dict()
        
        def add_vertex(self, vertex, POS_VALUES = set(range(1, 10))):
            """
            Adds a vertex
            """
            self._data[vertex] = {
                "POS_VALUES" : POS_VALUES,         # By default can have this 9 values
                "degree" : 0,
                "try" : None,
                "point_to": set()
            }

        def add_edge(self, vertex_from, vertex_end):
            """
            Adds an edge between 2 existing vertices
            """
            # When creating an edge we might:
            #   1.- Adding the edge
            #   2.- Increasing the degree
            self._data[vertex_from]["point_to"].add(vertex_end)
            self._data[vertex_from]["degree"] += 1

            self._data[vertex_end]["point_to"].add(vertex_from)
            self._data[vertex_end]["degree"] += 1
        
        def degree(self, vertex):
            """
            Returns the degree of a given vertex
            """
            return self._data[vertex]["degree"]

        def remove_non_accepted_values(self):
            """
            Removes from the graph the values that can not be taken.
            """
            added_numbers = 0
            def _remove_():
                added_numbers = 0
                for vertex in self._data.keys():
                    val = self._data[vertex]["POS_VALUES"]
                    if len(val) == 1:
                        # In case we now a number can not be in all the other positions, we remove it
                        for vertex_pointed in self._data[vertex]["point_to"]:
                            difference = self._data[vertex_pointed]["POS_VALUES"] 
                            self._data[vertex_pointed]["POS_VALUES"] = difference.difference(val)
                            added_numbers += len(difference) - len(self._data[vertex_pointed]["POS_VALUES"])
                return added_numbers
            
            while (added_numbers + _remove_()) > added_numbers:
                added_numbers = _remove_()


            

        def travel_graph(self):
            """
            
            """

        def _list_of_pos_(self):
            """
            Returns the list of the posible values calculated
            """
            # for v in self._data.keys():


        def __str__(self):
            """
            Prints the edges of the graph
            """
            string = ""
            for vertex in self._data.keys():
                pointing = self._data[vertex]["point_to"]
                values = self._data[vertex]["POS_VALUES"]
                string += f"{vertex} points to {pointing} and can have the {values} as values \n"
            return string



    def __init__(self, sudoku, unknown = 0):
        """
        + sudoku: a sudoku like; must be an array of the values that has the own sudoku. Ordered by row/col
        + unknown: the parameter inclyed in the sudoku that has the meaning of unknown.
        """
        start_time_graph = time.time()
        self._unknown_parameter = unknown
        # Create the table wi will play with:
        self._sudoku_table = np.array([[chr(letter) + str(number) for number in range(1, 10)] for letter in range(65, 74)])
        # Create the dictionary that will store the rial data:
        self._sudoku_values = dict(zip([chr(letter) + str(number) for letter in range(65, 74) for number in range(1, 10)], sudoku))

        # Now create the graph:
        self.graph = self.Graph()
        
        # Create the vertices:
        self.vertices = [chr(letter) + str(number) for letter in range(65, 74) for number in range(1, 10)]
        # And add them
        for vertex in self.vertices:
            if self._sudoku_values[vertex] != unknown:
                self.graph.add_vertex(vertex, {self._sudoku_values[vertex]})
            else:
                self.graph.add_vertex(vertex)

        #       ***     CREATING EDGES      ***
        table = self._sudoku_table
        # In the first step we add cols and rows
        for index in range(9):
            row = table[index]
            col = table[:, index]
            combinations_row = [(a, b) for a in row for b in row if a != b and b != a]
            combinations_col = [(a, b) for a in col for b in col if a != b and b != a]
            # And create the combinations as edges on the graph
            for edge_index in range(len(combinations_row)):
                self.graph.add_edge(*combinations_row[edge_index])
                self.graph.add_edge(*combinations_col[edge_index])
        # Finally the blocks
        block = self.get_block_combinations()
        for block_values in block:
            combinations = [(a, b) for a in block_values for b in block_values if a != b and b != a]
            for edge in combinations:
                self.graph.add_edge(*edge)
        #       ********************************
        end_time_graph = time.time()
        print("Data structure for organazing the sudoku created in {} seconds".format(end_time_graph - start_time_graph))

        # Once it has been created the vertices and the edges, it's time to remove the values that can not take place
        start_time_removing_non_valid = time.time()
        self.graph.remove_non_accepted_values()
        end_time_removing_non_valid = time.time()
        print("Remove all the invalid values toke {} seconds".format(end_time_removing_non_valid - start_time_removing_non_valid))
        print(self.check_win())
        # print(self.graph)
        

    def get_block_combinations(self):
        """
        Returns a list of combinations of the letters (A1, A2...) for each block
        """
        return_list = []
        for block in range(9):
            up = (block) // 3 * 3
            left = (block) % 3 * 3
            aux = []
            for row in self._sudoku_table[up : up + 3, left : left + 3]:
                
                for index in row:
                    aux.append(index)
                if aux not in return_list:
                    return_list.append(aux)

        return return_list

    def check_win(self):
        """
        Checks if win
        """
        check_graph = [self.graph._data[v]["POS_VALUES"] for v in self.graph._data.keys()]
        result = True
        for i in check_graph:
            result = result and (len(i) == 1)
        return result

    def __str__(self):
        return self.graph.__str__()
        
        



if __name__ == "__main__":
    s = sudoku(
        [5, 3, 0, 0, 7, 0, 0, 0, 0,
        6, 0, 0, 1, 9, 5, 0, 0, 0,
        0, 9, 8, 0, 0, 0, 0, 6, 0,
        8, 0, 0, 0, 6, 0, 0, 0, 3,
        4, 0, 0, 8, 0, 3, 0, 0, 1,
        7, 0, 0, 0, 2, 0, 0, 0, 6,
        0, 6, 0, 0, 0, 0, 2, 8, 0,
        0, 0, 0, 4, 1, 9, 0, 0, 5,
        0, 0, 0, 0, 8, 0, 0, 7, 9]
    )

    sudo = sudoku(
        [
            0, 0, 1, 3, 7, 8, 0, 0, 9,
            3, 2, 0, 9, 0, 0, 0, 5, 0,
            9, 7, 4, 1, 0, 2, 6, 3, 0,
            0, 1, 6, 0, 8, 0, 0, 0, 0,
            7, 9, 0, 0, 0, 0, 0, 8, 5,
            0, 0, 0, 0, 3, 0, 1, 9, 0,
            0, 6, 9, 4, 0, 3, 8, 7, 2,
            8, 4, 0, 0, 0, 7, 5, 1, 3,
            1, 0, 0, 8, 2, 5, 9, 0, 0
        ]
    )
    print(sudo)
