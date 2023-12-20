class CalorieTracker:
    def __init__(self, total_burned_calories=0, total_consumed_calories=0):
        self.total_burned_calories = total_burned_calories
        self.total_consumed_calories = total_consumed_calories

    def add_record(self, burned_calories, consumed_calories):
        new_burned_calories = self.total_burned_calories + burned_calories
        new_consumed_calories = self.total_consumed_calories + consumed_calories

        return CalorieTracker(new_burned_calories, new_consumed_calories)

    def display_totals(self):
        print("Total Burned Calories:", self.total_burned_calories)
        print("Total Consumed Calories:", self.total_consumed_calories)

tracker = CalorieTracker()

tracker = tracker.add_record(burned_calories=300, consumed_calories=500)

tracker.display_totals()
