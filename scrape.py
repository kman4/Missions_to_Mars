#!/usr/bin/env python
# coding: utf-8

# In[1]:


#! pip install splinter


# In[2]:


#! pip install webdriver_manager


# In[3]:


# importing Dependencies
import requests
from bs4 import BeautifulSoup as bs
import splinter 
import pandas as pd
import pymongo
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
# this detects what broswer version u have installed and advice the .exe file need to be installed.


# In[4]:


# Running Chromedriver
executable_path = {'executable_path' : 'chromedriver.exe'}
browser = splinter.Browser('chrome', **executable_path)


# In[9]:


# Scarpping Mars news URL page 
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
soup =  bs(html, 'html.parser')
print(soup.prettify())


# In[10]:


# Printing the latest news title and paragraph


# In[11]:


content = soup.find("div", class_= "content_page")


# In[12]:


titles = content.find_all("div", class_='content_title')
titles[0].text


# In[13]:


# Printing Paragraph Text
article_text = content.find_all("div", class_='article_teaser_body')
article_text[0].text


# In[14]:


# Trying to scrape image

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html


# In[15]:


soup = bs(html,'html.parser')
featured_image = soup.find("article",class_='carousel_item')['style']


# In[16]:


latter = featured_image.split('/spaceimages/')[1].split("'")[0]


# In[17]:


former = url.split("?")[0]


# In[18]:


final_url = former + latter
final_url


# In[19]:


# Mars facts to be scraped

facts_url = 'https://space-facts.com/mars/'
mtables = pd.read_html(facts_url)
mtables


# In[20]:


facts_df = mtables[2]
facts_df.columns = ["Description", "Value"]
facts_df


# In[21]:


html_table = facts_df.to_html()
html_table.replace('\n', '')
print(html_table)


# In[23]:


#  scrapping Mars hemisphere image


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
soup =  bs(html, 'html.parser')
hemisphere = []

products = soup.find("div", class_ = "result-list" )
mars_hemispheres = products.find_all("div", class_="item")

for mars_hemisphere in mars_hemispheres:
    title = mars_hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = mars_hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup= bs(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    hemisphere.append({"title": title, "img_url": image_url})


# In[24]:


# printing link
    
hemisphere


# In[25]:


# closing broswer
browser.quit()


# In[ ]:




