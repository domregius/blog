from flask import Flask, render_template

app = Flask("hello")

@app.route("/")

def hello():
    return "Hello world...."
    
@app.route("/meucontato")
def zebra():
    return render_template('index.html')
        