import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# URL for main genre page. Only works with IMSDB links
url = "https://imsdb.com/genre/Action"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links = soup.find_all('a')

# Regex pattern
regex_pattern = r"Insert your regex pattern here"

results = []

for link in links:
    href = link.get('href')
    if href:
        if href.startswith('/'):
            full_url = "https://imsdb.com" + href
        else:
            full_url = href

        try:
            response = requests.get(full_url)
        except requests.exceptions.RequestException as e:
            continue

        soup = BeautifulSoup(response.content, "html.parser")
        page_links = soup.find_all('a')

        for page_link in page_links:
            if page_link.text.startswith("Read ") and page_link.text.endswith(" Script"):
                script_link = page_link.get('href')
                if script_link:
                    try:
                        script_response = requests.get("https://imsdb.com" + script_link)
                        script_soup = BeautifulSoup(script_response.content, "html.parser")
                        script_text = script_soup.find('pre')
                        if script_text:
                            text = script_text.text.lower()

                            regex_instances = re.findall(regex_pattern, text, flags=re.IGNORECASE)

                            regex_count = len(regex_instances)

                            results.append([script_link.split('/')[-1], regex_count, ", ".join(regex_instances)])


                    except requests.exceptions.RequestException as e:
                        continue

# Write to excel
df = pd.DataFrame(results, columns=['Script Name', 'Words Tracked', 'Instaces of Words Tracked'])

# Replace with your file location
df.to_excel(r'Your file location here', index=False)

print("Excel file created with script name, words tracked count, and instances of words tracked.")
