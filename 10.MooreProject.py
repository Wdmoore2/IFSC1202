class Student():
    def __init__(self, firstname, lastname, tnumber, scores):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.Grades = [float(score) if score else 0.0 for score in scores]

    def RunningAverage(self):
        non_blank_scores = [score for score in self.Grades if score != 0.0]
        if non_blank_scores:
            return sum(non_blank_scores) / len(non_blank_scores)
        return 0.0

    def TotalAverage(self):
        return sum(self.Grades) / len(self.Grades)

    def LetterGrade(self):
        average = self.TotalAverage()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

def main():
    with open('10.Project Student Scores.txt', 'r') as file:
        students = []
        for line in file:
            data = line.strip().split(',')
            firstname, lastname, tnumber, *scores = data
            student = Student(firstname, lastname, tnumber, scores)
            students.append(student)

    print(f"{'First Name':<12} {'Last Name':<12} {'ID':<12} {'Running Average':<12} {'Semester Average':<12} {'Letter Grade':<12}")
    print('-' * 72)
    for student in students:
        print(f"{student.firstname:<12} {student.lastname:<12} {student.tnumber:<12} {student.RunningAverage():<12.2f} {student.TotalAverage():<12.2f} {student.LetterGrade():<12}")

if __name__ == "__main__":
    main()