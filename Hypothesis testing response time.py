#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from scipy import stats as stats1


# In[7]:


data = pd.read_csv("E:/AIML/Hypothesis-Testing---One-sample-t-test-master/datasets/Complaint_Response_Time.csv")


# In[8]:


data


# In[9]:


d1 = data.Response_Time


# In[10]:


d1


# In[11]:


stats1.ttest_1samp(d1,30)


# In[12]:


d1.mean()


# In[ ]:




