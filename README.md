Student Tracker v5

This is a small Python project I made to practice working with functions, dictionaries, and JSON files. The program lets me add students, their subjects, and their scores, and then it gives a report about the class.

It can also save the data and load it again later.

Features

Add students with subjects and scores

Calculate average score for each student

Show the top student and the lowest student

Show the class average

Give every student a grade (A, B, C, F)

Count how many subjects each student has

Save all data in a JSON file

Search for old students from saved data

Show top 3 students based on average

How to Use

Run main.py

Choose a number from the menu

Follow the input instructions

Data is saved automatically when you use option 1

File Structure
main.py
student_data.py
calculations.py
tools.py
data_hundling.py
students.json

Data Example

This is how the saved JSON data looks:

{
  "01/05/2025 14:22:10": {
    "Amine": {"Math": 90, "English": 85},
    "Sara": {"Science": 92, "Math": 88}
  }
}

Why I Made It

I made this project to practice:

Breaking code into multiple files

Working with dictionaries

Returning values from functions

JSON save/load system

Debugging and improving ideas step by step

This is version 5, and my plan is to keep improving it in the future
