class Travel:
    """
    The objective is to travel around a sudoku and create all the posibilities. For examenple, given the next options:

    1.- A value is [1]
    2.- Another one is [2, 3, 4]
    3.- Last one is [1, 4, 5]

    And the constraints are that 1 is not compatible with 3 and 2 with 3.
    """
    def __init__(self):
        """
        Creates the travel object
        """
        self.values = {
            "A2": {
                "uncompatible_with": "A3",
                "values": [2, 3, 4],
                "len": 3
            },
            "A1": {
                "uncompatible_with": "A3",
                "values": [1],
                "len": 1
            },
            
            "A3": {
                "uncompatible_with": "A1",
                "values": [1, 4, 5],
                "len": 3
            }
        }
        print(self.values)
        sorted_values = self._sort_by_len_values()
        print(sorted_values)
    
    def _sort_by_len_values(self):
        """
        Returns the sorted dictionary by the len of the values
        """
        return dict(sorted(self.values.items(), key = lambda x: x[1]["len"]))


class Tree:
    """
    Simple tree implementation
    """
    class Node:
        def __init__(self):
            self.children = dict()
        
        def add_children(self, parent, children):
            if parent in self.children.keys():
                self.children[parent].append(children)
            else:
                self.children[parent] = [children]
    def __init__(self):
        """
        Creates an empty tree
        """
        self.data = []



if __name__ == "__main__":
    t = Travel()