# jobsBgAnalyzer
A script that goes through each IT category in jobs.bg and returns data that could be help job seekers and those interested in seeing trends in skills and salaries from the Bulgarian IT market.

The program begins by doing an HTTP request and returns an HTML document. By using the BeautifulSoup library, we parse through the document and grab data. In the case here, the program grabs skills, sections and salaries of each listing by default.

For each IT category, we get back an independent .csv  with skills and salaries.

## Setup
Make sure you have the pip package manager from which you'll have to get BeautifulSoup, Requests, Pandas and lxml

If you're unsure or don't know how to install, follow the steps:
```
pip install BeautifulSoup4
pip install requests
pip install pandas
pip install lxml
```
If you want to see the data, ```pip install jupyter notebook``` and use that for simple visualizations.
