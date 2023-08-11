class Person():
    def get_name(self):
        name = input("Name: ")
        return name
    
    def get_age(self):
        age = int(input("Age: "))
        return age
    
class Student(Person):
    def get_roll(self):
        roll_no = int(input("Roll no:"))
        return roll_no
    
class Teacher(Person):
    def get_id(self):
        id_no = int(input("ID no:"))
        return id_no
    
john = Student()
print(john.get_name())
harry = Teacher()
print(harry.get_age())