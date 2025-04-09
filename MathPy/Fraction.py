class Fraction:
    def __init__(self, num, denom):
        assert type(denom) == int and type(num) == int, "not an int"
        self.num = num
        self.denom = denom
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top,bott)
    def __sub__(self, other):
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top,bott)
    def __float__(self):
        return self.num/self.denom
    def inverse(self):
        return Fraction(self.denom, self.num)

a = Fraction(1, 4)
b = Fraction(3, 4)
c = a+b
print(f"{c} \n{float(c)} \n{Fraction.__float__(c)}\n{float(b.inverse())}")