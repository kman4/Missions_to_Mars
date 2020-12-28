#!/usr/bin/env python
# coding: utf-8

import requests
import json 
from bs4 import BeautifulSoup as bs
import splinter 


def scrape_all(): 
    executable_path = {'executable_path' : 'chromedriver.exe'}
    browser = splinter.Browser('chrome', **executable_path)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html

soup = bs(html, 'html.parser')
print(soup.prettify())


content = soup.find("div", class_='content_page')

titles = content.find_all("div", class_='content_title')
print(titles[0].text.strip())

article_text = content.find_all("div", class_='article_teaser_body')
article_text[0].text

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html

soup = bs(html, 'html.parser')
featured_image = soup.find("article", class_='carousel_item')['style']

latter = featured_image.split('/spaceimages/')[1].split("'")[0]

former = url.split('?')[0]

final_url = former + latter
final_url

browser.find_by_id("full_image").click()

browser.find_by_text("more info     ").click()

html = browser.html
soup = bs(html, 'html.parser')
featured_img = soup.find("img", class_='main_image')['src']

featured_img
pic_url = f"https://www.jpl.nasa.gov{featured_img}"

pic_url

def insert_into_mongo(): 
