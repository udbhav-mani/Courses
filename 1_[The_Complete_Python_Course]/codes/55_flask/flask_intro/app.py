from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

posts = {
    0: {"id": 0, "title": "Post number 0 ", "content": "This is blog post number 0"},
    1: {"id": 1, "title": "Post number 1 ", "content": "This is blog post number 1"},
    2: {"id": 2, "title": "Post number 2 ", "content": "This is blog post number 2"},
    3: {"id": 3, "title": "Post number 3 ", "content": "This is blog post number 3"},
    4: {"id": 4, "title": "Post number 4 ", "content": "This is blog post number 4"},
    5: {"id": 5, "title": "Post number 5 ", "content": "This is blog post number 5"},
}


@app.route("/")
def homepage():
    return render_template("home.jinja2", posts=posts)


@app.route("/posts/<int:post_id>")
def post(post_id):
    single_post = posts.get(post_id)
    if not single_post:
        return render_template("404.jinja2", message=f"Post {post_id} not found!!")
    return render_template("post.jinja2", post=posts.get(post_id))


# not needed now
@app.route("/posts/form")
def form():
    return render_template("create.jinja2")


@app.route("/posts/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        contents = request.form.get("content")  # we use form to not get data in link
        posts_id = len(posts)

        posts[posts_id] = {"id": posts_id, "title": title, "content": contents}

        # return render_template("post.jinja2", post=posts.get(posts_id))
        # or
        return redirect(url_for("post", post_id=posts_id))
    return render_template("create.jinja2")


if __name__ == __name__:
    app.run(debug=True)
