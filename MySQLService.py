import pymysql
from db_configuration import mysql

def exist(new_student_ID):
	select_id = select_ids()
	for id in select_id:
		#Convert string to list and dict to list
		if([int(new_student_ID)] == [*id.values()]):
			return True
	return False

def point_to_mysql():
	mysql_connector = mysql.connect()
	cursor = mysql_connector.cursor(pymysql.cursors.DictCursor)
	return mysql_connector, cursor

def select_ids():
	try:
		mysql_connector, cursor = point_to_mysql()
		cursor.execute("SELECT Student_ID FROM ")
		columns = cursor.fetchall()
		return columns
	except Exception as error:
		print(error)
	finally:
		cursor.close() 
		mysql_connector.close()