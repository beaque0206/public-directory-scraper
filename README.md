# 🕵️ Lead Scraper with Python & BeautifulSoup

This project demonstrates how to build a Python script that scrapes public contact information from a structured directory-style website and exports the data to an Excel spreadsheet.

> ⚠️ **Disclaimer**:  
> This script is provided for **educational purposes only**.  
> Users are responsible for ensuring that any use of this code complies with applicable laws, website Terms of Service, and robots.txt policies. Use responsibly.

---

## 📌 What the Script Does

- Navigates a multilevel business directory (e.g., by state and city)
- Extracts:
  - name
  - Phone number
  - Source URL
- Saves results into `leads_output.xls`

---

## 🧰 Technologies Used

- Python 3
- [`requests`](https://pypi.org/project/requests/) – for HTTP requests
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) – for HTML parsing
- [`xlwt`](https://pypi.org/project/xlwt/) – for writing Excel files

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Make sure the target website allows scraping.
3. Run the script
   ```bash
   python scraper.py

## 📁 Output

-Generates `leads_output.xls`

## 💼 Use Cases

- Internal lead generation
- Web scraping practice
- Automating structured data extraction from public web pages

## ✅ Reminder
Always respect:
- The website's robots.txt file
- The site's Terms and Conditions
- Ethical use of any collected data (e.g., no spamming or resale)
