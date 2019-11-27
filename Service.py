from MySQLRequest import add_student, update_student, delete_student, select_a_student, select_all_students, select_ids
from MySQLService import exist


def check_action(request_methods, to_do, student_info):
    if (request_methods == "POST"):
        if (to_do == "ADD"):
            return add_student(student_info) 
        if (to_do == "UPDATE_STUDENT"):
            return update_student(student_info)
    if(request_methods == "GET"):
        if(to_do == "DELETE"):
            return delete_student(student_info)
        if(to_do == "GET_STUDENTS"):
            return select_all_students()
        if(to_do == "GET_A_STUDENT"):
            return select_a_student(student_info)
        if(to_do == "GET_IDS"):
            return select_ids() 
    return None
