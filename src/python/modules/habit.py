# src/python/modules/habit.py

import datetime

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity  # "daily" or "weekly"
        self.completions = []  # List of datetime.date

    def complete(self, date=None):
        if date is None:
            date = datetime.date.today()
        self.completions.append(date)

    def last_completion(self):
        return self.completions[-1] if self.completions else None
