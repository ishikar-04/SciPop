#!/usr/bin/env python
# coding: utf-8

# ### To get the user's interface: RUN "streamlit run scraper.py" in terminal

"""
This is the code for the web scraping functions using pygooglenews and other packages 
to scrape Google News according to a matrix of factors including author name, key words 
found in the titles of the peer-reviewed publications, DOI's and peer-reviewed journal names.
"""

import re
import string
import warnings
from collections import Counter

import nltk
from nltk.corpus import stopwords
from pygooglenews import GoogleNews
import pandas as pd
import streamlit as st

warnings.filterwarnings('ignore')
gn = GoogleNews()

# Avoid saying df is not a good name
# pylint: disable=invalid-name


def main(df):
    """
    Main function which accepts a CSV file as input. Invokes (i) all scraping functions,
    (ii) function which consolidates a list of relevant keywords. Returns a csv file containing
    academic journal article title, author, and DOI appended to related news
    articles and their corresponding URLS
    Input: User's uploaded dataset in pandas.DataFrame format
    Output: Scraping results as a dataset in pandas.DataFrame format
    """

    # raise error for invalid input
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The input argument should be in pd.DataFrame format")
    
    # raise error for invalid number of columns
    if  len(df.columns) < 3:
        raise ValueError("The number of variables in the dataset should be at least 3")

    df = df.dropna(how='all')
    df.dropna(how='all', axis=1, inplace=True)

    # Matching steps need to be added
    
    # get keywords in the article title to remove useless results
    keyword_list = key_words(df)
    keyword_list = (list(zip(*keyword_list))[0])

    # scrap by author name
    scraping_author_df = pd.DataFrame(scraping_author(df))
    key_count = [0]*len(scraping_author_df)
    for i in range(len(scraping_author_df)):
        for j in range(len(keyword_list)):
            if keyword_list[j] in scraping_author_df.iloc[i].loc['news_title']:
                key_count[i] = key_count[i]+1

    # know how many key words in each result when scraping by author name
    scraping_author_df['key_count'] = key_count

    # scrap by doi
    scraping_doi_df = pd.DataFrame(scraping_doi(df))

    # scrap by title
    scraping_title_df = pd.DataFrame(scraping_title(df)) 

    # concat all df's together
    lst = [scraping_author_df, scraping_doi_df, scraping_title_df]
    df_result = pd.concat(lst)

    # remove irrelevant and duplicate results
    df_result = df_result[df_result['key_count'] != 0]
    df_result.drop_duplicates(subset=['news_link'], inplace=True)

    return df_result


def key_words(df):
    """
    Key_words function to help eliminate results that are not relevant to the articles.
    Input: User's uploaded dataset in pandas.DataFrame format
    Output: 10 most common words in article titles in list format
    """
    
    # raise error for no title column
    if 'Article_Title' not in df.columns:
        raise ValueError("No available columns for counting keywords")
    
    # raise error if the type of values (except Null) is not string
    df_article_title = df[df.Article_Title.notnull()]
    if not isinstance(df_article_title.iloc[0].loc['Article_Title'], str):
        raise TypeError("Article title should be a string")

    article_titles = df['Article_Title'].to_list()

    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    punct = set(string.punctuation)

    for i in range(len(article_titles)):
        # lowercasing the text
        article_titles[i] = str(article_titles[i]).lower()
        # remove stopwords
        article_titles[i] = " ".join([word for word in article_titles[i].split() 
                                      if word not in stop_words])
        # remove unicode
        text = article_titles[i].encode(encoding='ascii', errors='ignore').decode()
        article_titles[i] = " ".join([word for word in text.split()])
        # remove market ticker and hashtag
        article_titles[i] = re.sub('\$', '', article_titles[i])
        article_titles[i] = re.sub('\#', '', article_titles[i])
        # remove punctuation
        article_titles[i] = "".join([ch for ch in article_titles[i] 
                                     if ch not in punct])

    res = ' '.join(article_titles)
    res = res.split(' ')
    return Counter(res).most_common(10)


def scraping_author(df):
    """
    This function scrapes google news for anything matching the
    scholarly author name in df
    Input: User's uploaded dataset in pandas.DataFrame format
    Output: Scraping results as a dataset in pandas.DataFrame format
    """

    # raise error for no author column
    if 'Author_Name' not in df.columns:
        raise ValueError("No available column for scarping by author_name")

    # raise error for no doi column
    if 'Article_DOI' not in df.columns:
        raise ValueError("No available column for scarping by DOI")
    
    # raise error if the type of values (except Null) is not string
    df_author = df[df.Author_Name.notnull()]
    if not isinstance(df_author.iloc[0].loc['Author_Name'], str):
        raise TypeError("Author name should be a string")


    stories = []
    for i in range(len(df_author)):
        search = gn.search(df_author.iloc[i].loc['Author_Name'])
        newsitem = search['entries']
        for item in newsitem:
            story = {
                'Author_Name': df_author.iloc[i].loc['Author_Name'],
                'Article_Title': df_author.iloc[i].loc['Article_Title'],
                'Article_DOI': df_author.iloc[i].loc['Article_DOI'],
                'news_title': item.title,
                'news_link': item.link
            }

            stories.append(story) 
    return stories


def scraping_doi(df):
    '''
    This function scrapes google news for anything matching the
    scholarly DOI in df
    Input: User's uploaded dataset in pandas.DataFrame format
    Output: Scraping results as a dataset in pandas.DataFrame format
    '''
    
    # raise error if the type of values (except Null) is not string
    df_doi = df[df.Article_DOI.notnull()]
    if not isinstance(df_doi.iloc[0].loc['Article_DOI'], str):
        raise TypeError("DOI should be a string")

    stories = []
    for i in range(len(df_doi)):
        search = gn.search(df_doi.iloc[i].loc['Article_DOI'])
        newsitem = search['entries']
        for item in newsitem:
            story = {
                'Author_Name': df_doi.iloc[i].loc['Author_Name'],
                'Article_Title': df_doi.iloc[i].loc['Article_Title'],
                'Article_DOI': df_doi.iloc[i].loc['Article_DOI'],
                'news_title': item.title,
                'news_link': item.link
            }

            stories.append(story) 
    return stories


def scraping_title(df):
    '''
    This function scrapes google news for anything matching the
    scholarly title in df
    Input: User's uploaded dataset in pandas.DataFrame format
    Output: Scraping results as a dataset in pandas.DataFrame format
    '''
    stories = []
    df_article_title = df[df.Article_Title.notnull()]
    for i in range(len(df_article_title)):
        search = gn.search(df_article_title.iloc[i].loc['Article_Title'])
        newsitem = search['entries']
        for item in newsitem:
            story = {
                'Author_Name': df_article_title.iloc[i].loc['Author_Name'],
                'Article_Title': df_article_title.iloc[i].loc['Article_Title'],
                'Article_DOI': df_article_title.iloc[i].loc['Article_DOI'],
                'news_title': item.title,
                'news_link': item.link
            }

            stories.append(story) 
    return stories
