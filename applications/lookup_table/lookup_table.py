import math
import random
import time

# Create dictionary with(x, y) key-value pairs
hash_table = {}
begin_time = time.time()
for x in range(2, 15):
    for y in range(3, 7):
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        hash_table[(x, y)] = v
        print(f'Hash Table Generation: x={x}, y={y}')
end_time = time.time()
f'Time to generate hash table is {end_time-begin_time} seconds'
print(len(hash_table))

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    return hash_table[(x, y)]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
