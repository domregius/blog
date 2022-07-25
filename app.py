from flask import Flask

app = Flask("hello")

@app.route("/")

def hello():
    return "Hello world...."
    
@app.route("/meucontato")
def zebra():
    return "domregius@gmail.com"