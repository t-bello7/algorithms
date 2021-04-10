
# This code is a routine to generate the 
# order n and coefficients of normalized transfer function 
# use n = [1-10] and apmax = [0.25,0.5] db
import math


#This function takes the cosine of the x
def test_func(x):
    return math.cos(x)
 
def mapper(x, min_x, max_x, min_to, max_to):
    return (x - min_x) / (max_x - min_x) * (max_to - min_to) + min_to
 
def cheb_coef(func, n, min, max):
    coef = [0.0] * n
    for i in range(n):
        f = func(mapper(math.cos(math.pi * (i + 0.5) / n), -1, 1, min, max)) * 2 / n
        for j in range(n):
            coef[j] += f * math.cos(math.pi * j * (i + 0.5) / n)
    return coef

 
 
def main():
    N = 10
    min = 0.25
    max = 0.5
    c = cheb_coef(test_func, N, min, max)
 
    print( "Coefficients:")
    for i in range(N):
        print (" The coefficients of the " + str(i) + " order is " +  str(c[i]))
 
    return None
 
main()
