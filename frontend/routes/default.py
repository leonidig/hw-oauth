from flask import (render_template,
                   request)
from requests import post

from .. import app

# @auth_app.get("/items/")
# @auth_app.get("/users/me")
# @auth_app.post("/token")

@app.get("/login")
def login():
    return render_template("login.html")


@app.post("/login")
def login_post():
    form_data = request.form.copy()
    username = form_data.get("username")
    password = form_data.get("password")
    data = {
        "username": username,
        "password": password,
    }
    response = post("http://127.0.0.1:8000/token", data=data)
    # if response.ok:
    if response.status_code == 200:
        return response.json()
    return response.json().get("detail")
