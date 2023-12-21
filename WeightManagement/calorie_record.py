class CalorieTracker:
    def __init__(self, total_burned_calories=0, total_consumed_calories=0):
        self.total_burned_calories = total_burned_calories
        self.total_consumed_calories = total_consumed_calories

    def add_record(self, burned_calories=None, consumed_calories=None):
        if burned_calories is None:
            burned_calories = 0
        if consumed_calories is None:
            consumed_calories = 0

        new_burned_calories = self.total_burned_calories + burned_calories
        new_consumed_calories = self.total_consumed_calories + consumed_calories

        return CalorieTracker(new_burned_calories, new_consumed_calories)

    def display_totals(self):
        print("\n=== Calorie Record ===")
        print("Total Burned Calories\t:", self.total_burned_calories)
        print("Total Consumed Calories\t:", self.total_consumed_calories)
