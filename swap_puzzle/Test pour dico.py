from grid import Grid
import heapq as hpq

g = Grid(2,2)
print(g)
h = Grid(3, 2)
v = Grid (3, 3)
heap = []
hpq.heappush(heap, (4, v))
hpq.heappush(heap, (3, h))
hpq.heappush(heap, (3, g))
min = hpq.nsmallest(heap)[1]
print(min)
print(heap)
