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

    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        When adding an edge between two nodes, if one of the ones does not exist it is added to the list of nodes.

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.nb_edges += 1
        self.edges.append((node1, node2))

    def bfs(self, a, b): 
        """
        Finds a shortest path from src to dst by BFS.  

        Parameters: 
        -----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 
        src = list_to_tuple(a)
        dst = list_to_tuple(b)
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
            marked.append(current)
            file.pop(0)
            
        if inverse_path != []:
            path = inverse_path[::-1]
            return path
        else : 
            return None
        
    
    def get_back_path(self, dst, src, dict):
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

    def efficient_bfs(self, src):  
        path = []
        file = [src] #list of grids
        marked = [] #list of grids
        parents = {list_to_tuple(src.state) : -1} #dict of tuples
        m = src.m
        n = src.n
        dst = list_to_tuple([list(range(i*n+1, (i+1)*n+1)) for i in range(m)])

        while file != []:
            current = file[0]
            grid_neighbors = Grid.get_grid_all_swaps(current)
            for element in grid_neighbors:
                if element not in file :
                    if element not in marked : 
                        file.append(element)
                        parents[list_to_tuple(element.state)] = list_to_tuple(current.state)
                if list_to_tuple(element.state) == dst : 
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

