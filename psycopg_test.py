from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def main():
  # Establish the connection with the database
  # Also knows as 'Starting a session' or 'Begins a transaction'
  conn = psycopg2.connect('dbname=example user=postgres password=1234')

  # Set a Cursor obj to executing commands
  cursor = conn.cursor() # interface to queue transactions

  cursor.execute('DROP TABLE IF EXISTS table2;')

  cursor.execute('''
    CREATE TABLE table2 (
      id INTEGER PRIMARY KEY,
      completed BOOLEAN NOT NULL DEFAULT False
    );
  ''')

  # Plain SQL statement
  cursor.execute('''
    INSERT INTO table2 (id, completed) VALUES (2, false);
  ''')

  # Passing a Tuple as a 2nd arg
  cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

  # Passing a Dict as a 2nd arg
  cursor.execute('INSERT INTO table2 (id, completed)' +
  ' VALUES (%(id)s, %(completed)s);', {
    'id': 3,
    'completed': False
  })

  # Passing Dict and Transaction into variables
  data = {'id': 4, 'completed': True}
  transaction = 'INSERT INTO table2 (id, completed)' + ' VALUES (%(id)s, %(completed)s);'
  cursor.execute(transaction, data)

  # Execute a SELECT statement
  cursor.execute('SELECT * from table2;')

  # Fetch all results from previous cursor.execute
  # result1 = cursor.fetchall()
  # print('fetchall - result1 =>',result1)

  # Fetch as many results as indicated by the argument
  result2 = cursor.fetchmany(3)
  print('fetchmany(3) - result2 =>',result2)

  # Fetch first row from the result set
  # It'd be None if a previous fetch take all the results
  result3 = cursor.fetchone()
  print('fetchone - result3 =>',result3)

  # Commit the transaction ~~ Comprometer la ejecucion de la transaccion
  conn.commit()

  # Close the cursor and the connection with the database
  conn.close()
  cursor.close()
  return
