class Complex:
    def __init__(self,pR,pI):
        self.__pI = pI
        self.__pR = pR

    def __add__(self, other):
        return Complex(self.__pR+other.__pR, self.__pI+other.__pI)
    def __sub__(self, other):
        return Complex(self.__pR-other.__pR, self.__pI-other.__pI)
    def __mul__(self, other):
        return Complex(self.__pR*other.__pR, self.__pI*other.__pI)
    def __truediv__(self, other):
        return Complex(self.__pR/other.__pR, self.__pI/other.__pI)
    def __abs__(self):
        return Complex(abs(self.__pR), abs(self.__pI))
    def __eq__(self, other):
        return self.__pR == other.__pR and self.__pI == other.__pI
    def __ne__(self, other):
        return self.__pR != other.__pR and self.__pI != other.__pI
    def __str__(self):
        return 'partie Re :'+str(self.__pR)+' partie Im : '+str(self.__pI)
if __name__ == '__main__':
    c1 = Complex(1,2)
    c2 = Complex(3,4)
    c3 = c1+c2
    c4 = c3 - c1
    c5 = c1*c2
    c6 = c1 / c2
    c7 = abs(c2)
    c8 = c2 == c4
    c9 = c6 != c5
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    print(c5)
    print(c6)
    print(c7)
    print(c8)
    print(c9)
