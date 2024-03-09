from grid import Grid
import time

a = 0
debut = time.time()
for i in range(0, 1000000):
    a +=1
fin = time.time()

print(fin - debut)
