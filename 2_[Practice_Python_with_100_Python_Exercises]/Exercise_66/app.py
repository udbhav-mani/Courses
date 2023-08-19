# Create an English to Portuguese translation program.

# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.


def vocab(word):
    return d.get(word)


d = dict(weather="clima", earth="terra", rain="chuva")
user_input = input("Enter word: ")
print(vocab(user_input))
