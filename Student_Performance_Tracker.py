class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        if name in self.students:
            print(f"Student '{name}' already exists. Updating scores.")
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        if not self.students:
            print("No students to display.")
            return

        print("\nStudent Performance:")
        print("-" * 40)
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Name: {name}, Average: {average:.2f}, Status: {status}")
        print("-" * 40)
        class_avg = self.calculate_class_average()
        print(f"Class Average: {class_avg:.2f}")


def main():
    tracker = PerformanceTracker()

    print("Welcome to the Student Performance Tracker!")
    while True:
        try:
            name = input("Enter student name (or 'done' to finish): ").strip()
            if name.lower() == 'done':
                break
            scores = []
            for subject in ["Math", "Science", "English"]:
                while True:
                    try:
                        score = int(input(f"Enter {name}'s score for {subject}: "))
                        if 0 <= score <= 100:
                            scores.append(score)
                            break
                        else:
                            print("Score must be between 0 and 100. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            tracker.add_student(name, scores)
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    tracker.display_student_performance()


if __name__ == "__main__":
    main()