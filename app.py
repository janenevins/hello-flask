from flask import Flask

application = Flask(__name__)

@application.route('/foobarbaby')

def homepage():
    return "Hello messed up world!"

@application.route('/hello/<your_name>')
def hello(your_name):
    return "Hello {}!!!".format(your_name)

if __name__ == '__main__':
    application.run(debug=True, use_reloader=True)
