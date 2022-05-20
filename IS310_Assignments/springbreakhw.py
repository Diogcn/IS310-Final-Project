# Step 1:
from bs4 import BeautifulSoup
import requests

with open('updated_raw_text_script_urls.txt') as input_file:
    lines = input_file.readlines()

url_list = []
named_list = []

for line in lines:
    tnamed_list = line.split(" +++$+++ ")
    url_list.append(tnamed_list[2].strip())
    named_list.append(tnamed_list[1])

# Step 2:
def scrape_webpage(url):
    response = requests.get(url)
    html_string = response.text
    return html_string

for i in range(len(url_list)):
    scrapethis = scrape_webpage(url_list[i])
    soup = BeautifulSoup(towrite, "html.parser")
    fname = named_list[i] + '.txt'
    with open(fname, 'w') as f:
        f.write(soup.text)

# Note: I just want to say that I want to credit Leo as the main
# reference as his formatting for this assignment is extremely clean. Although
# I do try to code this in a format that I would normally do.
