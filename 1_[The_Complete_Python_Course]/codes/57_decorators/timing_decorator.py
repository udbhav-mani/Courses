import time


def timer(fun):
    def time_it(*args, **kwargs):
        start = time.time()
        fun(*args, **kwargs)
        print(time.time() - start)

    return time_it


@timer  # this = [timer(hello)()] or hello = timer(hello) = time_it
def hello():
    print("Hello world!!")
    time.sleep(3)

# hello = timer(hello) = time_it

hello()
