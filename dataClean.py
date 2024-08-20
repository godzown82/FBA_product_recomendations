#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import seaborn as sns
import gitconfig

""" ## Data cleaning function:"""
# 

# In[ ]:
def clean_up():

    env_path = gitconfig.env_path
    env_path
    data_df = pd.read_csv(f'{env_path}/amazon.csv')
    data_df.head()


    # ### Replace special characters and columns with number values to numbers

    # In[ ]:


    #gather all the columns that need to be converted
    cols = ['discounted_price','actual_price','rating','discount_percentage','rating_count'] 

    for col in cols:
        #remove the '₹' character from the pricing columns
        data_df[col] = data_df[col].str.replace('[₹]', '', regex=True)
        #remove the '%' character from the discount percentage column
        data_df[col] = data_df[col].str.replace('[%]', '', regex=True)
        #remove the ',' character from the discount percentage column
        data_df[col] = data_df[col].str.replace('[,]', '', regex=True)
        #convert the columns to numerics
        data_df[col] = pd.to_numeric(data_df[col],errors='coerce')

    return data_df

