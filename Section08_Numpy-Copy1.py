#!/usr/bin/env python
# coding: utf-8

# # Numpy Array 

# In[2]:


import numpy as np
x = np.array([1,2,3], np.int16)


# In[3]:


print(x, type(x))


# In[4]:


x = np.array([[1,2,3],[4,5,6]], np.int16)


# In[5]:


print(x)


# In[11]:


x.shape, x.ndim, x.dtype


# In[12]:


x


# In[13]:


x.size


# In[14]:


x.nbytes


# In[15]:


x.T


# # Numpy Constants
# 

# In[16]:


np.inf, np.NAN, np.NINF, np.NZERO, np.PZERO


# In[18]:


np.e, np.euler_gamma, np.pi


# test 3

# In[2]:


import os


# In[3]:


[k for k in os.environ.keys() ]


# ttt

# In[ ]:




