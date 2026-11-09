class Teacher:
    def __init__(self, name):
        self.name = name

class Activity:
    def __init__(self, title, adviser):
        self.title = title
        self.adviser = adviser           # Activity knows a Teacher

# --- Running the Code ---
mr_cruz = Teacher("Mr. Cruz")
fair = Activity("Science Fair", mr_cruz)
print(fair.title, "is advised by", fair.adviser.name)

# Sample Output:
# Science Fair is advised by Mr. Cruz