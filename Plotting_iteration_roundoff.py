# %% [markdown]
# # **Lab 3 - Plotting, iteration, and roundoff error**

# %% [markdown]
# Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.

# %%
# Do not edit this cell.

LabID="Lab3"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

# %% [markdown]
# **Enter your BYU NetID**

# %%
# Enter your first and last names in between the quotation marks.

first_name="Monte"

last_name="Gardiner"

# Enter your Math 215 section number in between the quotation marks.

section_number="001"

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="mbgardin"

# %% [markdown]
# **Import NumPy and PyPlot**

# %%
import numpy as np
from matplotlib import pyplot as plt

# %% [markdown]
# **Problem 1**

# %%
# Plot both functions from Problem 1 here.  Put all of your code to create the plot inside the function below.

def create_plots():
  x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
  plt.plot(x, np.sin(x))
  plt.plot(x, np.cos(4 * x))
  plt.show()
  return None

# %% [markdown]
# **Problem 2**

# %%
# Create the scatter plot from Problem 2 here.  Put all of your code to create the plot inside the function below.

def create_scatter_plot():
  x = np.random.normal(scale=1.5, size=500)
  y = np.random.normal(scale=1, size=500)
  plt.plot(x, y, 'x', markersize=5, alpha=1.0)
  plt.show()
  return None

# %% [markdown]
# **Problem 3**

# %%
def fact(n):
  if n==0:
    return 1
  else:
    return n * fact(n-1)

# %% [markdown]
# **Problem 4**

# %%
root = 1.79128784747792 # Replace the value -1 with your approximation to the root of f(x), correct to 12 decimal places.

# %% [markdown]
# **Problem 5**

# %%
def g(x):
  return x**4 - 2*x**3 - 17*x**2 + 4*x + 30

def g_prime(x):
  return 4*x**3 - 6*x**2 - 34*x + 4

# %% [markdown]
# **Problem 6**

# %%
def newtons_method(starting_guess,n):
  x_j = starting_guess
  for i in range(n):
    x_j = x_j - g(x_j) / g_prime(x_j)
  return x_j

# %% [markdown]
# **Problem 7**

# %%
def integration(m):
  E = 1 - 1 / np.exp(1)
  for j in range(1, m + 1):
    E = 1 - j * E
  return E

# %% [markdown]
# **STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.   

# %% [markdown]
# **You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

# %% [markdown]
# To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to [gradescope.com](https://gradescope.com) for grading.
