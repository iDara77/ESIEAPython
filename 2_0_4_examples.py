class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def get_name(self):
        return self.name

p1 = Person("Alice")
print(p1.name)
print(p1.get_name())

class Student(Person):
    def __init__(self, name, semester) -> None:
        super().__init__(name)
        self.semester = semester

e1 = Student("Bob", "S2")
print(e1.semester)
print(e1.name)

class Teacher(Person):
    def __init__(self, name, course) -> None:
        super().__init__(name)
        self.course = course


t1 = Teacher("Bob", "Python")
print(t1.course)
print(t1.name)

print(f"t1 has attribute name: {hasattr(t1, 'name')}")
print(f"t1 has attribute course: {hasattr(t1, 'course')}")
print(f"t1 has attribute semester: {hasattr(t1, 'semester')}")

class Bucket():
    volume=5 # Tous les object de type bucket auront volume = 5
    
    def __init__(self, id, holds) -> None:
        self.holds = holds
        self.id = id
    
    @classmethod
    def printVolume(cls):
        print("Volume: %d" % cls.volume)
    
    def printHolds(self):
        print("B%d Holds: %d" % (self.id,self.holds))

b1 = Bucket(1,3)
b2 = Bucket(2,4)
b1.printVolume()
b1.printHolds()
b2.printVolume()
b2.printHolds()
print("After b1.holds = 5")
b1.holds = 5
b1.printHolds()
b2.printHolds()
b1.volume = 10
print("After b1.volume = 10")
b1.printVolume()
b2.printVolume()
print("After Bucket.volume = 10")
Bucket.volume = 10
b1.printVolume()
b2.printVolume()