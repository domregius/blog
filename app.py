from flask import Flask, render_template
import datetime

app = Flask("hello")

posts = [
    { "title": "meu primeiro post",
       "body": "aqui é o texto do post",
       "author": "regis",
        "created": datetime.datetime(2022,7,25)
        },

    { "title": "meu segundo post",
       "body": "aqui é o texto do segundo post",
       "author": "alberto",
        "created": datetime.datetime(2022,7,29)
        }
]

@app.route("/")

def index():
    return render_template('index.html', posts=posts)
    
@app.route("/login")
def login():
    return render_template('login.html', posts=posts)