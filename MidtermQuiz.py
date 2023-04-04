class DistanceConversion:
    def __init__(self,distance):
     self.__distance = distance

    def centimeter(self):
     return self.__distance*100
    def kilometer(self):
     return self.__distance/1000
    def inches(self):
     return self.__distance*39.37

    def display(self):
        print("Centimeter:", round(self.centimeter(),2))
        print("Kilometer:", round(self.kilometer(),2))
        print("Inches:", round(self.inches(),2))
newdc = DistanceConversion(float(input("Enter distance:")))
newdc.display()
