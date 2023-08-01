
def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n



prime_object = prime_generator(100)


for i in prime_object:
    print(i)
