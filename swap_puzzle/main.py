from grid import Grid
from solver import Solver

g = Grid(2, 3)
print(g)
Grid.swap(g, (0,2), (1,2))
print(g)



data_path = "C:/Users/cfrou/OneDrive/Bureau/Projet programmation/ensae-prog24/input/"
#attention : depuis le copier-coller du chemin du fichier, on a des antislashs au lieu de slashs
file_name = data_path + "grid0.in"

print(file_name)


g = Grid.grid_from_file(file_name)
print(g)
