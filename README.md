I used Beautiful soup, a Python Library to scrap data from IMBD.

I parsed the HTML file and extracted and scrapped texts namely:
-Movie title
-Movie date
-Movie rating
-Movie Rank

I ran the code and saved it as an Excel file for further editing and formatting.

I formatted the borders of the excel cells to fit in data and used Find & Replace to remove the brackets () in the Date column.

I then saved it as a CSV file and imported it as a table on MySQL Workbench.
I used SQL queries to extract the Top 10 ranked Movies in the year 2000 below and 2000 above and sorted them by their ratings.
So, we can tell which century has the most rated movies
