#4
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in uppercase:", self.input_string.upper())

def test_methods():
    manipulator = StringManipulator()
    manipulator.getString()
    manipulator.printString()

test_methods()