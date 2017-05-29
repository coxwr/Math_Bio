import scipy 
import numpy as np
import matplotlib.pyplot as plt

#file to create a multiple linear regression

x = np.array([[58.5,50,59,5,58,60.5,57.5,49.3,53.6,58.3,51,54.2,54,59.5,57.5,56.25],[220,250,165,270,200,250,210,130,220,165,190,165,280,190,200],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]) #independent variables
y = np.array([19.5,18.0,22,19,21,22,29.5,18,20,20,25,17,26.5,23,29]) #dependent variable

m_t =np.array([[58.5,220,1],[50,150,1],[59.5,165,1].[58,270,1],[60.5,200,1],[57.5,250,1],[49.3,210,1],[53.6,130,1],[58.3,220,1],[51,165,1],[54.2,190,1],[54,165,1],[59.5,280,1],[67.5,190,1],[56.25,200,1]])

m = x
#m_t = np.transpose(x)

coef = np.dot(np.dot(np.linalg.inv(np.dot(m_t,m),m_t),y))  #calculates coefficients of hyper-plane of best fit

print(coef)
