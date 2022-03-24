import logging

import requests
from chalice import Chalice

app = Chalice(app_name="chalice-with-cdk")
app.debug = True
app.log.setLevel(logging.DEBUG)


@app.route("/")
def index():
    response = requests.get("http://httpbin.org/ip")
    return response.json()


@app.route("/posts")
def posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()


@app.route("/post/{post_id}")
def post(post_id):
    app.log.info(f"Checking for post id: {post_id}")
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    return response.json()
