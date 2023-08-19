import random

text = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = ""
# for i in range(6):
#     password = password + random.choice(text)


chosen = random.sample(text, 6)
chosen = "".join(chosen)
print(chosen)
