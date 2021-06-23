from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/') #Python decorator
def index():
  return "Hello, world!"

if __name__ == '__main__':
  app.run()
