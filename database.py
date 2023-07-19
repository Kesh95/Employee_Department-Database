import mysql.connector
from mysql.connector import pooling

poolsize = 5
poolname='Project'
connectionpool= mysql.connector.pooling.MySQLConnectionPool(pool_name=poolname,pool_size=poolsize,host="ccmg-dev-collance.c9u4fryy0ibx.ap-south-1.rds.amazonaws.com",
  user="training_user01",
  password="Collance@2023",
  database="training",
  autocommit=True,)



def call(query):
  connection = connectionpool.get_connection()
  cursor = connection.cursor()
  cursor.execute(query)
  myresult = cursor.fetchall()
  cursor.close()
  return myresult










