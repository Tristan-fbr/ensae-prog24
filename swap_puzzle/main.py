from grid import Grid
from solver import Solver
from graph import Graph



"""
g = Grid(3,2)
#print(g)

h = Grid.random_grid(g)
#print(h_state)
print(type(h))
print("h", h)


i = Graph({})
result=Graph.A_star(i, h)
print("A*", result)
result_bis = Graph.efficient_bfs(i, h)
print('BFS', result_bis)





if result == result_bis : 
    print('True')"""

"""
aim = Grid(3, 1)

print(g)
#Grid.swap_seq(g, [((0,2), (1,2)),((0,2), (0,1))])
#print(g)
#print(Graph.bfs(i, g.state, aim.state))
Graph.A(i, g)
"""




"""
modified_list=[]
for e in g.state:
    modified_list.append(e)
s=Solver(modified_list)
swaps_solution = Solver.get_solution(s)

print("solutions", swaps_solution)
print(g)
print(Grid.is_sorted(g))
g = Grid.grid_from_file(file_name)
print(g)
"""



data_path = "C:/Users/cfrou/OneDrive/Bureau/Projet programmation/ensae-prog24/input/"
#attention : depuis le copier-coller du chemin du fichier, on a des antislashs au lieu de slashs
file_name = data_path + "graph2.in"

#print(file_name)


g = Graph.graph_from_file(file_name)
print(g)
print(Graph.bfs(g, 4, 3))

"""
new_grid = Grid(3,3)
print(new_grid)
new_grid.swap((1,1),(1,2))
new_grid.swap((1,2),(2,2))
new_grid.swap((0,1),(0,0))
new_grid.swap((1,0),(1,1))
new_grid.swap((2,2),(1,2))
new_grid.swap((1,1),(2,1))
new_grid.swap((1,1),(0,1))
new_grid.swap((2,0),(2,1))
new_grid.swap((2,2),(2,1))
print(new_grid)
print(new_grid.distance_grid())



import matplotlib.pyplot as plt

def create_table(data, title=None):
    plt.figure(figsize=(8, 6))
    plt.axis('off')
    if title:
        plt.title(title)
    table = plt.table(cellText=data, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.5, 1.5)
    plt.show()


create_table(data, title='Grid')
"""