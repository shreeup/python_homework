import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f" X: {self.x}, Y: {self.y}"
    
    def eucliddist(self,other):
        dx = self.x - other.y
        dy = self.y - other.y
        # Use math.hypot for a robust calculation of the hypotenuse/distance
        return math.hypot(dx, dy)
    
class Vector(Point):
    def __init__(self,x,y):
        super().__init__(x,y)

    def __str__(self):
        return f" Y: {self.y}, X: {self.x}"
    
    def __add__(self, other):
        newx=self.x+other.x
        newy=self.y+other.y
        return Vector(newx,newy)

p1 = Point(3, 4)
p2 = Point(6, 8)
print(f"P1 created: {p1}") 
print(f"P2 created: {p2}") 
distance_p1_p2 = p1.eucliddist(p2)
print(f"Dist btn P1 and P2: {distance_p1_p2}") 

v1 = Vector(2, 5)
v2 = Vector(1, -3)

print(f"V1 created: {v1}") 
print(f"V2 created: {v2}") 
v3 = v1 + v2
print(f"V1 + V2 = V3: {v3}")