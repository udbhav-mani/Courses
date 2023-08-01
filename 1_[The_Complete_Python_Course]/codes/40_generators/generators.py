def count_to_two():
    i = 1
    while i <= 100:
        yield i
        i += 1


# def gen():
#     i = 1
#     for i in range(100):
#         i += 1
#         yield i


gen_obj = count_to_two()


for i in gen_obj:
    print(i)

print(next(gen_obj))


# for i in gen():
#     print(i)
