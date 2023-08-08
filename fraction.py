class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        if self.numerator%self.denominator == 0:
            return "{}".format(self.numerator/self.denominator)
        return "{}/{}".format(self.numerator, self.denominator)
    
    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = (self.denominator * other.denominator)
        result = Fraction(new_numerator, new_denominator)
        return result

num1, den1 = map(int, input().split())
num2, den2 = map(int, input().split())
frac1 = Fraction(num1, den1)
frac2 = Fraction(num2, den2)
result = frac1 + frac2
print(result)