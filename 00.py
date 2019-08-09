#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[4]:


a = randint(1, 101)
b = int(input(">> "))
while b != a:
    if b < a:
        print("bigger")
    
    else:
        print("smaller")
    
    b = int(input(">> "))
    
else:
    print("you're right!:)")


# In[ ]:




