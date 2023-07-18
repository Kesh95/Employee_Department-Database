import mysql.connector
mydb = mysql.connector.connect(
  host="ccmg-dev-collance.c9u4fryy0ibx.ap-south-1.rds.amazonaws.com",
  user="training_user01",
  password="Collance@2023",
  database="training",
  autocommit=True,
)



def call(query):
  cursor = mydb.cursor()
  cursor.execute(query)
  myresult = cursor.fetchall()
  cursor.close()
  # mydb.close()
  return myresult










# from mysql import connector
# from mysqlx import errorcode
#
#
# def mysql_get_mydb():
#     '''Takes no args, and returns a connection to MYDB via MYSQL.'''
#
#     try:
#         cnx = connector.connect(host="ccmg-dev-collance.c9u4fryy0ibx.ap-south-1.rds.amazonaws.com",
#                                 user="training_user01",
#                                 password="Collance@2023",
#                                 database="training",
#                                 # raise_on_warnings=True,
#                                 # use_pure=False,
#                                 autocommit=True, )
#     except connector.Error as err:
#         if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with your user name or password")
#         elif err.errno == errorcode.ER_BAD_DV_ERROR:
#             print("Database does not exist")
#         else:
#             print(err)
#     # the else will happen if there was no error!
#     else:
#         cnx.close()
#     return cnx
