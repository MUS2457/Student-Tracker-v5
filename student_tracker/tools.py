from calculations import average
import data_hundling
def search_students():
    data = data_hundling.load_user_data()
    while True :
        student_name = input("Enter student name or 'exit' to quit : ").strip()
        if student_name.lower() == 'exit' :
            return None,None
        capital_name = student_name.capitalize()
        for timestamp,students in data.items():
            if capital_name in students:
                return capital_name,students[capital_name]
        else :
            print("Student not found")
            continue

def top_three_students():
    loaded_data = data_hundling.load_user_data()
    combined = {}
    if loaded_data :
        for timestamp,students in loaded_data.items():
            for name,subject in students.items():
                combined[name] = subject
        averages = average(combined)
        list_student = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:3]
        return list_student
    return []
