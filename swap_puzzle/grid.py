"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import matplotlib.pyplot as plt

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
            The intiail state of the grid. Default is empty (then the grid is created sorted).
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

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        for i in range (self.m):
            for j in range (self.n):
                if self.state[i][j] == i*self.n + j:
                    nb_de_cases_bonnes =+ 1
                    if nb_de_cases_bonnes == self.n*self.m:
                        return True
                    
    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        error=1
        #first allowed swap : same line, adjacent columns
        if cell1[0] == cell2[0]:
            if cell1[1]==cell2[2]+1 or cell1[1]==cell2[2]-1:
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
            Grid.swap(cell1, cell2)

    def graphic_rep(self):
        fig, ax = plt.subplots()
        ax.set_xticks(range(self.n+1))
        ax.set_yticks(range(self.m+1))
        ax.grid()

        for i in range(1, m+1):
            for j in range(1, n+1):
                ax.text(j-0.5, i-0.5, str((i-1)*n + j), ha='center', va='center')

        ax.set_xlim(0, self.n)
        ax.set_ylim(0, self.m)
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


