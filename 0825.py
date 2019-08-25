#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt


# In[2]:


import pandas as pd


# In[3]:


get_ipython().run_line_magic('ls', '')


# In[4]:


df = pd.read_csv("ch4-2.csv")


# In[5]:


df.head()


# In[6]:


df["10"]


# In[8]:


df.plot()


# In[ ]:




