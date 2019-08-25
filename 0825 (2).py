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


# In[13]:


cg = df["10"].values


# In[14]:


cg


# In[ ]:





# 原本的是浮點數?我把它換成str,但還是不能計算

# In[15]:


cg.mean()


# In[22]:


cg = str(cg)


# In[23]:


cg


# In[24]:


cg.mean()


# In[ ]:




