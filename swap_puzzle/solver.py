from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def __init__(self, n, m, state):
        self.n = n
        self.m = m
        self.state = state
        
    
    def get_solution(self):
        """We proceed step by step, i.e. cell by cell beginning at the top left and continuing by column. 
        For each step we define the targeted cell (the place where the number should be) and the right cell (the place where the number is)"""
        swaps_solution = []
        i = 0 #i and j the coordinates of the targeted cell
        j = 0
        
        for step in (0, self.n*self.m - 1):
            #Search for the right cell
            k = i*self.n + j + 1
            for a in (0,self.m) :
                for b in (0,self.n):
                    if self.state[a][b] == k:
                        ik = a
                        jk = b
            #adjusting lines
            while ik < i :
                ik = ik +1 
                swaps_solution.append(((ik, jk), (ik + 1, jk)))
            while ik > i : 
                ik = ik - 1
                swaps_solution.append(((ik, jk), (ik - 1, jk)))
            #moving left
            while jk > j :
                jk = jk - 1
                swaps_solution.append(((ik, jk), (ik , jk - 1)))
            #end of the step
            if i == self.m:
                i = 0
                j = j+1
            else : 
                i = i+1

        return(swaps_solution)
            

        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

