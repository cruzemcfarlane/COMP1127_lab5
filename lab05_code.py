

class Polygon:
    def __init__(self,nbrsides):
        self.nbr_sides = nbrsides

    def whoamI(self):
        if self.nbr_sides == 3:
            return "Triangle"
        elif self.nbr_sides == 4:
            return "Rectangle"
        else: return "Polygon"

    def howmanysides(self):
        return self.nbr_sides

    def area(self):
        return "No Area"

    def perimeter(self):
        return "No Perimeter"
