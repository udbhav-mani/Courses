import time
from multiprocessing import Process


def complex_calculation():
    start = time.time()
    [n**2 for n in range(40000000)]
    print(f"Complex Calculation took - {time.time()-start} seconds.")


def take_input():
    start = time.time()
    user_input = input("Enter our name - ")
    print(f"Hello, {user_input}.")
    print(f"Take input took - {time.time()-start} seconds.")


if __name__ == "__main__":
    process1 = Process(target=complex_calculation)
    # this give use error ->
    # process2 = Process(target=take_input)
    # because both the process are trying to access the terminal simultaneously

    # if we do  this ->
    process2 = Process(target=complex_calculation)
    # it will be a great benefit of time to us

    start = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()

    print(f"Total time it took - {time.time()-start} seconds.")


