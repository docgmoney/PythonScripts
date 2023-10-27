def mean(data):
    if type(data) == dict:
        the_mean = sum(data.values()) / len(data)
    else:
        the_mean = sum(data) / len(data)
    return the_mean

student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
print(f"{mean(student_grades):.2f}")