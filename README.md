# jobsBgAnalyzer
A script that goes through each IT category in jobs.bg and returns useful data that can later be used fo vizualzation.

The program begins by doing an HTTP request and returns an HTML document. By using the BeautifulSoup library, we parse through the document and grab data. The program grabs skills, sections and salaries of each listing by default.

For each IT category, we get back an independent .csv  with skills and salaries.

## Setup
Make sure you have the pip package manager. Install BeautifulSoup, Requests, Pandas and lxml:

```
pip install BeautifulSoup4
pip install requests
pip install pandas
pip install lxml
```
If you want to create simple vizualizations with your data, ```pip install jupyter notebook```.
