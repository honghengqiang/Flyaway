from flask import Flask


@app.route('/')
def hello_world():
    return 'Hello World!'


def create_app():
    app = Flask(__name__)
    return app


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(port=8000, host='0.0.0.0')
