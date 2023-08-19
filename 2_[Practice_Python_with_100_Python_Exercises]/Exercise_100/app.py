from flask import Flask, render_template, request

app = Flask(__name__)


def validate_username(username):
    with open("users.txt", "r") as file:
        contents = file.read().strip().split("\n")
        if username in contents:
            return False
        else:
            return True


def validate_password(password):
    result1 = any(char.isdigit() for char in password)
    result2 = any(char.isupper() for char in password)
    result3 = len(password) >= 5

    errors = list()
    if not result3:
        errors.append("Length is less than 5!")
    if not result2:
        errors.append("An uppercase letter is missing in the password!")
    if not result1:
        errors.append("A number is missing in the password!")

    return errors


@app.route("/")
def homepage():
    return render_template("app.html")


@app.route("/sent", methods=["GET", "POST"])
def sent():
    if request.method == "POST":
        line = request.form
        user_name = line.get("username")
        if not validate_username(user_name):
            return render_template("app.html", message="Username exists!" + "<br>")

        password = line.get("password")
        errors = validate_password(password=password)
        if len(errors) > 0:
            return render_template("app.html", message="Password not good!" + "<br>")

    return render_template("app.html", message="Success")


if __name__ == __name__:
    app.run(debug=True)
