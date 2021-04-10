
# ok welcome back to coding tomi

# This code is a routine to generate the 
# order n and coefficients of normalized transfer function 
# use n = [1-10] and apmax = [0.25,0.5] db
import re
import sys
import math
import os
import random
import numpy

print(numpy.polynomial.chebyshev.Chebyshev(2))
# if __name__ == '__main__':
#     def studentinfo():
#         name = input("write your name here:")

#     def cheb_coef(func, n, min, max):
#     coef = [0.0] * n
#     for i in range(n):
#         f = func(mapper(math.cos(math.pi * (i + 0.5) / n), -1, 1, min, max)) * 2 / n
#         for j in range(n):
#             coef[j] += f * math.cos(math.pi * j * (i + 0.5) / n)
#     return coef
 
# def cheb_approx(x, n, min, max, coef):
#     a = 1
#     b = mapper(x, min, max, -1, 1)
#     c = float('nan')
#     res = coef[0] / 2 + coef[1] * b
 
#     x = 2 * b
#     i = 2
#     while i < n:
#         c = x * b - a
#         res = res + coef[i] * c
#         (a, b) = (b, c)
#         i += 1
 
#     return res
 
# def main():
#     N = 10
#     min = 0
#     max = 1
#     c = cheb_coef(test_func, N, min, max)
 
#     print( "Coefficients:")
#     for i in range(N):
#         print (" % lg" % c[i])
 
#     print ("\n\nApproximation:\n    x      func(x)       approx      diff")
#     for i in range(20):
#         x = mapper(i, 0.0, 20.0, min, max)
#         f = test_func(x)
#         approx = cheb_approx(x, N, min, max, c)
#         print( "%1.3f %10.10f %10.10f % 4.2e" % (x, f, approx, approx - f))
 
#     return None


#     studentinfo()