from grid import Grid
import time

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def __init__(self, list):
        m = 0
        n = 0
        for line in list :
            m +=1
        for column in list[0]:
            n +=1
        self.n = n
        self.m = m
        self.state= list
        
    
    def get_solution(self):
        """
        Finds a naive solution to the swap puzzle.

        Output : 
        -------
        swaps_solution : list
            A list of swaps which, if used by the swap_seq function, will returns an ordered grid. 
        """
        beginning = time.time()
        swaps_solution = []
        i, j = 0, 0 #i and j the coordinates of the targeted cell
        
        
        for j in range (0, self.n):
            for i in range(0, self.m):
                #Searching for the coordinates of the right cell
                k = i*self.n + j + 1
                for a in range (0,self.m) :
                    for b in range (0, self.n):
                        if self.state[a][b] == k:
                            ik = a
                            jk = b
                #adjusting lines
                while ik < i :
                    swaps_solution.append(((ik, jk), (ik + 1, jk)))
                    Solver.swap(self, (ik, jk), (ik + 1, jk))
                    ik = ik +1 
                while ik > i : 
                    swaps_solution.append(((ik, jk), (ik - 1, jk)))
                    Solver.swap(self, (ik, jk), (ik - 1, jk))
                    ik = ik - 1
                #moving left
                while jk > j :
                    swaps_solution.append(((ik, jk), (ik , jk - 1)))
                    Solver.swap(self,(ik, jk), (ik , jk - 1))
                    jk = jk - 1
        end = time.time()
        print(beginning - end)
        return(swaps_solution)
            
    
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

