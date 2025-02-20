class student:
    def __init__(self,name):
        print("Inside Constructor")
        self.name=name
        print("Object initalized")

    def  show (self):
        print("Hello, my name is",self.name)

    def __del__(self):
         print("Insiode destructor")
         print("Object destroyed")

s1=student("Ganpat")
s1.show()
