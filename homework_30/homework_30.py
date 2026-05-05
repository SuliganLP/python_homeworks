import json
from collections import defaultdict
from datetime import datetime


def student_courses_report():

    def collect_data():
        with open("student_courses.json", "r") as file:
            return json.load(file)

    students = collect_data()
    report = {}

    def count_students(students_list):
        report["total_students"] = len(students_list)

    def age_on_enrollment(students_list):
        enroll_age_list = []

        for student in students_list:
            birth_date = datetime.strptime(student["birth_date"], "%d.%m.%Y")
            enroll_date = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")

            enroll_age = enroll_date - birth_date
            enroll_age_list.append(enroll_age.days / 365)

        report["average_enrollment_age"] = round(sum(enroll_age_list) / len(enroll_age_list), 1)

    def students_on_courses(students_list):
        courses_dict = defaultdict(int)

        for student in students_list:
            for course in student["courses"]:
                courses_dict[course] += 1

        report["students_per_course"] = dict(sorted(courses_dict.items()))

    count_students(students)
    age_on_enrollment(students)
    students_on_courses(students)

    def save_report():
        with open("student_courses_report.json", "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4, ensure_ascii=False)

    save_report()


student_courses_report()
