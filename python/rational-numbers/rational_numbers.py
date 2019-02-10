from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = ((self.numer * other.denom) + (other.numer * self.denom))
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = ((self.numer * other.denom) - (other.numer * self.denom))
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = ((self.numer * other.numer))
        denom = (self.denom * other.denum)
        return Rational(numer, denom)

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass