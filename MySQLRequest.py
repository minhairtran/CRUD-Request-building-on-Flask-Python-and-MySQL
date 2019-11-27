import pymysql
from db_configuration import mysql
from MySQLService import point_to_mysql, exist


def select_ids():
    try:
        mysql_connector, cursor = point_to_mysql()
        cursor.execute("SELECT Student_ID FROM studentsdatabase")
        columns = cursor.fetchall()
        return columns
    except pymysql.err.ProgrammingError:
        print("Table doesn't exist")


def select_all_students():
    try:
        mysql_connector, cursor = point_to_mysql()
        cursor.execute("SELECT * FROM studentsdatabase")
        rows = cursor.fetchall()
        return rows
    except pymysql.err.ProgrammingError:
        print("Table doesn't exist")


def select_a_student(id):
    try: 
        if(not exist(id)):
            raise Exception()
        mysql_connector, cursor = point_to_mysql()
        cursor.execute("SELECT * FROM studentsdatabase WHERE Student_ID = %s", id)
        row = cursor.fetchone()
        return row
    except Exception:
        print("Student doesn't exist")


def add_student(student_info):
    try:
        new_student_ID = student_info[0]
        if(exist(new_student_ID)):
            raise Exception()
        sql = "INSERT INTO studentsdatabase(Student_ID, Student_name, Student_age) VALUES(%s, %s, %s)"
        mysql_connector = mysql.connect()
        cursor = mysql_connector.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, student_info)
        mysql_connector.commit()
        return student_info
    except Exception:
        print("Student exist")


def update_student(student_info):
    try:
        new_student_ID = student_info[0]
        if(not exist(new_student_ID)):
            raise Exception()
        sql = "UPDATE studentsdatabase SET Student_Name=%s, Student_Age=%s WHERE Student_ID=%s"

        # rearrange list as [name, age, id]
        student_info = (student_info[1], student_info[2], student_info[0])
        mysql_connector, cursor = point_to_mysql()
        cursor.execute(sql, student_info)
        mysql_connector.commit()
        return student_info
    except Exception:
        print("Student doesn't exist")

def delete_student(id):
    try:
        if(not exist(id)):
            raise Exception()
        mysql_connector, cursor = point_to_mysql()
        cursor.execute(
            "DELETE FROM studentsdatabase WHERE Student_ID=%s", (id,))
        mysql_connector.commit()
        return id
    except Exception:
        print("Student doesn't exist")