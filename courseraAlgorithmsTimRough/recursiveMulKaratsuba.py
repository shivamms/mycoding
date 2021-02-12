# let x = 5678 y = 1234 a = 56 b = 78 c = 12 d = 34
# we can rewrite x = (10**n/2 * a)+b where n = number of digits = 4
# x = (10**2 * 56)+78 = 100*56+78 = 5600+78 = 5678
#sameway, y = (10**n/2 * c)+d = 1234
#then x * y = ((10**n/2 * a)+b) *  ((10**n/2 * c)+d)
# x * y = 10**n*a*c + 10**n/2+a*d+b*c + b*d --------- equation (1)
#idea: Recursively compute a*c, a*d, b*c and b*d and then compute x * y using
#equation (1). Since we do the multiplication with smaller numbers, it is simple.

def recursiveMulKaratsuba(x , y):
  