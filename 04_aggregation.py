class Student:
    def __init__(self, name):
        self.name = name

class Club:
    def __init__(self, name):
        self.name = name
        self.members = []                # Students are created outside

    def add_member(self, student):
        self.members.append(student)

# --- Running the Code ---
ana = Student("Ana")
club = Club("Science Club")
club.add_member(ana)
del club                                 # club is gone...
print(ana.name, "still exists")          # ...but Ana remains

# Sample Output:
# Ana still exists