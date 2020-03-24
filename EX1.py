class Cercle:
    def __init__(self,r):
        self.__r = r
    def getR(self):
        return self.__r
    def __add__(self, other):
        return Cercle(self.__r + other.__r)
    def __lt__(self,other):
        return self.__r < other.__r
    def __gt__(self, other):
        return self.__r > other.__r
    def __str__(self):
        return str(self.__r)
if __name__ == '__main__':
    c = Cercle(2)
    c2 = Cercle(3)
    c3 = c + c2
    c4 = c < c2
    c5 =  c > c3
    print(c3)
    print(c4)
    print(c5)
