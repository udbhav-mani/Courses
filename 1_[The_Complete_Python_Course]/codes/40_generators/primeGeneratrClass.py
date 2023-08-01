# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop
        self.i = 2

    def __next__(self):
        for n in range(2, self.i):
            if self.i % n == 0:
                self.i += 1
                self.__next__()
        else:
            var = self.i
            self.i += 1
            return var


gen = PrimeGenerator(100)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
