from app import db, Computer
# import psycopg2

# class database_info():
#     database="testdb"
#     user="pgadmin"
#     host="127.0.0.1"
#     password="secure_password"

# def connect():
#   c = psycopg2.connect(database=database_info.
#                        database,user=database_info.user,
#                        host=database_info.host,
#                        password=database_info.password)
#   return c

# conn = connect()
# cur = conn.cursor()
  
# create the tables in our database....there is a better way to do this we will see soon!
db.create_all()

# create two instances of our class
my_mac = Computer('Macbook Pro', 8)
my_acer = Computer('Aspire V15', 16)

my_mac.name # Macbook Pro
my_mac.memory_in_gb # 8
my_mac.id # None

# Whoa, what happened to our id? We don't have one yet because we have not saved it!

# first we need to add our instances individually (or use the add_all method which accepts a list)
db.session.add(my_mac)
db.session.add(my_acer)

# save it in the database
db.session.commit()

my_mac.id # 1
my_acer.id # 2

# cur.close()
# conn.close()