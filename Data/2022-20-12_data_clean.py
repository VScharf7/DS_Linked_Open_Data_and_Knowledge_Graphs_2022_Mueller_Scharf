#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("sRNATarBase3_w_target_from_1_to_terminal.csv")


# In[2]:


df.columns


# In[7]:


df.drop(['ID', 'REGULATION', 'PMID', 'SRNA_SEQ', 'TARGET_SEQ'], axis=1, inplace=True)


# In[9]:


df.shape


# In[16]:


srna = df[['SRNA_NAME', 'SRNA_ALIAS', 'SRNA_TYPE', 'SRNA_LENGTH', 'SRNA_START', 'SRNA_END', 'SRNA_STRAND']]
target = df[['TARGET_NAME', 'TARGET_ALIAS', 'TARGET_TYPE', 'TARGET_LENGTH',
       'TARGET_START', 'TARGET_END', 'TARGET_STRAND', 'TARGET_REGION']]
bac = df[['TAXID', 'ORG_CODE', 'STRAIN_NAME']]


# In[17]:


print(srna.head(2))
print(target.head(2))
print(bac.head(2))


# In[18]:


get_ipython().system('pwd')


# In[19]:


srna.to_csv('srna.csv')


# In[20]:


target.to_csv('target.csv')


# In[21]:


bac.to_csv('bacteria.csv')


# In[ ]:




