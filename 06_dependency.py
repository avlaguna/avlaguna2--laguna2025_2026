class Activity:
    def __init__(self, title):
        self.title = title

class ReportPrinter:
    def print_report(self, activity):    # only uses Activity as a parameter
        print("Report for:", activity.title)

# --- Running the Code ---
ReportPrinter().print_report(Activity("Science Fair"))

# Sample Output:
# Report for: Science Fair