
from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig

def computePCA():
  # taking number of rows and column
  n, m = map(int, input("Enter rows and column with a space ").split()) 
  #defining the matrix and taking input.
  A = array([input("Enter elements row by row separated by a space ").strip().split() for _ in range(n)], int)
  print(A)
  # calculate the mean of each column
  M = mean(A, axis=0)
  # center columns by subtracting column means
  C = A - M
  # calculate covariance matrix of centered matrix
  V = cov(C.T)
  # eigendecomposition of covariance matrix
  values, vectors = eig(V)
  projection_matrix = (vectors.T[:][:2]).T
  # project data
  P = projection_matrix.T.dot(C.T)
  print(P.T)

computePCA()