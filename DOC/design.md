#  SciPop Design

## Intended Broad Use of SciPop
Intended users of our software are academics primarily working in psychology, anthropology, or population health or other professionals conducting scholarly research or meta-research. Our intended users are able to search scholarly articles on a given topic of interest then get an output (.csv file) of media articles indexed on Google News which reference that scholarly media either by citing the scholarly author name, DOI of the scholarly article, or title of the scholarly article. 

## User Stories and Functional Design/ Use-Cases
Our software is designed to accomodate differences in user roles demonstrated below. In both cases, the user responsibilities are different but the tool functions the same. However, there is variation in user expectation as well as differences in potential impact of each researchers line of work, helping the software designers as a signal detection test. Future applications of this software ideally could be used with other use-cases with reverse goals such as inputting popular or news media articles on a certain scientific topic and then the tool would scrape for the scientific articles. 

### Example User 1: Anthropologist Interested in Sex/Gender In Sports Research 
Delaney is an anthropologist interested in doing meta-research about how the press cites or uses scholarly research on the topic of sex/gender, hormone testing, and professional sports. For example, in many professional sports associations hormone testing for reproductive hormones (estrogen, testosterone) is still quite common. It is controversial because hormone levels are not specific to ones gender or neccessarily their biological sex assigned at birth. Delaney has a .csv file of scholarly articles organized by author first and last name, article title, and DOI. She wants to be able to upload this .csv and get a .csv list of news media indexed on Google News that are making reference to these articles when they discuss sex/gender in sports. Rather than having to search each article individually on Google News, SciPop will produce an output for the user to use as they wish. 

#### Use-Case for User 1:
User: Uploads/drags and drops a .csv file on the SciPop uploader webpage. The .csv must list the scholarly author name (labeled "Author_Name"), journal article titles (labeled "Article_Name"), and/or DOIs (labeled "Article_DOI) that the user is interested in scoping [DRAG AND DROP]  
Tool: Reads in the .csv, scrapes Google News for each of the selected matching print articles (i.e. not video transcripts) which contain (i) hyperlinked DOI, (ii) author name, or (iii) article title  
Tool: Provides minimal quality checks/tests by calculating a count of how many of the most common 10 words from the scholarly article titles are present in the titles of the scraped Google News item links. The tool uses this to delete irrelevant scrape results. 
Tool: Saves list of search results in .csv file  
User: Exports/downloads the tool output 

### Example User 2: Oncology Researcher Wants to Scope Out High Impact Research and It's Use in Media 
An oncology researcher doing work on CART cell therapy, a popular and cutting edge immunotherapy. She wants to understand how the public is writing about new immunotherapy techniques. This oncology professor knows that this area of research is high impact and likely to get picked up by media within days to months of publishing. She doesn't have a pre-specified list of articles like User 1, but she wants to use UW libraries to search for the top 50 articles relevant to search terms about CART cell therapy and then use that .csv to explore how media is popularizing this scholarly research. 

#### Use-Case for User 2:
User: Navigates to UW library search  
User: Searches for “CART Cell Therapy” peer-reviewed journal articles, filtered by year of choice (2021-2022) and searches top 50 results  
User: Downloads the query to their computer as a .csv file  
User: Renames column headers to SciPop-compliant labels (Author_Name, Article_Title, or Article_DOI)
User: Uploads this .csv file to our software [DRAG AND DROP]  
Tool: Reads in the .csv, scrapes Google News for each of the selected matching print articles (i.e. not video transcripts) which contain (i) hyperlinked DOI, (ii) author name, or (iii) article title  
Tool: Provides minimal quality checks/tests by calculating a count of how many of the most common 10 words from the scholarly article titles are present in the titles of the scraped Google News item links. The tool uses this to delete irrelevant scrape results. 
Tool: Saves list of search results in .csv file  
User: Exports/downloads the tool output 


## Component Design

### Root component – Web scraper for Google News
This is developed as a primary component which is not dependent on the features which upload or download the CSV files. THEREFORE it can be tested independently. We adapted the GoogleNews package in Python to scrape results from Google News. This was tested from use-case 1. 


### Component 2- DOI/Citation Input by the User
User will upload a .csv file in which each row contains data regarding a single publication. Each column stores a different identifying feature of the article (e.g. article title, DOI, first author last name, first author given name) to optimize scraping results. 

![Image](https://github.com/ishikar-04/CSE583-Project/blob/main/IMAGE/Screengrab%20Tech%20Spec.png?raw=true)

### Component 3 - Popular Article Storage from Web Scrape 
Web scraper will return scrape as a list with popular media articles  
List of results will be stored as a data frame in Pandas  
User downloads stored dataframe as .csv from the SciPop webpage. 

### Component 4 - Users’ Interface App
A website for users to upload a input file in .csv format, showing the preview for input to help users check what they upload is right, and then giving back the scraping results to them as a .csv file.
