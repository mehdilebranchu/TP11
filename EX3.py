def gcd(a, b):
    '''gcd retourne le plus grand commun diviseur (greatest common divisor)
           de 2 nombres donnés.'''
    while b:
        a, b = b, a%b
    return a
class Rational:
    def __init__(self,num,denum):
        self.__num = num
        self.__denum = denum
    def __sub__(self, other):
        b = self.__denum * other.__denum
        a = (self.__num*other.__denum)-(other.__num*self.__denum)
        ratio = Rational(a,b)
        ratio.simplification()
        return ratio
    def __rsub__(self, other):
        b = self.__denum * other.__denum
        a = (self.__num*other.__denum)-(other.__num*self.__denum)
        ratio = Rational(a,b)
        ratio.simplification()
        return ratio
    def __add__(self, other):
        b = self.__denum * other.__denum
        a = (self.__num*other.__denum)+(other.__num*self.__denum)
        r = Rational(a,b)
        r.simplification()
        return r
    def __str__(self):
        return 'num :'+str(self.__num)+' denum : '+str(self.__denum)
    def __mul__(self, other):
        a = Rational(self.__num * other.__num,self.__denum * other.__denum)
        a.simplification()
        return a
    def __truediv__(self, other):
        b = Rational(self.__num * other.__denum,self.__denum * other.__num)
        b.simplification()
        return b

    def simplification(self):
        fc=gcd(self.__num,self.__denum)
        self.__num /= fc
        self.__denum /= fc
        return self.__num,self.__denum


if __name__ == "__main__":
    r1 = Rational(1,2)
    r2 = Rational(1,3)
    r3 = r1 - r2
    r4 = r3 * r2
    r5 = r4 / r2
    print(r5)
