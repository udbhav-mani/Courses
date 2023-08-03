from concurrent.futures import ThreadPoolExecutor
import time


def complex_calculation():
    start = time.time()
    [n**2 for n in range(40000000)]
    print(f"Complex Calculation took - {time.time()-start} seconds.")


def take_input():
    start = time.time()
    user_input = input("Enter our name - ")
    print(f"Hello, {user_input}.")
    print(f"Take input took - {time.time()-start} seconds.")


# creates a pool of threads
start = time.time()
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(take_input)

print(f"Total time it took - {time.time()-start} seconds.")
