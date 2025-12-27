def get_student() :
    while True :
        student = input("Enter student name, 'Done' to finish, 'Exit' to quit: ").strip()

        if student.lower() in ("exit", "done"):
            return student.lower()
        if  student == '' :
            print("You need to enter a student name.")
            continue
        return student.capitalize()

def get_subject(student) :
    while True :
        subject = input(f"Enter subject name for the student {student} or 'done' to finish: ").strip()

        if subject.lower() == 'done' :
            return subject
        if subject == '' :
            print("You need to enter a subject name.")
            continue
        return subject

def get_score(student, subject) :
    while True :
        try :
            score = int(input(f"Score of {student} in {subject}: "))

            if score < 0 :
                print("You need to enter a positive number.")
                continue
            return score
        except ValueError :
            print("You need to enter a positive number.")
            continue

def student_data() :
    students = {}
    while True :
        student = get_student()
        if student == "exit" :
            print("Goodbye")
            break
        if student == "done" :
            break
        if student not in students :
            students[student] = {}

        while True :
            subject = get_subject(student)
            if subject == "done" :
                break
            score = get_score(student, subject)
            students[student][subject] = score

    return students

