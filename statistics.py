#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv('E:/AIML/Descriptive_Statistics-master/CC_Expenses_Exercise.csv')


# In[3]:


data


# In[4]:


cc = data.Credit_Card_usage


# In[5]:


cc


# In[6]:


cc.describe()

  
# In[7]:


gender = data.Sex


# In[8]:


cc.groupby(gender).mean()


# In[9]:


shop = data.Shopping


# In[10]:


cc.groupby(shop).mean()


# In[11]:


bank = data.Banking


# In[12]:


bank


# In[13]:


cc.groupby(bank).mean()


# In[15]:


import matplotlib.pyplot as plt
plt.hist(cc)
plt.show()


# In[19]:


data.boxplot(column='Credit_Card_usage', by = 'Sex' )
plt.show()


# In[ ]:


myData.boxplot(column='Credit_Card_usage',by='Sex')
myplot.show()


# In[20]:


cc.groupby([gender, bank]).mean()


# In[21]:


cc.groupby([gender, bank, shop]).mean()


# In[22]:


cc.groupby([gender, bank,shop]).describe()


# In[ ]:





# In[ ]:




