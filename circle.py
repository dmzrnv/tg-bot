import math
forlength = (2 * math.pi)
class circle():
  @staticmethod 
  def lengthFromRadius(radius):
    return radius * forlength
  @staticmethod
  def areaFromRadius(radius):
      return radius * radius * math.pi
  def __init__(self, x,y, radius):
    self.x = x
    self.y = y
    self.radius = radius
  def length(self):
    return self.radius * forlength
  def area(self):
    return self.radius * self.radius * math.pi
  def do_intersect(self, circle):
    x_distance = self.x - circle.x
    y_distance = self.y - circle.y
    r1 = self.radius
    r2 = circle.radius
    return (r2-r1)**2 <= (x_distance**2 + y_distance**2) <= (r2+r1)**2
  def __eq__(self, circle):
    return self.y == circle.y and self.x == circle.x and self.radius==circle.radius
  def __str__(self):
    return f'Окружность с радуисом {self.radius} и центром в точке {self.x}:{self.y}'


