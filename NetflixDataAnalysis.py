#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


data=pd.read_csv(r"C:\Users\LENOVO\Downloads\file.csv")


# In[5]:


data


# In[7]:


data.head()


# In[8]:


data.tail()


# In[9]:


data.shape


# In[10]:


data.size


# In[11]:


data.columns


# In[13]:


data.dtypes


# In[14]:


data.info()


# In[15]:


data[data.duplicated()]                                                        # to check duplicate record in dataset


# In[16]:


data.drop_duplicates(inplace=True)                                        # to remove duplicate cell


# In[17]:


data[data.duplicated()]  


# Task. Is there any Null Value present in any column ? Show with Heat-map.

# In[18]:


data.isnull()                                                            # to check the null


# In[19]:


data.isnull().sum()                                               # to count null value


# In[38]:


import seaborn as sns                                           # to import seaborn library
import matplotlib.pyplot as plt


# In[21]:


sns.heatmap(data.isnull())                                      # to see the null value using heatmap


# Q.1. For 'House of Cards', what is the Show Id and Who is the Director of this show?

# In[22]:


data.head()


# In[26]:


data[data['Title'].isin(['House of Cards'])]


# In[29]:


data[data['Title'].str.contains('House of Cards')]


# Q.2. In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.

# In[30]:


data.dtypes


# In[31]:


data['Date_N']=pd.to_datetime(data['Release_Date'])


# In[32]:


data.head()


# In[33]:


data['Date_N'].dt.year.value_counts()


# In[34]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# Q.3. How many Movies & TV Shows are in the dataset ? Show with Bar Graph.

# In[35]:


data.head(2)


# In[36]:


data.groupby('Category').Category.count()


# In[41]:


sns.countplot(data=data, x='Category')


# Q.4. Show all the Movies that were released in year 2000.

# In[42]:


data.head(2)


# In[43]:


data['Year']=data['Date_N'].dt.year


# In[44]:


data.head(2)


# In[45]:


data[(data['Category']=='Movie')&(data['Year']==2020)]


# Q.5. Show only the Titles of all TV Shows that were released in India only.

# In[46]:


data.head(2)


# In[47]:


data[(data['Category']=='TV Show')&(data['Country']=='India')]


# In[48]:


data[(data['Category']=='TV Show')&(data['Country']=='India')]['Title']


# Q.6. Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix?

# In[49]:


data.head(2)


# In[50]:


data['Director'].value_counts().head(10)


# Q7. Show all the records,where "category is movie and type is comedies"or" country is United Kingdom".

# In[51]:


data.head(2)


# In[52]:


data[(data['Category']=='Movie')&(data['Type']=='Comedies')|(data['Country']=='United Kingdom')]


# Q8. In how many Movies/show ,Tom Cruise was casted?

# In[53]:


data.head(2)


# In[54]:


data[data['Cast']=='Tom Cruise']


# In[55]:


data[data['Cast'].str.contains('Tom Cruise')]


# In[56]:


data_new=data.dropna()


# In[57]:


data_new.head(2)


# In[59]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# Q9.What are the different ratingd defined by Netflix?

# In[60]:


data.head(2)


# In[61]:


data.Rating.nunique()


# In[62]:


data.Rating.unique()


# Q9.1 How many Movies got the'TV-14' rating,in Canada?

# In[63]:


data.head(2)


# In[69]:


data[(data['Category']=='Movie')&(data['Rating']=='TV-14')].shape


# In[70]:


data[(data['Category']=='Movie')&(data['Rating']=='TV-14')&(data['Country']=='Canada')].shape


# Q9.2 How many TV show got the 'R' rating, after year2018?

# In[71]:


data.head(2)


# In[73]:


data[(data['Category']=='TV Show')&(data['Rating']=='R')&(data['Year']>2018)]


# Q10 What is the maximum duration of a Movie/TV Show on Netflix?

# In[74]:


data.head(2)


# In[75]:


data['Duration'].unique()


# In[79]:


data[['Minute', 'Unit']]=data['Duration'].str.split(' ',expand=True)


# In[87]:


data.drop(columns=['Minutes'], inplace=True)


# In[81]:


data.head()


# In[82]:


data.shape


# In[83]:


data['Minute'].max()


# Q11. Which individual country has highest number of tv shows?

# In[86]:


data.head(2)


# In[88]:


data_tvshow=data[data['Category']=='TV Show']


# In[89]:


data_tvshow.head(2)


# In[90]:


data_tvshow.Country.value_counts()


# In[91]:


data_tvshow.Country.value_counts().head(1)


# Q12 How can we sort the dataset by Year?

# In[92]:


data.head(2)


# In[94]:


data.sort_values(by='Year').head(2)


# In[95]:


data.sort_values(by='Year',ascending =False).head(2)


# Q13 Find all the instances where:
#     Category is 'Movie' and type is 'Drama'
#     Or
#     Category is 'TV Show' And type is 'Kid TV'

# In[96]:


data.head(2)


# In[98]:


data[(data['Category']=='Movie')&(data['Type']=='Dramas')]


# In[102]:


data[(data['Category']=='TV Show')&(data['Type']=="Kids' TV")]


# In[103]:


data[(data['Category']=='Movie')&(data['Type']=='Dramas')| (data['Category']=='TV Show')&(data['Type']=="Kids' TV") ]


# In[ ]:




