#!/usr/bin/env python
# coding: utf-8

# Xiaojun Wang
# Email: xiaojunw@umich.edu

# In[5]:


import numpy as np
import pandas as pd


# ## Pandas idioms
# 
# - `pandas` is a powerful toolkit for data scientists to manipulate data and analyze the data.
# - Pandas idioms are some features that makes the codes more readable, verstile and efficient.

# ## Data selection idioms
# 
# - We can use `df.loc[condiction, column name]` or `df[condiction]` sytax to select data that satisfy the condictions. 
# - We can use `&` representing `and` and `|` representing `or` to include multiple condictions.

# ### Example

# In[6]:


df = pd.DataFrame(
    {"name": ["Tom", "Jerry", "Kathy", "Selina"], "year": ["Freshman", "Sophmore", "Freshman", "Senior"], "grade": [76, 92, 98, 100]}
)
df


# In[7]:


# 1) Let's find the students who gets full score
df[df["grade"]==100]


# In[8]:


# 2) Let's find the first-year student whose grades are higher than 90
df.loc[(df["year"] == 'Freshman') & (df["grade"] > 90), "name"]


# ## Value assigment
# 
# - Sometimes we want to modify the data after selection. There are two ways to achieve the goal:
# - 1) Use `df.loc` and `=`
# - 2) Create a "mask" and use `df.where` to find the target data and assign the value

# ### Example

# In[9]:


# 3) The instructor just found out that there is a grading mistake for Tom's assignment. 
# His grade should be 80 instead.
# First method: 
df1, df2 = df, df
df1.loc[df["name"] == 'Tom', "grade"] = 80
df1


# In[10]:


# Second method:
mask = pd.DataFrame({"name": [True] * 4, "year": [True] * 4, "grade": [False, True, True, True]})
df2.where(mask, 80)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




