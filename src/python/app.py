# src/python/app.py

from modules.habit_manager import HabitManager
from modules.analytics import Analytics

def main():
    manager = HabitManager()
    analytics = Analytics()

    # Simple CLI
    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. List Habits")
        print("3. Complete Habit")
        print("4. View Streak")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Habit name: ")
            periodicity = input("Periodicity (daily/weekly): ")
            manager.add_habit(name, periodicity)
            print(f"Habit '{name}' added.")
        
        elif choice == "2":
            habits = manager.list_habits()
            print("Your habits:", habits)
        
        elif choice == "3":
            name = input("Which habit to complete?: ")
            habit = manager.find_habit(name)
            if habit:
                habit.complete()
                print(f"Habit '{name}' marked as completed!")
            else:
                print("Habit not found.")
        
        elif choice == "4":
            name = input("Which habit to view streak?: ")
            habit = manager.find_habit(name)
            if habit:
                streak = analytics.calculate_streak(habit)
                print(f"Streak for '{name}': {streak}")
            else:
                print("Habit not found.")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
