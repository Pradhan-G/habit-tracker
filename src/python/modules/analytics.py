# src/python/modules/analytics.py

import datetime

class Analytics:
    def calculate_streak(self, habit):
        if not habit.completions:
            return 0
        
        sorted_dates = sorted(habit.completions, reverse=True)
        streak = 0
        today = datetime.date.today()

        for i, date in enumerate(sorted_dates):
            expected_date = today - datetime.timedelta(days=i)
            if habit.periodicity == "weekly":
                expected_date = today - datetime.timedelta(weeks=i)

            if date == expected_date:
                streak += 1
            else:
                break
        
        return streak
