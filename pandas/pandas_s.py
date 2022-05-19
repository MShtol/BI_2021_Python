#!/usr/bin/env python
# coding: utf-8

# In[258]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


# ****1. Read from tsv and plot****

# In[38]:


# 54/0.006896
# 7911.0/ 0.983503
24/0.002310


# In[57]:


df = pd.read_csv('train.csv')

# sns.plot(data=df, x='pos',y=A_fraction)
df.head()


# For every pos there is one missing value for in nucleotide count (and respective frequency is missing too).
# Restoring total number of reads returns different values:
# * A| 7911.0/0.983503 == 8044
# * C| 54.0/0.006896 == 7831
# * T| 11.0/0.000815 = 13497
# 
# Same is true for other rows.
# 
# For simplification we will consider missing freqency as (1-a-b-c), where a,b,c are remaining frequencies.

# In[145]:


freq_df = df.iloc[:,[0,10,11,12,13]].set_index('pos')

for index, row in freq_df.iterrows():
    mask = row.isna().values
    row[mask] = 1 - np.sum(row[~mask])


freq_df.plot(figsize=(20, 5))
plt.ylabel('Frequency', fontsize=15)
plt.xlabel('pos', fontsize=15)
plt.show()


# **2. Data selection**

# In[149]:


df_select = df[df['matches'] > df['matches'].mean()][['pos', 'reads_all', 'mismatches',
                                                      'deletions', 'insertions']]

df_select.to_csv('train_select.csv')


# **3. EDA of dataset** 
# Int his dataset we have data about 499 customers and some info about their purchases, marital status, educatuin, income, burth year

# In[152]:


eda = pd.read_csv('customers.csv')


# In[160]:


eda.head()


# All columns except educational_level, marital_status and purhcase_date contain numbers.

# In[158]:


eda.info()


# We have 499 customers and 12 columns with data. There are no null values in dataframe. Also, "purhcase_date" contains typo

# In[171]:


eda = eda.rename(columns={'purhcase_date':'purchase_date'})


# In[173]:


eda['educational_level'].unique()


# looks OK

# In[175]:


eda['marital_status'].unique()


# Not uniformed. Let's male all widows widowed!!

# In[177]:


eda['marital_status'] = eda['marital_status'].replace('Widow', 'Widowed')


# Do we have duplocates?

# In[180]:


eda.drop_duplicates().shape


# No, we don't.
# Let's look on some stats.

# In[189]:


eda = eda.drop(columns='customer_id')


# In[190]:


eda.describe()


# Here we can see some intresting stuff. with avg birthyear 1978 we have some really old person - 1899 year og birth! Also we can see, that at least 75% customers don't leave complaints. With median online purchases we have someone who bought onlibe 27 times.
# 
# Let's see grouped data

# In[201]:


eda.groupby('educational_level').mean()


# In[202]:


eda.groupby('educational_level').std()


# Among intresting we can see that annual income is drasstically differs from other groups only in Basic educational level. Differncies between other groups is insignificant.

# In[224]:


sns.histplot(eda['annual_income'])


# Looks like bimodal distribution.

# In[246]:


eda.groupby('educational_level')['annual_income'].plot.density(legend=True,figsize=(20,15))


# We can assume that first peak of bimodal distibution is comprised of customers with Basic ad some High-school educatuin.
# 
# Let's look at correlations between numeric variables

# In[245]:


correlations = eda.corr()
sns.heatmap(correlations, xticklabels=correlations.columns,
            yticklabels=correlations.columns, annot=True);


# The only strong correlations we see is between annual income

# #### 4. working with real data (.gff, .bed)
# ##### 4.1 Write function for reading .gff and .bed

# In[253]:


def read_gff(path):
    """
    Reads .gff file from path, renames columns and returns pd.DatFrame
    """
    return pd.read_csv(path,
                       sep="\t",
                       names=["chromosome","source","type","start","end",
                              "score","strand","phase","attributes"],
                       comment="#")


def read_bed6(path):
    """
    Reads 6-column .bed file from path, renames columns and returns pd.DatFrame
    """
    return pd.read_csv(path,
                       sep="\t",
                       names=["chromosome","start","end","name","score","strand"])


# ##### 4.2 reformat attribute column data to readble format

# In[268]:


gff = read_gff('rrna_annotation.gff')

gff['attributes'] = gff['attributes'].str.replace('=','_').str.split('_').str[1]


# ##### 4.3  Count grouped data and plot it

# In[367]:


gff.groupby(["chromosome",'attributes']
           ).agg({'attributes':'count'}
                ).rename(columns={'attributes':'count'}
                        ).unstack(fill_value=0)


# In[366]:


plt.figure(figsize=(20,10))
sns.countplot(data=gff, x=gff.chromosome, hue=gff.attributes)
plt.xticks(rotation = 60)
plt.legend(fontsize=15)
plt.show()


# ##### 4.4 reproduce bedtools intersec

# We can do it by merging both tables with innier join and just filter rows where rrnas falls into contig

# In[383]:


comb_tbl = gff.merge(bed, how='inner', on='chromosome')
comb_tbl = comb_tbl[(comb_tbl['start_y'] < comb_tbl['start_x']) & (comb_tbl['end_y'] >= comb_tbl['end_x'])]

comb_tbl

