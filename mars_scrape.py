# 1. Dependencies
import pandas as pd
import requests
import pymongo
import time
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# 2. Set up connection path to driver 
def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path , headless=False)

def scrape ():
    browser= init_browser()
    return {
        'mars_news': mars_news(browser),
        'mars_featured_image': mars_image (browser),
        'mars_tweet': mars_weather_tweet(browser),
        'mars_facts':mars_facts (),
        'mars_hemispheres': mars_hemispheres (browser)
    }
# 3. Scrape info from mars news
def mars_news(browser):
    # browser = init_browser ()
#Create Mars global dictionary that can be imported to Mongo
    news_titles = {}    
    url='https://mars.nasa.gov/news/'
    # browser = init_browser()
    time.sleep(2)
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
