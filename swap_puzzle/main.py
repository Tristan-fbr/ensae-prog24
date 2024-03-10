from grid import Grid
from solver import Solver
from graph import Graph


def list_to_tuple(liste):
    tuple_result = []
    for inner_list in liste:
        tuple_result.append(tuple(inner_list))
    return tuple(tuple_result)


"""
How to create a random grid.
"""
g = Grid(3,3)
h = Grid.random_grid(g)

 
"""
How to have a graphic representation of the grid
"""
Grid.graphic_rep(h)


"""
Example of use of is_sorted
"""
print("Pour g :", Grid.is_sorted(g),"\n"+"Pour h :", Grid.is_sorted(h))


"""
Example of use of get_solution
"""
s = Solver(h.state)
swaps_solution = Solver.get_solution(s)
print("solved h\n", h)


"""
Example of use of the bfs and the function graph_from_file.
"""
data_path = "C:/Users/cfrou/OneDrive/Bureau/Projet programmation/ensae-prog24/input/"
file_name = data_path + "graph2.in"
i = Graph.graph_from_file(file_name)
print(Graph.bfs(i, 12, 7))


"""
How to solve the swap problem using the naive bfs
Here we recreate a new grid of smaller dimensions (2 x 2).
"""
g = Grid(2,2)
h = Grid.random_grid(g)
dico = Grid.dict(h)
graph = Graph(dico)
print("BFS", Graph.bfs(graph, list_to_tuple(h.state), list_to_tuple(g.state)))


"""
How to solve the swap problem using the efficient bfs.
With this we can go for a larger grid.
"""
g = Grid(3,2)
h = Grid.random_grid(g)
i = Graph({})
print("efficient BFS", Graph.efficient_bfs(i, h))


"""
How to solve the swap problem using A*
The grid here is much larger.
"""
g = Grid(3,3)
h = Grid.random_grid(g)
i = Graph({})
print("A* ", Graph.A_star(i, h))