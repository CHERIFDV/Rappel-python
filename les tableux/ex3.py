import numpy as np

x = np.random.randint(0,9,size=(10))

for i in range(1,11):
    i%2 == 0 and print(i)
