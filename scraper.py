#!/usr/bin/env python
# coding: utf-8

# ### This is the code for the web scraping functions using pygooglenews and other packages to scrape Google News according to a matrix of factors including author name, key words found in the titles of the peer-reviewed publications, DOI's and peer-reviewed journal names. 

# ### To get the user's interface: RUN "streamlit run scraper.py" in terminal

import nltk
from nltk.corpus import stopwords
import re
import string
from collections import Counter
import difflib as difflib

from pygooglenews import GoogleNews
import pandas as pd
import numpy as np
import streamlit as st

import warnings

warnings.filterwarnings('ignore')
gn = GoogleNews()


def main(df):
    """
    Main function which accepts a CSV file as input. Invokes (i) all scraping functions, 
    (ii) function which consolidates a list of relevant keywords. Returns a csv file containing
    academic journal article title, author, and DOI appended to related news 
    articles and their corresponding URLS
    Input: User's uploaded dataset in pandas.DataFrame format
    Output: Scraping results as a dataset in pandas.DataFrame format
    """
    # must be in same repository that the jupyter notebook is located in
    # df = pd.read_csv("UseCase1_Data.csv")
    
    df = df.dropna(how ='all') # drop last n rows because google news functions 
    #won't work with NaN or NA values, we need to add an ifelse/judgement to each function. We only can search for strings
    df.dropna(how='all', axis=1, inplace=True)
    
    # Matching steps
    # author_cols = [col for col in df.columns if 'author' in col]+[col for col in df.columns if 'Author' in col]
    #title_cols = [col for col in df.columns if 'title' in col]+[col for col in df.columns if 'Title' in col]
    #doi_labels = [col for col in df.columns if 'doi' in col]+[col for col in df.columns if 'DOI' in col]+[col for col in     df.columns if 'Doi' in col]
    
    #difflib.get_close_matches('Author_Name', author_cols)
    #difflib.get_close_matches('Title', title_cols)
    
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
    lst = [scraping_author_df, scraping_doi_df, scraping_title_df]  # List of your dataframes
    df_result= pd.concat(lst)
    
    # remove irrelevant and duplicate results
    df_result = df_result[df_result['key_count'] != 0]
    df_result.drop_duplicates(subset=['news_link'], inplace = True)

    return df_result
    

def key_words(df):
    """
    Key_words function to help eliminate results that are not relevant to the articles.
    Input: User's uploaded dataset in pandas.DataFrame format
    Output: 10 most common words in article titles in list format
    """
    article_titles = df['Article_Title'].to_list()

    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    punct = set(string.punctuation)
    
    for i in range(len(article_titles)):
        # lowercasing the text
        article_titles[i] = str(article_titles[i]).lower()
        # remove stopwords
        article_titles[i] = " ".join([word for word in article_titles[i].split() if word not in stop_words])
        # remove unicode
        text = article_titles[i].encode(encoding='ascii', errors='ignore').decode()
        article_titles[i] = " ".join([word for word in text.split()])
        # remove market ticker and hashtag
        article_titles[i] = re.sub('\$', '', article_titles[i])
        article_titles[i] = re.sub('\#', '', article_titles[i])
        # remove punctuation
        article_titles[i] = "".join([ch for ch in article_titles[i] if ch not in punct])
        
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
    #df_author = df.dropna([df.iloc'Author_Name'])
    df_author = df[df.Author_Name.notnull()]

    stories = []
    for i in range(len(df_author)):
        search = gn.search(df_author.iloc[i].loc['Author_Name'])
        newsitem = search['entries']
        for item in newsitem:
            story = {
                'Author_Name': df_author.iloc[i].loc['Author_Name'],
                'Article_Title': df_author.iloc[i].loc['Article_Title'],
                'Article_DOI': df_author.iloc[i].loc['Article_DOI'],
                'news_title': item.title, #change to 'news_title' for clarity
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
    stories = []
    df_doi = df[df.Article_DOI.notnull()]
    for i in range(len(df_doi)):
        search = gn.search(df_doi.iloc[i].loc['Article_DOI'])
        newsitem = search['entries']
        for item in newsitem:
            story = {
                'Author_Name': df_doi.iloc[i].loc['Author_Name'],
                'Article_Title': df_doi.iloc[i].loc['Article_Title'],
                'Article_DOI': df_doi.iloc[i].loc['Article_DOI'],
                'news_title': item.title, #change to 'news_title' for clarity
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
                'news_title': item.title, #change to 'news_title' for clarity
                'news_link': item.link
            }
            
            stories.append(story)    
    return stories


'''
The following codes is to set up users' interface with Streamlit.
'''
def _max_width_():
    """
    Display string formatted as Markdown.
    """
    
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

    
# Configures the default settings of the page.
st.set_page_config(page_icon="🎓", page_title="SCIPOP")

# Display an image with its url.
st.image(
    "https://png.pngitem.com/pimgs/s/202-2021802_graduation-cap-emoji-transparent-hd-png-download.png",
    width=100,
)

# Draw Markdown-formatted text, with input as a string.
st.write(
"""
# SCIPOP APP
Upload your article dataset to see the relevant news.\n
#### Dataset guidance:\n 
Column_Name: Author_Name, Article_Title, Article_DOI. Could see example dataset for reference.
"""
)

# Display a file uploader widget. Users can drag/drop their input file in .csv format.
uploaded_file = st.file_uploader("Upload CSV", type=".csv")

# Checkbox of example file to demo the app.
use_example_file = st.checkbox(
    "Use example file", False, help="Use in-built example file to demo the app"
)

# Path for example file.
if use_example_file:
    uploaded_file = "UseCase1_Data.csv"
    
# Read and preview input file.    
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("### Data preview")
    st.dataframe(df.head())

    output_df = main(df)
else:
    st.stop()

# Display a download button widget. Users can download their output file in .csv format.
st.download_button(
    label="Download data as CSV",
    data=output_df.to_csv().encode('utf-8'),
    file_name='news.csv',
    mime='text/csv',
)
