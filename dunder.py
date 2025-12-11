
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        
        return f"Name : {self.name} - Age : {self.age} "

class Vector:
    def __init__(self, x, y) -> None:
        
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    
v1 = Vector(10,20)
v2 = Vector(50,60)
v3 = v1 + v2

print(v3)