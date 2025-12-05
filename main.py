"""
Educational Hub and Spoke Project
Main hub that orchestrates calls to modular spokes
"""

from modules import greetings, calculations, data_processing

def main():
    """Main hub function that coordinates all spoke modules"""
    
    print("=" * 50)
    print("Educational Hub and Spoke Project")
    print("=" * 50)
    print()
    
    # Spoke 1: Greetings Module
    print("--- GREETINGS MODULE ---")
    greeting_message = greetings.get_greeting("User")
    print(greeting_message)
    print()
    
    # Spoke 2: Calculations Module
    print("--- CALCULATIONS MODULE ---")
    numbers = [10, 20, 30, 40, 50]
    total = calculations.sum_numbers(numbers)
    average = calculations.average_numbers(numbers)
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print()
    
    # Spoke 3: Data Processing Module
    print("--- DATA PROCESSING MODULE ---")
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "Diana", "score": 95}
    ]
    processed_data = data_processing.process_student_data(students)
    print("Student Data:")
    for key, value in processed_data.items():
        print(f"  {key}: {value}")
    print()
    
    print("=" * 50)
    print("Project Complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()