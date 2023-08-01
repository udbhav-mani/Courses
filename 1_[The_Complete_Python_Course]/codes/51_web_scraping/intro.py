from bs4 import BeautifulSoup

SIMPLE_HTML = """<!DOCTYPE html>
<html>
    <head>
        <title>My web page</title>
    </head>
    <body>
        <h1>Hello, world!</h1>
        <p class = "subtitle">This is my first web page.</p>
        <p>It contains a 
             <strong>main heading</strong> and <em> paragraph </em>.
        </p>
    </body>
</html>"""
simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")

# print(simple_soup.findAll("p"))
# print(simple_soup.findAll("p", {"class":"subtitle"}))
plist = simple_soup.findAll("p")
strings = [
    string for string in plist if "subtitle" not in string.attrs.get("class", [])
]
# strings = [string for string in simple_soup.findAll("p")]
print(strings)
