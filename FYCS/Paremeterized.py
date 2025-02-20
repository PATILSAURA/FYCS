class student:
    def __init__(self,name,add,id,age):
        self.name = name
        self.add =  add
        self.id =  id
        self.age = age
    def show (self):
            print("student Name:",self.name)
            print("student Address:",self.add)
            print("student ID:",self.id)
            print("student age:",self.age)

s1=student("Ajay","Umbergaon",101,20)
s1.show()
