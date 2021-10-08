# jobsBgAnalyzer
A script that goes through each IT category in jobs.bg and returns a data set that could be helpful to job seekers and those interested in seeing trends in skills and salaries in the Bulgarian IT field.

Theprogram begins by doing an HTTP request and returns an HTML document. By using the BeautifulSoup library, we parse through the document and grab data. In this case, the program grabs skills, sections and salaries of each listing.

For each IT category, we get back an independent .csv  with skills and salaries.

## Usage
The script can be used in sequence with the pandas library and jupyter notebook for simple visualization. It is helpful to create data driven decisions and goals.
