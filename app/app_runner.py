from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(name = None):
    error = None
    return render_template('index.xhtml', name = name, error = error)

def run():
  app.run(debug = True, host = '0.0.0.0', port = 8080)

if __name__ == '__main__':
    run()