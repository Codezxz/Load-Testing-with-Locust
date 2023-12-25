from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_report():
    return {'Alpha':'1'}

if __name__ == '__main__':
    app.run()