from Service import check_action
from app import app
from flask import request, jsonify

@app.route('/add', methods=['POST'])
def receive_student_info():
	try:
		_json = request.json
		_id = _json["Student_ID"]
		_name = _json["Student_Name"]
		_age = _json['Student_Age']
		student_info = (_id, _name, _age)
		action = check_action(request_methods = request.method, to_do = "ADD", student_info = student_info)
		response = jsonify(f'Student {action} added successfully!')
		response.status_code = 200
		return response
	#id hoac name hoac age = null
	except TypeError:
		print("More information needed")

@app.route('/students')
def get_students():
	_json = request.json
	action = check_action(request_methods = request.method, to_do = "GET_STUDENTS", student_info = None)
	response = jsonify(action)
	response.status_code = 200
	return response

@app.route('/student/<int:id>')
def get_a_student(id):
	_json = request.json
	action = check_action(request_methods = request.method, to_do = "GET_A_STUDENT", student_info = id)
	response = jsonify(action)
	response.status_code = 200
	return response

@app.route('/id')
def get_IDs():
	_json = request.json
	check_action(request_methods = request.method, to_do = "GET_IDS", student_info = None)
	response = jsonify("This is all IDs of the students")
	response.status_code = 200
	return response

@app.route('/update', methods=['POST'])
def update_student():
	try:
		_json = request.json
		_id = _json["Student_ID"]
		_name = _json["Student_Name"]
		_age = _json['Student_Age']
		student_info = (_id, _name, _age)
		update_action = check_action(request_methods = request.method, to_do = "UPDATE_STUDENT", student_info = student_info)
		response = jsonify(f'Student {update_action} updated successfully!')
		response.status_code = 200
		return response
	except TypeError:
		print("More information needed")

@app.route('/delete/<int:id>')
def delete_student(id):
	delete_action = check_action(request_methods = request.method, to_do = "DELETE", student_info = id)
	if(delete_action == None):
		raise Exception()
	response = jsonify("Student deleted")
	response.status_code = 200
	return response

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