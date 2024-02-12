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
