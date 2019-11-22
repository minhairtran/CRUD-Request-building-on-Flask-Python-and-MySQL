from Repository.MySQLRequest import add_student, update_student
from Repository.MySQLService import exist

def check_action(request_methods, to_do, student_info):
	try:
		if (request_methods == "POST" and to_do == "ADD"):
			new_student_ID = student_info[0]
			if(exist(new_student_ID)):
				raise Exception("Student ID exists")
			add_student(student_info)
			return student_info
		if (request_methods == "POST" and to_do == "UPDATE_STUDENT"):
			update_student(student_info)
			return student_info
	except Exception as e:
		print("Unknown action.")



