d = dict(weather="clima", earth="terra", rain="chuva")


def vocab(word):
    return d.get(word.lower())


user_input = input("Enter word: ")
translation = vocab(user_input)
if translation is not None:
    print(translation)
else:
    print("We couldn't find that word!")
