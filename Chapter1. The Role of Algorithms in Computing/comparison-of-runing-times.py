#No leap year solution
from decimal import Decimal
from math import log, floor, factorial;

timeArray = [{"value" : 10 ** 6, "name" : "1 second"},
             {"value" : 60 * 10 ** 6, "name" : "1 minute"},
             {"value":60 * 60 * 10 ** 6, "name" : "1 hour"},
             {"value":24 * 60 * 60 * 10 ** 6, "name" : "1 day"},
             {"value":30 * 24 * 60 * 60 * 10 ** 6, "name" : "1 month"},
             {"value":365 * 24 * 60 * 60 * 10 ** 6, "name" : "1 year"},
             {"value":100 * 365 * 24 * 60 * 60 * 10 ** 6, "name" : "1 century"}]

def lgN(n):
    lower = 0.0
    upper = 10e500
    while True:
        middle = (lower+upper)/2
        if lower == middle or middle == upper:
            return middle
        if log(middle, 2) > n:
            upper = middle
        else:
            lower = middle
def sqrt(n): return n**2;
def n(n): return n;
def nLgn(n):
    lower = 0.0
    upper = 10e10
    while True:
        middle = (lower+upper)/2
        if lower == middle or middle == upper:
            return middle
        if middle*log(middle, 2) > n:
            upper = middle
        else:
            lower = middle
def sqrn(n): return floor(n**(1.0/2.0));
def pow3(n): return floor(n**(1.0/3.0));
def twoPown(n): return floor(log(n, 2));
def factn(n):
    i = 0
    while True:
        if factorial(i) > n:
           return i-1;
        i = i + 1;

print("             lg(n) sqrt(n)      n       nLg(n)   n^2      n^3     2^n      factn");
for element in timeArray:
    print("{}   {:.2e}  {:.2e}   {:.2e}  {:.2e}  {:.2e}  {:.2e}  {:.2e}  {:.2e}"
          .format(
                  element["name"],
                  Decimal(lgN(element["value"])),
                  Decimal(sqrt(element["value"])),
                  Decimal(n(element["value"])),
                  Decimal(nLgn(element["value"])),
                  Decimal(sqrn(element["value"])),
                  Decimal(pow3(element["value"])),
                  Decimal(twoPown(element["value"])),
                  Decimal(factn(element["value"]))
                  ));

