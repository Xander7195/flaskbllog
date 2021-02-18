
# @app.route("/")
# def hello():
#     return "<h1>Hello World</h1>"
from flaskblog import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)