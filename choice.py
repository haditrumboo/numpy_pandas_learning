import numpy as np

random = np.random.default_rng()

fruits = np.array(["apple", "banana", "grapes", "melon", "mango"])

fruit = random.choice(fruits, size=(3,2))

print(fruit)
