"""
This is the graph module. It contains a minimalistic Graph class.
"""

from grid import Grid
import heapq as hpq

def list_to_tuple(liste):
    tuple_result = []
    for inner_list in liste:
        tuple_result.append(tuple(inner_list))
    return tuple(tuple_result)

class Graph:
    """
    A class representing undirected graphs as adjacency lists. 

    Attributes: 
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...
    """

    def __init__(self, dict):

        self.graph = dict


    def bfs(self, state_src_grid, state_dst_grid): 
        """
        Answer to question 5 : naive BFS. Uses a dictionnary representing the whole graph.
        """
        src = list_to_tuple(state_src_grid.state)
        dst = list_to_tuple(state_dst_grid.state)
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
                    if inverse_path != []:
                        return(inverse_path[::-1])
            marked.append(current)
        return None
        

    def A_star(self, src):
        """uses the heapq module to find the path faster than efficient_bfs, 
        
        file est un heap où chaque item est un 2-uplet : (priorité, grille) 
        à vérifier car on peut vouloir implémenter l'odre d'apparition dans la grille afin de résoudre les égalités.
        mark sera une liste des 2uplets[1], soit des grilles. path est une liste qui double
        file, elle est impliquée seulement pour filtrer les éléments déjà en vue et ne pas recalculer la distance 
        de tous les nouveaux éléments créés """
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
                    if inverse_path != []:
                        return inverse_path[::-1]
            marked.append(current[3].state)
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


