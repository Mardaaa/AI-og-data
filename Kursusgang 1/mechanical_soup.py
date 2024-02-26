import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)
# print(page)
# print(type(page.soup))
# print(page.soup)

############### Log in ####################
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0] # Returns a list of all <form> elements
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)
print(profiles_page.url)

####################### Obtain URL for each link ########
links = profiles_page.soup.select("a")
for link in links:
    address = link["href"]
    text = link.text
    print(f"{text}: {address}")

################# Exercises ###############
print(profiles_page.soup.title)


######## INTERACT WITH WEBSITES IN REAL TIME ############
url = "http://olympus.realpython.org/dice"
page = browser.get(url)
# print(page.soup)
tag = page.soup.select("#result")[0]
# print(tag.text) # Number the dice has rolled
result = tag.text
print(f"The result of the dice roll is: {result}")


###### Time interval #####
import time

for i in range(4):
    page = browser.get(url)
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of the dice roll is: {result}")
    
    if i < 3:
        time.sleep(10) # New result pr. 10 seconds