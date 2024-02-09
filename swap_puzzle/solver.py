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
        i = 0 #i et j sont les coordonnées cibles
        j = 0
        
        for 
        #Préparation de l'étape
        k = i*self.n + j + 1
        for a in (0,self.m) :
            for b in (0,self.n):
                if self.state[a][b] == k:
                    ik = a
                    jk = b
        #ajustements lignes
        while ik < i :
            ik = ik +1 
        while ik > i : 
            ik = ik - 1
        #déplacements à gauche
        while jk > j :
            jk = jk - 1
        #fin de l'étape
        if i == self.n:
            i = 0
            j = j+1
        else : 
            i = i+1

        
            

        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

