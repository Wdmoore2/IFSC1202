import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))

    def angles(self):
        angle1 = math.degrees(math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3)))
        angle2 = math.degrees(math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3)))
        angle3 = math.degrees(math.acos((self.s1**2 + self.s2**2 - self.s3**2) / (2 * self.s1 * self.s2)))
        return angle1, angle2, angle3

Triangle_list = []
with open('examthreetriangles.txt', 'r') as file:
    for line in file:
        sides = line.strip().split(',')
        triangle = Triangle(sides[0], sides[1], sides[2])
        Triangle_list.append(triangle)

print(f"{'Type':<12}{'Side 1':<12}{'Side 2':<12}{'Side 3':<12}{'Perimeter':<12}{'Area':<12}{'Angle 1':<10}{'Angle 2':<10}{'Angle 3':<10}")
for triangle in Triangle_list:
    angles = triangle.angles()
    print(f"{triangle.type():<12}{triangle.s1:<12.3f}{triangle.s2:<12.3f}{triangle.s3:<12.3f}{triangle.perimeter():<12.3f}{triangle.area():<12.3f}{angles[0]:<10.3f}{angles[1]:<10.3f}{angles[2]:<10.3f}")