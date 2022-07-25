from flask import Flask

app = Flask("hello")

@app.route("/")

def hello():
    return "Hello world...."
    
@app.route("/meucontato")
def zebra():
    return """<html>
    <head>
        <title>Meu contato</title>
    <body>
        domregius
    </body>
    </head>
    
    <html>"""