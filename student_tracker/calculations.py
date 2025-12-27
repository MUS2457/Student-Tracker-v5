def average(data):
    averages = {}
    if not data :
        return {}
    else :
        for names,subject in data.items():
           all_scores = list(subject.values())
           average_per_student = round(sum(all_scores) / len(all_scores), 2)
           averages[names] = average_per_student

        return averages

def get_top_low(data):
    if data :
        dictionary = average(data)
        top_student = max(dictionary, key=dictionary.get)
        lowest_student = min(dictionary, key=dictionary.get)
        return top_student, lowest_student

    return None,None

def get_class_average(data):
    if data :
        dictionary = average(data)
        class_average = round(sum(dictionary.values()) / len(dictionary), 2)
        return class_average
    return None

def get_grade(data):
    if data :
        averages = average(data)
        grades = {}
        for name, score in averages.items():
            if 90 <= score <= 100:
                grade = "A"
            elif 70 <= score <= 89:
                grade = "B"
            elif 50 <= score <= 69:
                grade = "C"
            else:
                grade = "F"

            grades[name] = grade

        return grades

    return {}

def subject_count(data):
        subject_counter = {}
        if data :
            for name, subject in data.items():
                subject_counter[name] = len(subject)
            return subject_counter

        return {}
