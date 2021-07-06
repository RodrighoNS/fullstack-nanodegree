from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Postgres config variables              dialect     username pass host      port database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # avoid warning

# Open a connection
db = SQLAlchemy(app)

# Classes
class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

  # Representation, useful for debugging
  def __repr__(self):
    return f'\n<Person ID: {self.id} - Name: {self.name}>'

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/') #Python decorator
def index():
  # Get the 1st record from a model
  persons = Person.query.all()
  for person in persons:
    return "Hola " + person.name

if __name__ == '__main__':
  app.run()
