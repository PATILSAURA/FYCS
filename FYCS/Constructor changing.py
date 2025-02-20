class collage:
    def __init__(self,name):
        print("In class collage")
        self.name=name

class dept(collage):
    def __init__(self,name,dname):
        print("In class Department")
        super(). __init__(name)
        self.dname=dname

class cs(dept):
    def __init__(self,name,dname,cname):
        print("Class Dept FYCS")
        super().__init__(name,dname)
        self.cname=cname

obj=cs("NBMS","Computer science","FYCS")
