def increment(num):
    while num < 20:
        yield num
        num += 1


generators = [increment(10), increment(5), increment(0)]


while generators:
    current_task = generators[0]
    generators.remove(current_task)
    try:
        print(next(current_task))
        generators.append(current_task)
    except StopIteration:
        print("Task finished")
