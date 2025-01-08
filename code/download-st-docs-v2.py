import os
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from icecream import ic

# Base URL
base_url = "https://docs.streamlit.io/develop/api-reference"

# Debug flag
debug = True
if debug:
    ic.enable()
else:
    ic.disable()

# Output directory
output_dir = "../data"
os.makedirs(output_dir, exist_ok=True)
if debug:
    ic(output_dir)

# Function to convert HTML to PDF using Playwright
def html_to_pdf(html_content, pdf_file_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            page.set_content(html_content, timeout=60000)  # Increase timeout to 60 seconds
            page.pdf(path=pdf_file_path)
        except Exception as e:
            ic(f"Error processing {pdf_file_path}: {e}")
        finally:
            browser.close()

# Fetch and parse the main page
response = requests.get(base_url)
response.raise_for_status()
if debug:
    ic(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
if debug:
    ic(len(soup))

# Find all sublinks
links = soup.find_all('a', href=True)
if debug:
    ic(len(links))
for link in links:
    href = link['href']
    if href.startswith('/develop/api-reference'):  # Filter relevant links
        subpage_url = f"https://docs.streamlit.io{href}"
        if debug:
            ic(subpage_url)
        sub_response = requests.get(subpage_url)
        sub_response.raise_for_status()
        if debug:
            ic(sub_response.status_code)

        # Save as PDF
        file_name = href.split('/')[-1] or "index"
        pdf_file_path = os.path.join(output_dir, f"{file_name}.pdf")
        if os.path.exists(pdf_file_path):  # Skip if already downloaded
            if debug:
                ic(f"Skipping already downloaded: {pdf_file_path}")
            continue

        if debug:
            ic(pdf_file_path)
        
        # Convert HTML to PDF using Playwright
        html_to_pdf(sub_response.text, pdf_file_path)
        if debug:
            ic(f"Saved {pdf_file_path}")

print(f"Downloaded and converted Streamlit docs to PDF in {output_dir}")
