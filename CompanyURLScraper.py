import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import random
from fake_useragent import UserAgent
import openpyxl
from requests_ip_rotator import ApiGateway

# Function to search for company URL using Google (with added precautions)
def search_company_url(company_name, proxies):
    search_query = f"{company_name} official website"
    
    # Rotate User-Agent to simulate different users
    user_agent = UserAgent().random
    headers = {
        'User-Agent': user_agent,
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

    # Random delay to bypass spam protection
    time.sleep(random.uniform(3, 6))  # Random delay between 3 and 6 seconds
    
    try:
        # Using Proxy Rotation with requests_ip_rotator
        gateway = ApiGateway('https://www.google.com/search', proxies)
        
        # Send a request to Google search (with proxy)
        response = requests.get(f"https://www.google.com/search?q={search_query}", headers=headers, proxies=gateway.get_proxy())
        
        # Check if the response is successful
        if response.status_code != 200:
            print(f"Error: Unable to fetch results for {company_name}")
            return None
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the first URL from the search results
        search_results = soup.find_all('a', href=True)
        for link in search_results:
            href = link['href']
            if 'url?q=' in href:
                url = href.split('url?q=')[1].split('&')[0]
                return url
        
        print(f"No valid URL found for {company_name}")
        return None
    
    except Exception as e:
        print(f"Error occurred for {company_name}: {str(e)}")
        return None

# Function to update the Excel file with URLs
def update_excel_with_urls(input_file, output_file):
    # Read the Excel file with company names
    df = pd.read_excel(input_file)
    
    # Ensure the Excel file has a 'Company' column
    if 'Company' not in df.columns:
        print("Error: No 'Company' column found in the Excel file.")
        return
    
    # Initialize a new column for URLs
    df['Website URL'] = None
    
    # Load proxies from a file or use a proxy service like ProxyMesh, ScraperAPI, etc.
    proxies = ['http://proxy1:port', 'http://proxy2:port', 'http://proxy3:port']  # Example proxy list
    
    # Loop through each company name, search for the URL and update the DataFrame
    for index, row in df.iterrows():
        company_name = row['Company']
        print(f"Searching for: {company_name}")
        url = search_company_url(company_name, proxies)
        if url:
            df.at[index, 'Website URL'] = url
        
        # Random delay to simulate human behavior
        time.sleep(random.uniform(5, 10))  # Random delay between 5 and 10 seconds
    
    # Save the updated DataFrame back to an Excel file
    df.to_excel(output_file, index=False)
    print(f"Updated Excel file saved as {output_file}")

# Example usage
input_file = 'companies.xlsx'  # Input Excel file with company names
output_file = 'companies_with_urls.xlsx'  # Output Excel file with company names and URLs

update_excel_with_urls(input_file, output_file)
