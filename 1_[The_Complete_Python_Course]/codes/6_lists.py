dogs = ["lab", "golden", "pug", "husky"]
print(dogs)
print(dogs[0])

dogs.append("Shih-tzu")
print(dogs)

dogs.remove("pug")
print(dogs)

dogs_with_age = [["lab", 10], ["golden", 12], ["husky", 13]]
print(dogs_with_age)
dogs = ["lab", "golden", "husky"]  # can be heterogeneous
print(dogs)
print(len(dogs))

# join keyword
dogs_name = ", ".join(dogs)

print(dogs_name)
