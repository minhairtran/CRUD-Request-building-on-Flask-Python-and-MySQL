from Repository.MySQLRequest import select_a_student, select_all_students, select_ids
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
		add_action = check_action(request_methods = request.method, to_do = "ADD", student_info = student_info)
		if(add_action == None):
			raise Exception()
		response = jsonify('User added successfully!')
		response.status_code = 200
		return response
	except Exception as e:
		print(e)

@app.route('/students')
def get_students():
	response = jsonify(select_all_students())
	response.status_code = 200
	return response

@app.route('/student/<int:id>')
def get_a_student(id):
	student = select_a_student(id)
	response = jsonify(student)
	response.status_code = 200
	return response

@app.route('/id')
def get_IDs():
	IDs = select_ids() 
	response = jsonify(IDs)
	response.status_code = 200
	return response

@app.route('/update', methods=['POST'])
def update_user():
	try:
		_json = request.json
		_id = _json["Student_ID"]
		_name = _json["Student_Name"]
		_age = _json['Student_Age']
		student_info = (_id, _name, _age)
		return check_action(request_methods = request.method, to_do = "UPDATE_STUDENT", student_info = student_info)
	except Exception as e:
		print("More information required.")

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