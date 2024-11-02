from flask import (render_template,
                   request,
                   redirect,
                   url_for)
from requests import get, post

from .. import app



@app.get("/items/<token>")
def get_items(token: str):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = get(
        "http://127.0.0.1:8000/items",
        headers=headers,
    )
    if response.ok:
        return response.json()


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
        return redirect(url_for(
            get_items.__name__,
            token =  response.json().get("access_token")
            )
        )
    return response.json().get("detail")
