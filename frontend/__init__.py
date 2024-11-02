from flask import Flask


app = Flask("frontend")


from . import routes

