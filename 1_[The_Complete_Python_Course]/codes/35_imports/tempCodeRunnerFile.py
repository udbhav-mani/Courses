import utils.file_functions as fe

contents = """
Hello World,
This is the text from the lecture which taught us 
- importing from a file
Tried utils"""

filename = "data.txt"

fe.save_to_file(filename, contents)
fe.read_from_file(filename)
