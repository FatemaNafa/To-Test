from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QWidget
import sys

class StudentCourseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # This is the main window
        self.setWindowTitle("Student Course List")
        self.setGeometry(200, 200, 400, 300)

        # Create a main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Create input fields and labels
        self.name_label = QLabel("Student Name:")
        self.name_input = QLineEdit()
        self.course_label = QLabel("Course:")
        self.course_input = QLineEdit()

        # Add input fields to layout
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.course_label)
        layout.addWidget(self.course_input)

        # Create and add Add button
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_entry)
        layout.addWidget(self.add_button)

        # Create and add list widget to display entries
        self.student_list = QListWidget()
        layout.addWidget(self.student_list)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

    def add_entry(self):
        # Get the name and course from input fields
        name = self.name_input.text()
        course = self.course_input.text()

        # Validate input and add to list
        if name and course:
            self.student_list.addItem(f"Student: {name}, Course: {course}")
            self.name_input.clear()
            self.course_input.clear()
        else:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter both student name and course.")

def main():
    app = QApplication(sys.argv)
    window = StudentCourseApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
