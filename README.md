# jobsBgAnalyzer
A script that goes through each IT category in jobs.bg and returns a data set helpful to job seekers and those interested in seeing trends in skills and salaries in the Bulgarian IT field.

The program begins by doing an HTTP request and returns an HTML document. By using the BeautifulSoup library, we parse through the document and grab data. In the case here, the program grabs skills, sections and salaries of each listing by default.

For each IT category, we get back an independent .csv  with skills and salaries.

## Usage
The script can be used in sequence with pandas library and jupyter notebook for visualization.
