from threading import Thread
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


start = time.time()
complex_calculation()
take_input()
print(f"Total time it took - {time.time()-start} seconds.")


#  we can use threads to achieve cooperative muti tasking


thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=take_input)

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Total time mutitasking took - {time.time()-start} seconds.")
