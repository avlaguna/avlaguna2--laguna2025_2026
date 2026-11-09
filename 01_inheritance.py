class SchoolActivity:
    def __init__(self, title):
        self.title = title

    def display_details(self):
        print("Activity:", self.title)

class ScienceFair(SchoolActivity):      # child inherits from parent
    def conduct_activity(self):
        print("Conducting science experiments.")

# --- Running the Code ---
fair = ScienceFair("Science Fair")
fair.display_details()
fair.conduct_activity()

# Sample Output:
# Activity: Science Fair
# Conducting science experiments.