#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Flask


# In[6]:


app = Flask(__name__)


# In[7]:


@app.route('/')
def hello_world():
    return 'Hello world'


# In[ ]:




