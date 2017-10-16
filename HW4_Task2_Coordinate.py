from math import sqrt, atan
class Coordinate_System:
    def __init__(self, x, y, *args):
        self.coord = [x,y, list(args)]

    def distance_to_start(self):
        return sqrt((self.coord[0] - 0)**2 + (self.coord[1] - 0)**2)

    def distance_between_dots(self, p):
        return sqrt((self.coord[0] - p.coord[0])**2 + (self.coord[1] - p.coord[1])**2)

#Moving to another coordinate system, kind_cs:  1 = polar system; 2 = cylindrical system
    def change_coord_system(self, kind_cs):
        res = {}
        if kind_cs == 1 and len(self.coord) == 2:
            res.setdefault('radius', sqrt(self.coord[0]**2 + self.coord[1]**2))
            res.setdefault('angle', atan(self.coord[1]/self.coord[0]))
        elif kind_cs == 2 and len(self.coord) == 3:
            res.setdefault('radius', sqrt(self.coord[0]**2 + self.coord[1]**2))
            res.setdefault('angle', atan(self.coord[1]/self.coord[0]))
            res.setdefault('z', int(self.coord[2][0]))
        else:
            return 'Type a correct kind of coordinated system'
        return res

if __name__ == "__main__":
    obj1 = Coordinate_System(1,2,3)
    #obj2 = Coordinate_System(6,7)
    #print(obj1.distance_to_start())
    #print(obj1.distance_between_dots(obj2))
    print(obj1.change_coord_system(6))
    print(obj1.coord)