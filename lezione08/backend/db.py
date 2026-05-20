import mysql.connector as sql

def fetchall(query, params):
  conn = sql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="verificaChat"
  )
  cursor = conn.cursor()
  cursor.execute(query, params)
  return cursor.fetchall()

def fetchone(query, params):
  conn = sql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="verificaChat"
  )
  cursor = conn.cursor()
  cursor.execute(query, params)
  return cursor.fetchone()

def execute(query, params):
  conn = sql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="verificaChat"
  )
  cursor = conn.cursor()
  cursor.execute(query, params)
  conn.commit()