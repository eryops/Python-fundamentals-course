class Printer:
    def display_status(self):
        print("Printer: Ready to print documents.")

class Screen:
    def display_status(self):
        print("Screen: Displaying high resolution graphics.")


# Create objects
printer = Printer()
screen = Screen()

# Store them in the same list
devices = [printer, screen]

# Loop and call display_status()
for device in devices:
    device.display_status()

# This works because Python uses duck typing:
# As long as an object has the method being called (display_status),
# Python does not care about the object's class or inheritance.
# "If it walks like a duck and quacks like a duck, it's a duck."
