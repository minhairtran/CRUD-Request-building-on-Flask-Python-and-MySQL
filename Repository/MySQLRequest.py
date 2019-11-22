import pymysql
from db_configuration import mysql
from Repository.MySQLService import point_to_mysql

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

def select_all_students():
	try:
		mysql_connector, cursor = point_to_mysql()
		cursor.execute("SELECT * FROM studentsdatabase")
		rows = cursor.fetchall()
		return rows
	except Exception as error:
		print(error)
	finally:
		cursor.close() 
		mysql_connector.close()

def select_a_student(id):
	try:
		mysql_connector, cursor = point_to_mysql()
		cursor.execute("SELECT * FROM studentsdatabase WHERE Student_ID = %s", id)
		row = cursor.fetchone()
		return row
	except Exception as error:
		print(error)
	finally:
		cursor.close() 
		mysql_connector.close()

def  add_student(student_info):
	sql = "INSERT INTO studentsdatabase(Student_ID, Student_name, Student_age) VALUES(%s, %s, %s)"
	mysql_connector = mysql.connect()
	cursor = mysql_connector.cursor(pymysql.cursors.DictCursor)
	cursor.execute(sql, student_info)
	mysql_connector.commit()
	return student_info

def  update_student(student_info):
	sql = "UPDATE studentsdatabase(Student_ID, Student_name, Student_age) VALUES(%s, %s, %s)"
	mysql_connector = mysql.connect()
	cursor = mysql_connector.cursor(pymysql.cursors.DictCursor)
	cursor.execute(sql, student_info)
	conn.commit()
	resp = jsonify('User added successfully!')
	resp.status_code = 200
	return resp

