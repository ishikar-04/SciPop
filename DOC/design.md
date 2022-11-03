#  ArtiLink Design

## Intended Broad Use of ArtiLink
Intended users of our software are academics primarily working in psychology, anthropology, or population health or other professionals conducting scholarly research or meta-research. Our intended users would ideally be able to search scholarly articles on a given topic of interest then get an output (.csv file, dashboard) of popular media articles which reference that scholarly media. 

## User Stories and Functional Design/ Use-Cases
Our software will ideally be designed to accomodate differences in user roles demonstrated below. In each of these three cases, the user responsibilities are different but the tool functions the same. However, there is variation in user expectation as well as differences in potential impact of each researchers line of work, helping the software designers as a signal detection test. Future applications of this software ideally could be used with other use-cases with reverse goals such as inputting popular or news media articles on a certain scientific topic and then the tool would scrape for the scientific articles. 

### Example User 1: Anthropologist Interested in Sex/Gender In Sports Research 
Delaney is an anthropologist interested in doing meta-research about how the press cites or uses scholarly research on the topic of sex/gender, hormone testing, and professional sports. For example, in many professional sports associations hormone testing for reproductive hormones (estrogen, testosterone) is still quite common. It is controversial because hormone levels are not specific to ones gender or neccessarily their biological sex assigned at birth. Delaney has a .csv file of scholarly articles organized by author first and last name, and DOI. She wants to be able to upload this .csv and get a .csv or visual dashboard of what types of press outlets (.e.g New York Times, Science) or popular media (Blogs) are making reference to these articles when they discuss sex/gender in sports. While Delaney’s research isn’t super high impact (compared to User 2), she still wants to know how this research line is being discussed in popular media. 

#### Use-Case for User 1:
User: Uploads a .csv file listing the empirical research that they are interested in scoping [DRAG AND DROP]  
Tool: Scrapes Google news for each of the selected matching print articles (i.e. not video transcripts) which contain (i) hyperlinked DOI, (ii) author name, or (iii) article title  
Tool: Saves list of search results in .csv file  
User: Exports/downloads the tool output 

### Example User 2: Oncology Researcher Wants to Scope Out High Impact Research and It's Use in Media 
An oncology researcher doing work on CART cell therapy, a popular and cutting edge immunotherapy. She wants to understand how the public is writing about new immunotherapy techniques. This oncology professor knows that this area of research is high impact and likely to get picked up by media within days to months of publishing. She doesn't have a pre-specified list of articles like User 1, but she wants to use UW libraries to search for the top 50 articles relevant to search terms about CART cell therapy and then use that .csv to explore how media is popularizing this scholarly research. 

#### Use-Case for User 2:
User:  navigates to UW library search  
User: searches for “CART Cell Therapy” peer-reviewed journal articles, filtered by year of choice (2021-2022) and searches top 50 results  
User: downloads the query to their computer as a .csv file  
User: uploads this .csv file to our software [DRAG AND DROP]  
Tool: Searches each of the selected matching print articles (i.e. not video transcripts) which contain (i) hyperlinked DOI, (ii) author name, or (iii) article title  
Tool: Saves list of search results in .csv file  
User: Exports/downloads the tool output 

### Example User 3: Social Science Researcher Interested in Seeing Media that Covered Her Recent Paper 
A social science researcher is interested in understanding how news media have covered the findings published in her most recent empirical article. Although she has found some news articles on the internet (e.g., Google News), she is looking for a quick and automated way to consolidate all of the URLs of news stories that cited her work (hyperlinked or mentioned by author name+institution) and were published by trusted news publications.

#### Use-Case for User 3:  
User: uploads this .csv file to our software [DRAG AND DROP]  
Tool: Searches each of the selected matching print articles (i.e. not video transcripts) which contain (i) hyperlinked DOI, (ii) author name, or (iii) article title  
Tool: Saves list of search results in .csv file  
User: Exports/downloads the tool output
