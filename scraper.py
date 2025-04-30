import requests
from bs4 import BeautifulSoup
from xlwt import Workbook

# Initialize Excel workbook and sheet
wb = Workbook()
sheet = wb.add_sheet('Leads')

# Step 1: Get all state-level directory links
states = []
base_url = "https://example.com/"  # Replace with actual target domain if allowed
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')
state_links = soup.find_all('a', class_="Directory-listLink")

for link in state_links:
    states.append(link['href'])

# Step 2: Collect all sub-links under each state
all_links = []
for state in states:
    url = f"https://example.com{state}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    sub_links = soup.find_all('a', class_="Directory-listLink")
    all_links.extend([link['href'] for link in sub_links])

# Step 3: Scrape contact information
row = 0
for path in all_links:
    if '.html' in path:
        url = f"https://example.com/{path.split('/')[-1]}"
        name_class = "Hero-name"
        phone_class = "Core-phoneText"
    else:
        url = f"https://example.com/usa{path.split('/usa')[-1]}/"
        name_class = "Teaser-name"
        phone_class = "Teaser-phoneText"

    print(f"Scraping: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    names = soup.find_all('span', class_=name_class)
    phones = soup.find_all('span', class_=phone_class)

    for name, phone in zip(names, phones):
        sheet.write(row, 0, url)
        sheet.write(row, 1, phone.text.strip())
        sheet.write(row, 2, name.text.strip())
        row += 1

# Step 4: Save output
wb.save("leads_output.xls")
print("✅ Lead scraping complete. Data saved to leads_output.xls")
