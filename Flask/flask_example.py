from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Postgres config variables              dialect     username pass host      port database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # avoid warning

# Open a connection
db = SQLAlchemy(app)

@app.route('/') #Python decorator
def index():
  return "Hello, world!"

if __name__ == '__main__':
  app.run()
