#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import seaborn package
import seaborn as sns

# import matplotlib package
import matplotlib.pyplot as plt

# import pandas package
import pandas as pd

# read excel file specifying sheet name
df = pd.read_excel('downloads/baserate.xls', sheet_name= 'Data')

# set seaborn built in style theme to whitegrid
sns.set_style('whitegrid')

# set seaborn lineplot specifying x and y variables and the data to use
sns.lineplot(x= 'Date', y= 'Official Bank Rate %', data=df)

# set matplotlib title
plt.title('Bank of England Base Rate - August 2006 to June 2023')

# set matplotlib x axis label
plt.xlabel('Date')

# set matplotlib y axis label
plt.ylabel('Official Bank Rate %')

# remove the top and right spines within seaborn (borders of the figure that contain the visualisation)
sns.despine()

# show the matplotlib line graph
plt.show()


# In[ ]:




