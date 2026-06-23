#!/usr/bin/env python
# coding: utf-8

# #**Lab 6 - Least squares I**

# Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.

# In[1]:


# Do not edit this cell.

LabID="Lab6"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True


# **Enter your name, section number, and BYU NetID**

# In[ ]:


# Enter your first and last names in between the quotation marks.

first_name="Monte"

last_name="Gardiner"

# Enter your Math 215 section number in between the quotation marks.

section_number="001"

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="mbgardin"


# **Import NumPy**

# In[3]:


import numpy as np


# **Problem 1**

# In[4]:


# Replace the values of 0 with the NumPy arrays from Problem 1.

X1=np.array([[1, 5], [1, 10], [1, 15], [1, 20], [1, 25], [1, 30], [1, 35], [1, 40], [1, 45], [1, 50]])

Y1=np.array([3.33, 4.43, 4.39, 5.23, 5.67, 6.06, 7.01, 7.16, 8.03, 8.78])


# **Problem 2**

# In[5]:


# Replace the values of 0 with the normal equation coefficient matrix and normal equation right-hand side respectively from Problem 2.

normal_coef1=X1.T @ X1

normal_vect1=X1.T @ Y1


# **Problem 3**

# In[6]:


# Replace the value of 0 with the least squares solution beta1 you found in Problem 3.

beta1=np.linalg.solve(normal_coef1, normal_vect1)


# In[7]:


# Define a function whose graph is the line of best fit.

def ls1_line(x):
  return beta1[0] + beta1[1] * x


# In[8]:


import matplotlib.pyplot as plt

# Construct your plot of ls1_line and the corresponding data points here. Put all of your code to create the plots inside the function below.

def create_plots1():
  plt.scatter(X1[:, 1], Y1)
  x_vals = np.linspace(0, 35, 100)
  plt.plot(x_vals, ls1_line(x_vals))
  plt.show()
  return None


# In[9]:


# Replace the value of 0 with your prediction of the satellite's velocity at t=60.

pred1=ls1_line(60)


# **Problem 4**

# In[10]:


# Replace the values of 0 with the NumPy arrays from Problem 4.

t = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
X2=np.column_stack((t, t**2))

Y2=np.array([20.57, 87.48, 197.45, 347.67, 546.12, 784.35, 1066.02, 1390.97, 1761.85, 2177.34])


# **Problem 5**

# In[11]:


# Replace the values of 0 with the normal equation coefficient matrix and normal equation right-hand side, and least squares solution from Problem 5.

normal_coef2=X2.T @ X2

normal_vect2=X2.T @ Y2

beta2=np.linalg.solve(normal_coef2, normal_vect2)


# **Problem 6**

# In[12]:


# Define a function whose graph is the parabola of best fit.

def ls2_par(x):
  return beta2[0] * x + beta2[1] * (x ** 2)


# In[13]:


# Construct your plot of ls2_par and the corresponding data points here. Put all of your code to create the plots inside the function below.

def create_plots2():
  plt.scatter(X2[:, 1], Y2)
  x_vals = np.linspace(0, 25, 100)
  plt.plot(x_vals, ls2_par(x_vals))
  plt.show()
  return None


# In[14]:


# Replace the value of 0 with your prediction of the satellite's position at t=60.

pred2=ls2_par(60)


# **Problem 7**

# In[15]:


# Replace the values of 0 with the NumPy arrays from Problem 7.

T3 = np.array([87.77, 224.70, 365.25, 686.95, 4332.62, 10759.2])
r3 = np.array([0.389, 0.724, 1.0, 1.524, 5.2, 9.510])

Y3=np.log(r3)

X3=np.column_stack((np.ones(6), np.log(T3)))


# In[16]:


# Replace the values of 0 with the normal equation coefficient matrix and normal equation right-hand side from Problem 7.

normal_coef3=X3.T @ X3

normal_vect3=X3.T @ Y3


# In[17]:


# Replace the value of 0 with the least squares solution from Problem 7.

beta3=np.linalg.solve(normal_coef3, normal_vect3)


# **Problem 8**

# In[18]:


# Replace the values of 0 with your predictions for the semi-major axes of Uranus and Neptune.

pred_Uran=np.exp(beta3[0] + beta3[1] * np.log(30687.15))

pred_Nept=np.exp(beta3[0] + beta3[1] * np.log(60190.03))


# **STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.   

# **You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

# To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to [gradescope.com](https://gradescope.com) for grading.
