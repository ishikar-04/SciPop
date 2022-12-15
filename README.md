# SciPop
This is the readme file for software called SciPop created by Ishika Ray, Delaney Glass, and Qiyao Liu. This software is used for identifying news articles that mention or discuss scholarly research (journal articles or DOIs) or scholars themselves. This software is ideal for researchers interested in meta-science or interested in public conversations and reports of scholarly research. The user will navigate to <insert link for the landing page> and upload a .csv file with three columns titled "Author_Name", "Article_Title", and "Article_DOI" which refers to the scholarly author name (first last), the title of the scholarly journal article, and the DOI link of the scholarly article. SciPop will use a variety of technologies (Python, pygooglenews package, and others) to compile a list of relevant google news article titles and links, exportable as a .csv.

### Who Can Use SciPop? ###
Anyone can use SciPop, however it may be most useful to researchers and students who are studying specific topics and want to see how those topics or specific academic articles are being talked about in news media and popular culture indexed on Google News.

### How To Use SciPop? ###
Step 1:
Prepare your input .csv file with 1 sheet/page with column headings "Author_Name", "Article_Title", and "Aritcle_DOI". If you choose to only input some of the three column information, our software may be limited in the results it produces.  

Step 2:  
Navigate to <insert landing page link>

Step 3:  
Click "Drag and Drop File Here" and proceed to drag and drop your .csv

Step 4:  
Wait for your updated .csv file to appear then click "Download"

Step 5:  
Use your .csv as you wish and cite SciPop!
  
### Repository Structure ###
  
.
└── CSE583-Project
  
    ├── DOC
 
  │   ├── __init__.py
  
  │   ├── __pycache__
  
  │   │   └── __init__.cpython-39.pyc
  
  │   └── design.md
  
  ├── IMAGE
  
  │   ├── Screengrab Tech Spec.png
  
  │   └── logo-color.png
  
  ├── LICENSE
  
  ├── README.md
  
  ├── __pycache__
  
  │   ├── scraper.cpython-39.pyc
  
  │   └── testSciPop.cpython-39.pyc
  
  ├── environment.yml
  
  ├── examples
  
  │   ├── UseCase1_Data.csv
  
  │   ├── UseCase2_Data.csv
  
  │   ├── functions_bad input.ipynb
  
  │   └── testcase_example.ipynb
  
  ├── scipop
  
  │   ├── __init__.py
  
  │   └── scraper.py
  
  └── tests
  
  ├── __init__.py
  
  └── testSciPop.py  
  
 

### How Can I View The Behind-The-Scenes Code? ###  

Navigate to "examples/testcase_notebook.ipynb" for examples using .csv files in this Github Repo. These test cases (example users and scholarly topics) are fully described in "DOC/design.md"

If you want to see more code, you may clone this repository and run it using the virtual environment above. 

### How Can I Cite SciPop? ###  

<insert this citation later>

### How Do I Ask A Question For The Developers? ###  

To ask a question or if you encounter an error, please click the "Issues" tab above and ask your question and we will get back to you within a reasonable amount of time.





