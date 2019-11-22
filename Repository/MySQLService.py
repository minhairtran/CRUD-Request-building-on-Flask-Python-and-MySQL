import pymysql
from db_configuration import mysql


def exist(new_student_ID):
	select_id = select_ids()
	for id in select_id:
		if(new_student_ID == id):
			return True
	return False

def point_to_mysql():
	mysql_connector = mysql.connect()
	cursor = mysql_connector.cursor(pymysql.cursors.DictCursor)
	return mysql_connector, cursor

def select_ids():
	try:
		mysql_connector, cursor = point_to_mysql()
		cursor.execute("SELECT Student_ID FROM studentsdatabase")
		columns = cursor.fetchall()
		return columns
	except Exception as error:
		print(error)
	finally:
		cursor.close() 
		mysql_connector.close()