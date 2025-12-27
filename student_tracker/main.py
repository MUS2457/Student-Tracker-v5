import student_data
import calculations
import tools
import data_hundling   

def menu():
    print("\n--- Welcome to Student Tracker v5 ---")
    print("1. Add students and show report")
    print("2. Search a student")
    print("3. Top 3 students")
    print("4. Load old data")
    print("5. Exit")

def main():

    while True:
        menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            user_data = student_data.student_data()

            # Run calculations
            averages = calculations.average(user_data)
            top, low = calculations.get_top_low(user_data)
            class_average = calculations.get_class_average(user_data)
            grades = calculations.get_grade(user_data)
            subject_count = calculations.subject_count(user_data)

            # Show results
            print("\n--- Average Per Student ---")
            for name, avg in averages.items():
                print(f"{name}: {avg}")

            print(f"\nTop student: {top}")
            print(f"Lowest student: {low}")
            print(f"Class average: {class_average}")

            print("\n--- Grade Per Student ---")
            for name, grade in grades.items():
                print(f"{name}: {grade}")

            print("\n--- Subjects Per Student ---")
            for name, count in subject_count.items():
                print(f"{name}: {count}")

            # Save results
            data_hundling.save_user_data(user_data)
            print("\nData saved successfully!")

        elif choice == "2":
            name, info = tools.search_students()
            print(f"\nInformation for '{name}': {info}")

        elif choice == "3":
            top_three = tools.top_three_students()
            print(f"\nTop 3 students: {top_three}")

        elif choice == "4":
            old_data = data_hundling.load_user_data()
            print("\nOld data loaded:")
            print(old_data)

        elif choice == "5":
            print("Thank you for using Student Tracker v5! Goodbye!")
            break

        else:
            print("Invalid option, choose 1 to 5.")
            continue

if __name__ == "__main__":
    main()
