# %% [markdown]
# # **Lab 2 - Introduction to Python programming II**

# %% [markdown]
# Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.

# %%
# Do not edit this cell.

LabID="Lab2"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

# %% [markdown]
# **Enter your name, section number, and BYU NetID**

# %%
# Enter your first and last names in between the quotation marks.

first_name="Monte"

last_name="Gardiner"

# Enter your Math 215 section number in between the quotation marks.

section_number="001"

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="mbgardin"

# %% [markdown]
# **Problem 1**

# %%
first_elem = 1   # The for loop rebinds i but does not mutate my_list, so my_list stays [1,2,3,4] and first_elem is its first element.

# %% [markdown]
# **Problem 2**

# %%
def sum_list(L):
  total = 0
  for x in L:
    total = total + x
  return total

# %% [markdown]
# **Problem 3**

# %%
def list_relu(L):
  new_list=L.copy()  # Remember to create a copy of your list.  After this lab you'll need to remember to do it on your own.
  for i in range(len(new_list)):
    if new_list[i] < 0:
      new_list[i] = 0
  return new_list

# %% [markdown]
# **Problem 4**

# %%
import numpy as np  # Importing NumPy

# %%
my_var = (np.exp(5) - np.log(np.sqrt(5))) / np.exp(np.cos(3))

# %% [markdown]
# **Problem 5**

# %%
v = np.array([1, 3, -2, 4, 5])
u = np.array([1, 1, -2, 1, 1])
w = np.array([1, 0, 1, 0, 1])
my_vect_var = (np.dot(v, u) / np.dot(u, u)) * u + (np.dot(v, w) / np.dot(w, w)) * w

# %% [markdown]
# **Problem 6**

# %%
def first_rpt(M):
  new_matrix=M.copy()  # Remember to create a copy of your matrix.  After this lab you'll need to remember to do it on your own.
  for i in range(len(new_matrix)):
    new_matrix[i] = new_matrix[0]
  return new_matrix

# %% [markdown]
# **Problem 7**

# %%
def matrix_sum(M):
  total = 0
  for i in range(len(M)):
    for j in range(len(M[i])):
      total = total + M[i][j]
  return total

# %% [markdown]
# **Problem 8**

# %%
long_list = [0.5**i for i in range(1, 101)]

# %% [markdown]
# **Problem 9**

# %%
very_long_list = [base**exp for exp in range(1, 100) for base in range(1, 4)]

# %% [markdown]
# **STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.  

# %% [markdown]
# **You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

# %% [markdown]
# To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to [gradescope.com](https://gradescope.com) for grading.


