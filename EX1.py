class Cercle:
    def __init__(self,r):
        self.__r = r
    def getR(self):
        return self.__r
    def __add__(self, other):
        return self.__r + other.__r

