from flask import Flask, render_template, request, redirect, url_for
import database_module

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        password_confirm = request.form["password_confirm"]

        if password != password_confirm:
            return render_template("register.html", error="Passwords do not match")

        database_module.add_user(username, email, password)

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = database_module.get_user(email, password)
        if user:
            return redirect(url_for("groups"))
        else:
            return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")

@app.route("/groups")
def groups():
    groups = database_module.get_groups()
    return render_template("groups.html", groups=groups)

@app.route("/bills/<group_id>")
def bills(group_id):
    bills = database_module.get_bills(group_id)
    return render_template("bills.html", bills=bills)

if __name__ == "__main__":
    app.run(debug=True)
