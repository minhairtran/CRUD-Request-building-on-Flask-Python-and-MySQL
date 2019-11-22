import pymysql
from app import app
from db_configuration import mysql
from flask import jsonify
from flask import Flask, request
from Repository.MySQLRequest import update_student
		
@app.route('/add', methods=['POST'])
def add_student():
	try:
		_json = request.json
		_id = _json["Student_ID"]
		_name = _json["Student_Name"]
		_age = _json['Student_Age']
			# validate the received values
		if _name and _id and _age and request.method == 'POST':
				# save edits
			sql = "INSERT INTO studentsdatabase(Student_ID, Student_name, Student_age) VALUES(%s, %s, %s)"
			data = (_id, _name, _age)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/users')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM studentsdatabase")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as error:
		print(error)
	finally:
		cursor.close() 
		conn.close()
		
		
@app.route('/users/<int:id>')
def user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM studentsdatabase WHERE Student_ID = %s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as error:
		print(error)
	finally:
		cursor.close() 
		conn.close()

#Update name and age of a student
@app.route('/update', methods=['POST'])
def update_user():
	try:
		_json = request.json
		_id = _json['Student_ID']
		_name = _json['Student_Name']
		_age = _json['Student_Age']		
		# validate the received values
		if _name and _age and _id and request.method == 'POST':
			# save edits
			sql = "UPDATE studentsdatabase SET Student_Name=%s, Student_Age=%s WHERE Student_ID=%s"
			data = (_name, _age, _id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as error:
		print(error)	
	finally:
		conn.close()
		

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()