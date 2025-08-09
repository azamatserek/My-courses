import time

def linear_algo(n):
    total = 0
    for i in range(n):
        total += i
    return total

def quadratic_algo(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

# Time comparison
sizes = [100, 1000, 5000]

for n in sizes:
    start = time.time()
    linear_algo(n)
    end = time.time()
    print(f"Linear: n={n} | Time: {end - start:.6f} seconds")

for n in sizes:
    start = time.time()
    quadratic_algo(n)
    end = time.time()
    print(f"Quadratic: n={n} | Time: {end - start:.6f} seconds")
