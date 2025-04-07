# src/python/modules/habit_manager.py

from modules.habit import Habit

class HabitManager:
    def __init__(self):
        self.habits = []

    def add_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        self.habits.append(habit)

    def remove_habit(self, name):
        self.habits = [h for h in self.habits if h.name != name]

    def list_habits(self):
        return [habit.name for habit in self.habits]

    def find_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None
