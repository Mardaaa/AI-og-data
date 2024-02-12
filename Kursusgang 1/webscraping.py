from urllib.request import urlopen

#################Build your first web scraper########

# Define URL
def extract_html(url):
    # Open web page
    page = urlopen(url)
    # print(page) # Uncomment to see

    # Extract the HTML from the page
    html_bytes = page.read() # Read the object
    html = html_bytes.decode("utf-8") # Decode the object
    # print(html) # Prints the HTML code of the website
    return html


########## Extract text from HTML with String Methods #################
def find_title(html):
    # Find index of <title>
    title_index = html.find("<title>")

    # Find index of the title itself
    start_index = title_index + len("<title>")

    # Find index of the closing </title>
    end_index = html.find("</title>")

    # Extract the title by slicing the html string
    title = html[start_index:end_index]
    print(title)

# find_title()
url_1 = "http://olympus.realpython.org/profiles/aphrodite"
url_2 = "http://olympus.realpython.org/profiles/poseidon"
    # url_2 has a bit of HTML mixed in the title
    # This is because the opening <title > has a space before the closing bracket
        # This results in html.find("<title>") returns -1, since the exact substring doesn't exist
  
# Call functions
# html = extract_html(url_2)
# find_title(html)


################### Regular Expressions ####################
import re

# Find any text within a string that matches a given regular expression
    # Use "*"
# print(re.findall("ab*c", "ac"))
    # First string: The regular expression that you want to match
    # Second string: String to test
    # You search for the pattern "ab*c" in the string "ac"

# Examples
# re.findall("ab*c", "abcd")
# ['abc']

# re.findall("ab*c", "acc")
# ['ac']

# re.findall("ab*c", "abcac")
# ['abc', 'ac']

# re.findall("ab*c", "abdc")
# []

# Case sensitivity
# re.findall("ab*c", "ABC")
# []

# re.findall("ab*c", "ABC", re.IGNORECASE)
# ['ABC']

# group()-method: Return the first and most inclusive result
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
# print(match_results.group())

# sub()-method: Substitute text in a string
string = "Everything is <replaced> if it's in <tags>"
# string = re.sub("<.*>", "ELEPHANTS", string) # Greedy way
string = re.sub("<.*?>", "ELEPHANTS", string) # non-greedy way
# print(string)


########## Extract text from HTML with Regular Expressions ########
url_3 = "http://olympus.realpython.org/profiles/dionysus"
html = extract_html(url_3)

# Find title
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
print(title) # Output: <TITLE >Profile: Dionysus</title  / >

title = re.sub("<.*?>", "", title) # Remove HTML tags
print(title) # Output: Profile: Dionysus


######## Exercises ####################
# Write a program that grabs the full HTML from the following URL:
url = "http://olympus.realpython.org/profiles/dionysus"
# Then use .find() to display the text following Name: and 
# Favorite Color: (not including any leading spaces or trailing HTML 
# that might appear on the same line).
html = extract_html(url)
print(html)

for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)



