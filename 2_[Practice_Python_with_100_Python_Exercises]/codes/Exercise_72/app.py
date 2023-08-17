import webbrowser

user_input = input("Enter query term - ")
webbrowser.open(f"https://www.google.com/search?q={user_input}")
