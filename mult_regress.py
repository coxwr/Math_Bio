import scipy 
import numpy as np


#file to create a multiple linear regression

x = np.array() #independent variables
y = np.array() #dependent variable

m = x
m_t = np.transpose(x)

coef = np.dot(np.dot(np.linalg.inv(np.dot(m_t * )m) * m_t) * y)  #calculates coefficients of hyper-plane of best fit
