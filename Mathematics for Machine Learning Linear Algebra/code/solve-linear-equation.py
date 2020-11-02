# Equation:

'''
4x + 3y + 2z = 25
-2x + 2y + 3z = -10
3x -5y + 2z = -4
'''

# import module
import numpy as np

A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = np.array([25, -10, -4])
X = np.linalg.inv(A).dot(B)

print(X)


'''
In the script above the linalg.inv() and the linalg.dot() methods are chained together. The variable X contains the solution for Equation 2, and is printed as follows:

[ 5.  3. -2.]
'''

# Using solve()
'''
linalg.solve() method, which can be used to directly find the solution of a system of linear equations.
'''

X = np.linalg.solve(A, B)

print(X)