"""
This is the graph module. It contains a minimalistic Graph class.
"""

from grid import Grid
import heapq as hpq
import time


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

    def __init__(self, dictio, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 

        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes 
        if dict == {}:
            self.graph = dict([(n, []) for n in nodes])
        else : 
            self.graph = dictio
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []
        print('nodes', type(self.nodes))
        print('graph', self.graph)

        
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


    def bfs(self, src, dst): 
        """
        Answer to question 5 : naive BFS. Uses a dictionnary representing the whole graph.

        """
        beginning = time.time()
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
                    end = time.time()
                    print(end - beginning)
                    return path
            marked.append(current)
            file.pop(0)
        end = time.time()
        print(end - beginning)
        return None
    

    def get_back_path(self, dst, src, dict):
        """Is used at the end of the BFS : using the dictionnary of parents, get back from the destination
        to the source and return the path betwenn both"""
        active = dst
        inverse_path = []
        while active != src : 
            inverse_path.append((dict[active], active))
            active = dict[active]
        return inverse_path
    
    
    def efficient_bfs(self, src):  
        """
        Answer to question 8 : creates the adjacent nodes of the current one, preventing from creating the whole
        graph, and thus saving memory and time"""
        beginning = time.time()
        file = [src] 
        marked = [] 
        parents = {list_to_tuple(src.state) : -1}
        m = src.m
        n = src.n
        dst = list_to_tuple([list(range(i*n+1, (i+1)*n+1)) for i in range(m)])


        while file != []:
            current = file.pop(0)
            grid_neighbors = Grid.get_grid_all_swaps(current)
            for element in grid_neighbors:
                #check if not in file nor marked
                check = 0
                for elt in file :
                    if element.state == elt.state :
                        check += 1
                for elt in marked : 
                    if element.state == elt.state : 
                        check += 1
                if check == 0 : 
                    file.append(element)
                    parents[list_to_tuple(element.state)] = list_to_tuple(current.state)
                if list_to_tuple(element.state) == dst : 
                    inverse_path = Graph.get_back_path(self, list_to_tuple(element.state), list_to_tuple(src.state), parents)
                    end = time.time()
                    print(end - beginning)
                    return(inverse_path[::-1])
            marked.append(current)
        end = time.time()
        print(end - beginning)
        return None
        

    def A_star(self, src):
        """uses the heapq module to find the path faster than efficient_bfs, 
        
        file est un heap où chaque item est un 2-uplet : (priorité, grille) 
        à vérifier car on peut vouloir implémenter l'odre d'apparition dans la grille afin de résoudre les égalités.
        mark sera une liste des 2uplets[1], soit des grilles. path est une liste qui double
        file, elle est impliquée seulement pour filtrer les éléments déjà en vue et ne pas recalculer la distance 
        de tous les nouveaux éléments créés """
        beginning = time.time()
        file = [] 
        marked = [] 
        parents = {list_to_tuple(src.state): -1}
        #determines the destination
        m = src.m
        n = src.n
        dst = list_to_tuple([list(range(i*n+1, (i+1)*n+1)) for i in range(m)])
        order_of_apparition = 0
        hpq.heappush(file, (0, order_of_apparition, 0, src))

        while file != []:
            current = (hpq.heappop(file))
            grid_neighbors = Grid.get_grid_all_swaps(current[3])
            for element in grid_neighbors:
                #check if not in file nor marked
                check = 0
                for elt in file :
                    if element.state == elt[3].state :
                        check += 1
                for elt in marked : 
                    if element.state == elt : 
                        check += 1
                if check == 0 :
                    # Add the neighbor to the file
                    order_of_apparition += 1
                    dist = Grid.distance_grid(element)
                    hpq.heappush(file,(dist + current[2] + 1, order_of_apparition ,current[2]+1, element))
                    parents[list_to_tuple(element.state)] = list_to_tuple(current[3].state)
                    """elif element.distance_grid < current.distance_grid():
                        # Update parent if the neighbor has a smaller distance
                        parents[list_to_tuple(element.state)] = list_to_tuple(current.state)"""
                        
                if list_to_tuple(element.state) == dst:
                    inverse_path = Graph.get_back_path(self, list_to_tuple(element.state), list_to_tuple(src.state), parents)
                    end = time.time()
                    print(end - beginning)
                    return inverse_path[::-1]
            marked.append(current[3].state)
        end = time.time()
        print(end - beginning)
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
            nodes = []
            for i in range(1, n+1):
                nodes.append(i)
            graph = Graph({}, nodes)
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2) # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph

