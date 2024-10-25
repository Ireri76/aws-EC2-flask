from flask import Flask
application = Flask(__name__)

@application.route('/')
def index():
 return 'Welcome to flask app'

if __name__ == "__main__":
 application.run()
