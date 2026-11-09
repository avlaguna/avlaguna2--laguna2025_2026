class Schedule:
    def __init__(self, date):
        self.date = date

class Activity:
    def __init__(self, title, date):
        self.title = title
        self.schedule = Schedule(date)   # created INSIDE, owned by Activity

# --- Running the Code ---
fair = Activity("Science Fair", "Nov 20")
print(fair.title, "on", fair.schedule.date)
del fair                                 # the Schedule is destroyed with it

# Sample Output:
# Science Fair on Nov 20