import psycopg2

from database_info import database_info

def connect():
  c = psycopg2.connect(database=database_info.
                       database,user=database_info.user,
                       host=database_info.host,
                       password=database_info.password)
  return c

def get_all_toys():
  conn = connect()
  cur = conn.cursor()
  cur.execute("SELECT * FROM toys")
  toys = cur.fetchall()
  cur.close()
  conn.close()
  return toys

def add_toy(name):
  conn = connect()
  cur = conn.cursor()
  cur.execute("INSERT INTO toys (name) VALUES (%s)", (name,))
  conn.commit()
  cur.close()
  conn.close()
  
def update_toy(name,id):
  conn = connect()
  cur = conn.cursor()
  cur.execute("UPDATE toys  SET name = (%s) WHERE (id)=(%s)", (name,id,))
  conn.commit()
  cur.close()
  conn.close()
  
def deletind(id):
  conn = connect()
  cur = conn.cursor()
  cur.execute("DELETE FROM toys  WHERE (id)=(%s)",(id,))
  conn.commit()
  cur.close()
  conn.close()
  