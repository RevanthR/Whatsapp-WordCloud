#!/usr/bin/env python
# coding: utf-8

# In[1]:


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


# In[12]:


df=pd.read_csv(r"Devil.csv",encoding="latin-1")


# In[13]:


comment_words=''
stopwords=set(STOPWORDS)


# In[ ]:


for val in df.MESSAGES:
    val=str(val)
    tokens=val.split()
    for i in range(len(tokens)):
        tokens[i]=tokens[i].lower()
    for words in tokens:
        comment_words= comment_words+words+''


# In[ ]:


wordcloud = WordCloud(width=800,height=800,background_color='white',stopwords=stopwords,min_font_size=10).generate(comment_words)


# In[ ]:


plt.figure(figsize=(8,8),facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()


# In[ ]:




