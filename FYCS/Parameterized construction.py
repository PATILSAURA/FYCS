class student:
            def  __init__(self,name,age):
                self.name=name
                self.age=age
            def show (self):
                print("student name:-",self.name)
                print("student age:-",self.age)

S1=student("Ganesh",19)
S1.show() 
