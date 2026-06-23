# %% [markdown]
# #**Lab 10 - Networks and eigenvector centrality**

# %% [markdown]
# Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.

# %%
# Do not edit this cell.

LabID="Lab10"

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
# **Import and visualize the data**

# %% [markdown]
# The simplest way to load the data into Colab is to first download it as a .csv file to your local computer by clicking the link
# 
# https://drive.google.com/uc?export=download&id=1J8IirxuOT0vLp2jl-yIitFCqVX71XzsN
# 
# This will allow you to download the data as a .csv file.  In the top left corner of this screen you should see a little file folder icon.   Selecting it opens a new window to the left of the notebook with three tabs: "Upload", "Refresh", and "Mount Drive". Select "Upload".  This should bring up a window that allows you to select the file "Lab10webpagedata.csv" from your local machine, which will upload the file to your notebook.  You will need to do this again if you decide to close your notebook and reopen it at a later time.

# %% [markdown]
# Once you've uploaded your file, convert it to a NumPy array called "webpage_data" by executing the following cell.

# %%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Lab10webpagedata.csv')
webpagedata=df.values
webpage_data=np.array(webpagedata)

# %% [markdown]
# Execute the following cell to visualize the network.

# %%
import networkx as nx
edges=[(i[0],i[1]) for i in webpagedata]
G=nx.from_edgelist(edges)
nx.draw(G,node_size=75)

# %% [markdown]
# **Problem 1**

# %%
def adj_matrix(n,edge_list):
  adj_m = np.zeros((n, n))
  for u, v in edge_list:
    adj_m[u, v] += 1
  return adj_m


# %%
# Use E1 to test your function.

E1=np.array([[0,1],[1,4],[0,2],[0,4],[1,3],[2,0],[2,4],[3,4],[3,2],[3,2]])

# %% [markdown]
# **Problem 2**

# %%
def degree_cent(n,edge_list):
  A = adj_matrix(n, edge_list)
  return np.sum(A, axis=0)


# %% [markdown]
# **Problem 3**

# %%
# Save the value you obtain in Problem 3 as the variable top_indegree.

deg_array = degree_cent(499, webpage_data)
top_indegree = np.flip(deg_array.argsort(), 0)[0]


# %% [markdown]
# **Problem 4**

# %%
def stoch_mat(A):
  T = np.transpose(A)
  return T / np.sum(T, axis=0)


# %%
# Use A2 to test your function.

A2= np.array([[0,1,0,0,0,0,0,0],
 [0,0,1,0,0,0,0,0],
 [1,0,0,1,0,1,1,0],
 [0,0,0,0,1,1,0,0],
 [1,0,1,0,0,0,0,0],
 [1,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,0,1],
 [1,0,0,0,0,0,0,0]])

# %% [markdown]
# **Problem 5**

# %%
def stoch_eig(P,k):
  n = P.shape[0]
  x = np.ones(n) / n
  for _ in range(k):
    x = P @ x
  return x


# %% [markdown]
# **Problem 6**

# %%
def PageRank_cent(n,edge_list,k):
  A = adj_matrix(n, edge_list)
  P = stoch_mat(A)
  return stoch_eig(P, k)


# %% [markdown]
# **Problem 7**

# %%
# Save the value you obtain in Problem 7 as the variable top_PageRank.

pr_vector = PageRank_cent(499, webpage_data, 100)
top_PageRank = np.flip(np.argsort(pr_vector), 0)[0]


# %% [markdown]
# **STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.   

# %% [markdown]
# **You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

# %% [markdown]
# To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to [gradescope.com](https://gradescope.com) for grading.


