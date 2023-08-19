import time, timeit


def pow(num):
    sum = 0
    for i in range(0, num):
        sum += num**num

    return sum


start_time = time.time()
# print(pow(1000))
end_time = time.time()

print(end_time - start_time)

# also like this
print(timeit.timeit("[x**x for x in range(100)]"))
