class Point2D():

    def __init__(self, x,y):
        self.coord = [x,y]

    def distance(self):
        return (self.coord[0]**2 + self.coord[1]**2)**0.5

    def __str__(self):
        return f'Point: ({self.coord[0]}, {self.coord[1]})'

    def __getitem__(self, item):
        return self.coord[item]

    def __eq__(self, other):
        return (self.coord[0] == other.coord[0])&(self.coord[1] == other.coord[1])

    def __add__(self, other):
        return Point2D(self.coord[0] + other.coord[0], self.coord[1] + other.coord[1])

    def __le__(self, other):
        return (self.distance() <= other.distance())


    def __ge__(self, other):
        return (self.distance() >= other.distance())

    def __gt__(self, other):
        return (self.distance() > other.distance())

if __name__ =='__main__':
    point1 = Point2D(4,1)
    point2 = Point2D(4,1)
    print(point1==point2)
    print(point1+point2)
    print(point1<=point2)
    print(point1>=point2)
    print(point1>point2)
    for i in point1:
        print(i)