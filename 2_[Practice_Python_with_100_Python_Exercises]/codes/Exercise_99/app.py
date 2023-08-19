from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("app.html")


@app.route("/sent", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        line = request.form
        # print(line.get("title"))
        with open("data.txt", "a+") as file:
            file.write(line.get("title") + "\n")

    return render_template("app.html")


if __name__ == __name__:
    app.run(debug=True)
