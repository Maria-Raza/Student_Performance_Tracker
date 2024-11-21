# Student_Performance_Tracker
1. Student Class
Attributes: name (string), scores (list of integers).
Methods:
calculate_average(): Computes the average of the scores.
is_passing(passing_score=40): Checks if all scores are above or equal to the passing score (default 40).
2. PerformanceTracker Class
Attributes:
students: A dictionary with student names as keys and Student objects as values.
Methods:
add_student(name, scores): Adds or updates a student in the tracker.
calculate_class_average(): Computes the average score for all students.
display_student_performance(): Displays each student's performance and the class average.
3. Input Handling
Uses a loop to continuously accept input.
Ensures scores are valid integers within the range of 0 to 100 using try-except for error handling.
4. Output
Displays each student's name, average score, and pass/fail status.
Computes and displays the class average.
Example Output
plaintext
Copy code
Welcome to the Student Performance Tracker!
Enter student name (or 'done' to finish): Alice
Enter Alice's score for Math: 85
Enter Alice's score for Science: 90
Enter Alice's score for English: 78
Enter student name (or 'done' to finish): Bob
Enter Bob's score for Math: 35
Enter Bob's score for Science: 42
Enter Bob's score for English: 50
Enter student name (or 'done' to finish): done

Student Performance:
----------------------------------------
Name: Alice, Average: 84.33, Status: Passing
Name: Bob, Average: 42.33, Status: Needs Improvement
----------------------------------------
Class Average: 63.33
Additional Features (Optional)
Custom Passing Score: Allow the teacher to set a custom passing score.
Save/Load Data: Implement functionality to save data to a file and reload it later.
Graphical Analysis: Use libraries like Matplotlib to visualize performance trends.
