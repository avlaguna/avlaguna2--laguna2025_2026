class Schedulable:                       # interface
    def set_schedule(self):
        raise NotImplementedError

class ScienceFair(Schedulable):          # realizes the interface
    def set_schedule(self):
        print("Science Fair schedule set.")

# --- Running the Code ---
ScienceFair().set_schedule()

# Sample Output:
# Science Fair schedule set.