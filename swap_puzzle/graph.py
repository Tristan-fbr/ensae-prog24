"""
This is the graph module. It contains a minimalistic Graph class.
"""
from grid import Grid

def list_to_tuple(liste):
    tuple_result = []
    for inner_list in liste:
        tuple_result.append(tuple(inner_list))
    return tuple(tuple_result)

class Graph:
    """
    A class representing undirected graphs as adjacency lists. 

    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...]
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    edges: list[tuple[NodeType, NodeType]]
        The list of all edges
    """

    def __init__(self, dict):
        """
        Initializes the graph with a set of nodes, and no edges. 

        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """

        self.graph = dict

        
    def __str__(self):
        """
        Prints the graph as a list of neighbors for each node (one per line)
        """
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the graph with number of nodes and edges.
        """
        return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"


    def bfs(self, state_src_grid, state_dst_grid): 
        """Answer to question 5 : naive bfs. Uses a dictionnary representing the whole graph.
        """
        src = list_to_tuple(state_src_grid)
        dst = list_to_tuple(state_dst_grid)
        path = []
        file = [src]
        marked = []
        parents = {src : -1}

        while file != []:
            current = file[0]
            all_neighbors = self.graph[current]
            for element in all_neighbors:
                if element not in file :
                    if element not in marked : 
                        file.append(element)
                        parents[element] = current
                if element == dst : 
                    inverse_path = Graph.get_back_path(self, element, src, parents)
                    path = inverse_path[::-1]
                    return path
            marked.append(current)
            file.pop(0)
        return None
    
        
    def get_back_path(self, dst, src, dict):
        """Concludes the bfs : using the dictionnary of parents, get back from the destination
        to the source and return the path betwenn both"""
        print(dict)
        print(src)
        print(dst)
        active = dst
        inverse_path = []
        while active != src : 
            print(active)
            inverse_path.append((dict[active], active))
            active = dict[active]
        return inverse_path
    

    

        

    def A(self, src):
        path = []
        file = [src] 
        marked = [] 
        parents = {list_to_tuple(src.state): -1}
        m = src.m
        n = src.n
        dst = list_to_tuple([list(range(i*n+1, (i+1)*n+1)) for i in range(m)])

        while file != []:
            # Sort the file based on distance to destination
            file.sort(key=lambda state: state.distance_grid())

            current = file[0]
            grid_neighbors = Grid.get_grid_all_swaps(current)
            
            for element in grid_neighbors:
                if element not in marked:
                    if element not in file:
                        # Add the neighbor to the file
                        file.append(element)
                        parents[list_to_tuple(element.state)] = list_to_tuple(current.state)
                    elif element.distance_grid < current.distance_grid():
                        # Update parent if the neighbor has a smaller distance
                        parents[list_to_tuple(element.state)] = list_to_tuple(current.state)
                        
                    if list_to_tuple(element.state) == dst:
                        inverse_path = Graph.get_back_path(self, list_to_tuple(element.state), list_to_tuple(src.state), parents)
                        if inverse_path != []:
                            path = inverse_path[::-1]
                            return path

            marked.append(current)
            file.pop(0)
        return None



    @classmethod
    def graph_from_file(cls, file_name):
        """
        Reads a text file and returns the graph as an object of the Graph class.

        The file should have the following format: 
            The first line of the file is 'n m'
            The next m lines have 'node1 node2'
        The nodes (node1, node2) should be named 1..n

        Parameters: 
        -----------
        file_name: str
            The name of the file

        Outputs: 
        -----------
        graph: Graph
            An object of the class Graph with the graph from file_name.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2) # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph



new_grid = Grid(3,3)
print(new_grid)
new_grid.swap((1,1),(1,2))
new_grid.swap((1,2),(2,2))
new_grid.swap((0,1),(0,0))
new_grid.swap((1,0),(1,1))
new_grid.swap((2,2),(1,2))
new_grid.swap((1,1),(2,1))
new_grid.swap((1,1),(0,1))
new_grid.swap((2,0),(2,1))
new_grid.swap((2,2),(2,1))
print(new_grid)
print(new_grid.distance_grid())



import matplotlib.pyplot as plt

def create_table(data, title=None):
    plt.figure(figsize=(8, 6))
    plt.axis('off')
    if title:
        plt.title(title)
    table = plt.table(cellText=data, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.5, 1.5)
    plt.show()


create_table(data, title='Grid')