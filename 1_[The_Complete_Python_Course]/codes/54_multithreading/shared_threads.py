import time
import random
from threading import Thread


#  atomic statements cant be stopped middleway like print()
#  when there is a shared state, we should be very careful

counter = 0


def increment():
    # specifying we need to use global value
    global counter
    counter += 1
    time.sleep(random.random())
    print(f"New Counter Value - {counter}.")
    time.sleep(random.random())
    print("----------------------------")


if __name__ == "__main__":
    for i in range(10):
        #  after using threads it starts to mess up
        # we use queue to stp this random behaviour
        time.sleep(random.random())
        thread = Thread(target=increment)
        thread.start()
