Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Math Functions
import math

#Power, Root & Logarithmic Functions:
#math.sqrt()
math.sqrt(81)
9.0
math.sqrt(256)
16.0
math.sqrt(1024)
32.0

#math.cbrt()- Cube Root
math.cbrt(256)
6.3496042078727974
math.cbrt(8)
2.0
math.cbrt(343)
7.0

#math.pow() -  Raises a number to a power and returns a float.
math.pow(8,4)
4096.0
math.pow(9,3)
729.0
math.pow(7,3)
343.0
math.pow(3,3)
27.0

#math.exp() -  Calculates e raised to x.
math.exp(2)
7.38905609893065
math.exp(4)
54.598150033144236
math.exp(9)
8103.083927575384
math.exp(12)
162754.79141900392

#exp2() - Calculates 2 raised to x.
math.exp2(5)
32.0
math.exp2(10)
1024.0
math.exp2(45)
35184372088832.0
math.exp2(18)
262144.0

#math.expm1() -  Calculates e^x - 1 accurately for small x.
math.expm1(1)
1.718281828459045
#e = 2.71828
#((2.71828^1) - 1)

math.expm1(5)
147.4131591025766
math.expm1(8)
2979.9579870417283
math.expm1(19)
178482299.96318725

#math.log() -  Natural logarithm; optional base can be supplied.
math.log(100,10)
2.0
math.log(10)
2.302585092994046
math.log(85,5)
2.760374427722588
math.log(85)
4.442651256490317
math.log(5)
1.6094379124341003

#math.log10() -  Base-10 logarithm.
math.log10(25)
1.3979400086720377
math.log10(50)
1.6989700043360187
math.log10(1000)
3.0

#math.log2() - Base 2 logarithm.
math.log2(72)
6.169925001442312
math.log2(27)
4.754887502163468
math.log2(8)
3.0
math.log2(25)
4.643856189774724

#math.log1p() -  Calculates log(1+x) accurately for small x.
math.log1p(9)
2.302585092994046
math.log1p(25)
3.258096538021482
math.log1p(81)
4.406719247264253


#Summation, Product & Distance
#math.fsum() - Accurate floating-point sum of an iterable.
number = (10,20,30)
math.fsum(number)
60.0

Numbers = (25.4,10,35.85,25,50)
math.fsum(Numbers)
146.25

#math.prod() - Product of values in an iterable.
Numbers = (10,20,30)
>>> math.prod(Numbers)
6000
>>> 
>>> A = (7,8,9.5,10.2558)
>>> math.prod(A)
5456.0856
>>> 
>>> #math.dist() -  Euclidean distance between two points.
>>> A = (7,8)
>>> B = (5,4)
>>> math.dist(A,B)
4.47213595499958
>>> 
>>> #math.hypot() - Euclidean norm/hypotenuse; useful for right-triangle and vector length calculations.
>>> math.hypot(7,3)
7.615773105863909
>>> math.hypot(5,25)
25.495097567963924
>>> math.hypot(2,3)
3.605551275463989
>>> 
>>> #math.sumprod() -  Sum of products of corresponding elements.
>>> 
>>> A = (1,2,3,4)
>>> B = (4,5,6,7)
>>> math.sumprod(A,B)
60
