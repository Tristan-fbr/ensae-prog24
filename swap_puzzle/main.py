from grid import Grid
from solver import Solver

g = Grid(2, 3)
print(g)
Grid.swap_seq(g, [((0,2), (1,2)),((0,2), (0,1))])
print(g)

modified_list=[]
for e in g.state:
    modified_list.append(e)
s=Solver(modified_list)
swaps_solution = Solver.get_solution(s)

print("solutions", swaps_solution)
print(g)
print(Grid.is_sorted(g))

"""
data_path = "C:/Users/cfrou/OneDrive/Bureau/Projet programmation/ensae-prog24/input/"
#attention : depuis le copier-coller du chemin du fichier, on a des antislashs au lieu de slashs
file_name = data_path + "grid0.in"

print(file_name)


g = Grid.grid_from_file(file_name)
print(g)
"""