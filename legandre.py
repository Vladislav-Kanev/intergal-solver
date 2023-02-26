import numpy as np
from numpy.polynomial.legendre import leggauss

n = 3 # degree of Legendre polynomial
quad_points, quad_weights = leggauss(n)

print(f'qp = {", ".join([str(a) for a in quad_points.tolist()])}')
print(f'qw = {", ".join([str(a) for a in quad_weights.tolist()])}')
