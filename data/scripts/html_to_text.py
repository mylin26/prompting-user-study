from bs4 import BeautifulSoup
import json

html_code_filepath = './data/scripts/raw_html.html'
html_code_open = open(html_code_filepath, 'r', encoding="UTF-8")
html_code = html_code_open.read()

# Parse the HTML
soup = BeautifulSoup(html_code, 'html.parser')

# Find the div with id "event-models" and class "webdsl-placeholder"
event_models_div = soup.find('div', id='event-modals', class_='webdsl-placeholder')

# Extract all tags with the class "appended"
appended_tags = event_models_div.find_all('span', class_='appended')

json_array = []

# Print each of the extracted tags
for idx, tag in enumerate(appended_tags):
    soup2 = BeautifulSoup(str(tag), 'html.parser')

    # Extract the title
    title = soup2.find('h4').get_text(strip=True)

    # Extract the topics (if available)
    topics = soup2.find('p', class_='text-muted').get_text(strip=True)

    # Extract the abstract (if available)
    abstract = soup2.find('div', class_='bg-info event-description').find('p', class_=False).get_text(strip=True)

    # Extract the paper link (if available)
    paper_link_tag = soup2.find('span', class_='pull-left').find('a')
    paper_link = paper_link_tag['href'] if paper_link_tag else None

    # Extract the authors
    authors = [author.get_text(strip=True) for author in soup2.find_all('h5', class_='media-heading')]

    # Extract the allocated time
    time_info = soup2.find('strong').get_text(strip=True).replace('atMeeting', 'at Meeting').replace('atOffsite', 'at Offsite')
    arr = time_info.split(" at ")
    time_info = arr[0]
    location_info = arr[1]

    # Put the extracted information in a JSON object
    json_element = {
        "title": title,
        "topics": topics,
        "abstract": abstract,
        "paperLink": paper_link,
        "authors": authors,
        "allocatedTime": time_info,
        "location": location_info
    }

    json_array.append(json_element)

output_file = open("msr-2023.json", 'w')
json.dump(json_array, output_file, indent=4)