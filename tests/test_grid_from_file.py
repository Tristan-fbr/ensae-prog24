# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_GridLoading(unittest.TestCase):
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        self.assertEqual(g.m, 4)
        self.assertEqual(g.n, 2)
        self.assertEqual(g.state, [[1, 2], [3, 4], [5, 6], [8, 7]])

if __name__ == '__main__':
    unittest.main()



#code pour tester la fonction distance
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