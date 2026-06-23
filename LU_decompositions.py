# %% [markdown]
# # **Lab 5 - LU decompositions and Gaussian elimination**

# %% [markdown]
# Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.

# %%
# Do not edit this cell.

LabID="Lab5"

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
# **Import NumPy**

# %%
import numpy as np

# %% [markdown]
# **Problem 1**

# %%
def augment(A,b):
  return np.column_stack((A, b))

# %% [markdown]
# **Problem 2**

# %%
def first_column_zeros(A):
  B=np.copy(A)
  B=B.astype(float)
  for i in range(1, len(B)):
    factor = B[i, 0] / B[0, 0]
    B[i] = B[i] - factor * B[0]
  return B

# %% [markdown]
# **Problem 3**

# %%
def row_echelon(A,b):
  M = augment(A, b).astype(float)
  n = len(A)
  for j in range(n):
    for i in range(j + 1, n):
      factor = M[i, j] / M[j, j]
      M[i] = M[i] - factor * M[j]
  return M

# %% [markdown]
# **Problem 4**

# %%
def LU_decomposition(A):
  U=np.copy(A).astype(float)
  L=np.identity(len(A))
  n = len(A)
  for j in range(n):
    for i in range(j + 1, n):
      factor = U[i, j] / U[j, j]
      L[i, j] = factor
      U[i] = U[i] - factor * U[j]
  return L,U # We've included the return values for you, though your function needs to define them correctly.

# %% [markdown]
# **Problem 5**

# %%
def forward_substitution(L,b): # Accepts a lower triangular square matrix L and a vector b, solves Ly=b for y.
  n = len(L)
  y = np.zeros(n)
  for i in range(n):
    sum_val = sum(L[i, j] * y[j] for j in range(i))
    y[i] = (b[i] - sum_val) / L[i, i]
  return y

# %% [markdown]
# **Problem 6**

# %%
def back_substitution(U,y):    # Accepts an upper triangular square matrix U and a vector b, solves Ux=b for x.
  n = len(U)
  x = np.zeros(n)
  for i in range(n - 1, -1, -1):
    sum_val = sum(U[i, j] * x[j] for j in range(i + 1, n))
    x[i] = (y[i] - sum_val) / U[i, i]
  return x

# %% [markdown]
# **Problem 7**

# %%
def LU_solver(A,b):
  L, U = LU_decomposition(A)
  y = forward_substitution(L, b)
  return back_substitution(U, y)

# %% [markdown]
# **STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.   

# %% [markdown]
# **You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

# %% [markdown]
# To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to [gradescope.com](https://gradescope.com) for grading.
