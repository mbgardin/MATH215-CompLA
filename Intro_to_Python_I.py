# %% [markdown]
# # **Lab 1 - Introduction to Python programming I**

# %% [markdown]
# Enter your code in the spaces provided.  Do not change any of the variable names or function names that are already provided for you.  In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.

# %%
# Do not edit this cell.

LabID="Lab1"

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
my_first_var = ((3 + 5) * 2 - 4) / 3   # Replace with the required expression from Problem 1.

# %% [markdown]
# **Problem 2**

# %%
def arithmetic2(i):
  return ((i + 2) * 3) - 5

# %% [markdown]
# **Problem 3**

# %%
def triple(y):
  return 3 * y

# %%
def avg(x,y):
  return (x + y) / 2

# %%
def combine(x,y):
  # Calls both triple(y) and avg(x,y) as required.
  t = triple(y)
  a = avg(x, y)
  return t + a

# %% [markdown]
# **Problem 4**

# %%
def first(c):
  # Returns the first element of the list c.
  return c[0]

# %%
def first_last(c):
  # Returns the first and last elements of the list c.
  return c[0], c[-1]

# %%
def middle(c):
  # Returns all elements of c except the first and last.
  return c[1:-1]

# %% [markdown]
# **Problem 5**

# %%
def swap(c):
  new_list=c.copy() # This creates a copy of the list c, which is called new_list.  Your function should work with this list instead of the list c which is passed to the function.
  # Swap the first and last elements of new_list.
  new_list[0], new_list[-1] = new_list[-1], new_list[0]
  return new_list

# %% [markdown]
# **Problem 6**

# %%
def absolute_value(x):
  # Return the absolute value of x without using the built-in abs().
  if x < 0:
    return -x
  else:
    return x

# %% [markdown]
# **Problem 7**

# %%
def indicator(lower,upper,n):
  # Returns 1 if n is in the closed interval [lower, upper], 0 otherwise.
  if lower <= n <= upper:
    return 1
  else:
    return 0

# %% [markdown]
# **Problem 8**

# %%
def trunc_max(x,y):
  # Returns x if x <= y, otherwise returns y (truncates x at a maximum of y).
  if x <= y:
    return x
  else:
    return y

# %% [markdown]
# **STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.  

# %% [markdown]
# **You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

# %% [markdown]
# To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to [gradescope.com](https://gradescope.com) for grading.


