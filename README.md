# IMSDB-Regex-Search-Tool
Simple tool to help search IMSDB movie script database using regex

Background:
I wrote this code while working on a linguistics research project tracking expletive infixation, using the IMSDB movie script database. While the code is simple, it was a little difficult to get it so that the program would recognize which links were valid on the IMSDB page, and which weren't. Hopefully this helps.

Prerequisites:
Python 3.6 or later 
BeautifulSoup4 
Requests 
Pandas

Usage:
Set the url page to the IMSDB genre page you are interested in, insert your regex pattern into the regex_pattern variable, and update the file location in the df.to.excel method to specify where you would like the file to be saved to.

