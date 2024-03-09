"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
#import matplotlib.pyplot as plt
from copy import deepcopy


#transforms a list into a tuple (a hashable object)
def list_to_tuple(liste):
    """
    Side function having nothing to do with grids. 
    Turns a list into a tuple.
    """
    tuple_result = []
    for inner_list in liste:
        tuple_result.append(tuple(inner_list))
    return tuple(tuple_result)


class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The initial state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state


    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output


    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"
    

    def random_grid(self):
        """
        Using the dimension of a grid, returns a random grid
        """
        m = self.m
        n = self.n
        initial_state = []
        # Create a list of all possible numbers between 1 and n*m
        all_numbers = list(range(1, m * n + 1))
        # shuffle randomly those numbers
        random.shuffle(all_numbers)
        initial_state = [all_numbers[i*n:(i+1)*n] for i in range(m)]
        random_grid = Grid(m, n, initial_state)          
        return random_grid


    def is_sorted(self):
        """
        Checks is the current state of the grid is sorted and returns the answer as a boolean.
        """
        nb_right_cells=0
        for i in range (0, self.m):
            for j in range (0, self.n):
                if self.state[i][j] == i*self.n + j + 1:
                    nb_right_cells = nb_right_cells+ 1
        if nb_right_cells == self.n*self.m:
            return True
        else :
            return False
        
                    
    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        error=1
        if cell1[0] < 0 or cell2[0] < 0 :
            raise Exception("One cell does not exist")
        if cell1[1] < 0 or cell2[1] < 0 :
            raise Exception("One cell does not exist")

        #first allowed swap : same line, adjacent columns
        if cell1[0] == cell2[0]:
            if cell1[1]==cell2[1]+1 or cell1[1]==cell2[1]-1:
                int_cell1 = self.state[cell1[0]][cell1[1]]
                self.state[cell1[0]][cell1[1]]=self.state[cell2[0]][cell2[1]]
                self.state[cell2[0]][cell2[1]] = int_cell1
                error=0
        #second allowed swap : adjacent lines, same column
        elif cell1[0]==cell2[0]+1 or cell1[0]==cell2[0]-1:
            if cell1[1]==cell2[1]:
                int_cell1 = self.state[cell1[0]][cell1[1]]
                self.state[cell1[0]][cell1[1]]=self.state[cell2[0]][cell2[1]]
                self.state[cell2[0]][cell2[1]] = int_cell1
                error=0
        #in case the swap is not allowed
        if error == 1: 
            raise Exception("Swap not allowed")


    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for element in cell_pair_list:
            cell1 = element[0] 
            cell2 = element[1]
            Grid.swap(self, cell1, cell2)


    def graphic_rep(self):
        """
        Creates a graphic representation of the grid using matplotlib
        """
        #defines the grid : number of columns, number of lines
        fig, ax = plt.subplots()
        ax.set_xticks(range(self.n+1))
        ax.set_yticks(range(self.m+1))
        ax.grid()

        #fills in the cells of the grid
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                ax.text(j-0.5, self.m-i+0.5, str(self.state[i-1][j-1]))

        #shows the grid
        ax.set_aspect('equal')
        plt.show()


    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


    def get_grid_swap_case(self, i, j):
        """
        Using a grid and a cell, returns all the possible grids with only one move of the cell.
        
        Parameters : 
        ------------
        grid : Grid
            The grid.
        i : int
            The line number of the cell. 
        j : int
            The column number of the cell. 
        """

        resultat_swap_case=[]
        try:
            self.swap((i,j),(i+1,j))
            new_grid = Grid(self.m, self.n, initial_state=deepcopy(self.state))
            resultat_swap_case.append(new_grid)
            self.swap((i,j),(i+1,j))
        except:
            pass

        try:
            self.swap((i,j),(i,j+1))
            new_grid = Grid(self.m, self.n, initial_state=deepcopy(self.state))
            resultat_swap_case.append(new_grid)
            self.swap((i,j),(i,j+1))
        except:
            pass

        try:
            self.swap((i,j),(i-1,j))
            new_grid = Grid(self.m, self.n, initial_state=deepcopy(self.state))
            resultat_swap_case.append(new_grid)
            self.swap((i,j),(i-1,j))
        except:
            pass


        try:
            self.swap((i,j),(i,j-1))
            new_grid = Grid(self.m, self.n, initial_state=deepcopy(self.state))
            resultat_swap_case.append(new_grid)
            self.swap((i,j),(i,j-1))
        except:
            pass

        return resultat_swap_case
    
    
    def get_grid_all_swaps(self):
        """
        Returns the set of neighbors (grids accessible after a single swap) of a grid
        """

        resultat_all_swaps=[]
        for i in range(self.m):
            for j in range(self.n):
                for elt in self.get_grid_swap_case(i,j):
                    resultat_all_swaps.append(elt)
        return(resultat_all_swaps)
    

    def dict(self):
        #NB : with a grid bigger than 2 x 2, takes too much time
        """
        Changes a grid into a tuple then creates a dictionary used by the naive BFS.
        
        Parameters :
        ------------
        self : Grid
            The grid. 

        Output : 
        -------
        dict_all : ditc(tuple : list[tuple])
            The keys are tuples representing the state of the grid. 
            The lists contain all the state of the grids which are neighbours of the key.
        """

        to_be_seen=[self]
        dict_all={}
        while to_be_seen != []:
            current = to_be_seen.pop(0)
            all_neighbours= Grid.get_grid_all_swaps(current)
            tuple_neighbours = []
            for element in all_neighbours:
                tuple_neighbours.append(list_to_tuple(element.state))
            dict_all[list_to_tuple(current.state)] = tuple_neighbours
            for elt in all_neighbours:
                if elt not in to_be_seen and list_to_tuple(elt.state) not in dict_all.keys():
                    to_be_seen.append(elt)
        return dict_all
    

    def distance_grid(self):
        """
        Returns the distance between a grid and the sorted grid. 
        Used by A* to determine the heuristic of the grid.
        """
        
        nb_movement=0
        distance=0
        for i in range(self.m):
            for j in range(self.n):
                if self.state[i][j]% self.n == 0:
                    true_place_i = self.state[i][j]//self.n - 1
                    true_place_j = self.n -1
                else:
                    true_place_i = self.state[i][j]// self.n
                    true_place_j = self.state[i][j]% self.n - 1
                if self.state[i][j] == i*self.m + j + 1:
                    nb_movement = 0
                else:
                    nb_movement= abs(i-true_place_i) + abs(j-true_place_j)
                distance = distance + nb_movement
        return distance
