"""
Name: ThankGod Ofurum
Class CS1
Project: Create a class consisting of methods
for dealing with fractions both addition,
subtraction, multiplication and division

"""

"""Output greatest common divisor of fractions"""
def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        #assigning GCD as n
        m = oldn
        n = oldm % oldn
    return n
    
class Fraction:
    """class constructor consisting of Instant variable"""
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    """Display fraction on screen"""
    def show(self):
        print(self.num, "/", self.den)

    """Display fractions in print statement"""
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    """Allow addition of object instances"""
    def __add__(self, other):
        newnum = (self.num * other.den) + (self.den * other.num)
        newden = self.den * other.den
        return Fraction(newnum, newden)

    """Allow subtraction of object instances"""
    def __sub__(self, other):
        newnum = (self.num * other.den) - (self.den * other.num)
        newden = self.den * other.den
        return Fraction(newnum, newden)

    """Allow multiplication of object instances"""
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    """Allow division of object instances"""
    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = other.num * self.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    """Allow negation of object instances"""
    def __neg__(self):
        return Fraction(-self.num, self.den)

    """Allow comparison of object instances"""
    def __le__(self, other):
        #implement code

    """Allow comparison of object instances"""
    def __lt__(self, other):
        #implement code
        firstnum = self.num * other.den
        secnum = other.num * self.den
        if first

    """Allow comparison of object instacnes"""
    def __ge__(self, other):
        #implement code

    """Allow comparison of object instances"""
    def __gt__(self, other):
        #implement code

    """Override python default equality"""
    def __eq__(self, other):
        firstnum = self.num * other.den
        secnum = other.num * self.den
        return firstnum == secnum
    
    

    
    
