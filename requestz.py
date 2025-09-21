import requests
import os
from urllib.parse import urlparse
def download_image(url, filename=None):
    # Add headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Make the request with headers
        response = requests.get(url, headers=headers)
        
        # Check if request was successful
        if response.status_code == 200:
            print(f"Successfully downloaded! Status: {response.status_code}")
            
            # If no filename provided, extract from URL
            if not filename:
                parsed_url = urlparse(url)
                filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
            
            # Save the image
            with open(filename, 'wb') as file:
                file.write(response.content)
            
            print(f"Image saved as: {filename}")
            print(f"File size: {len(response.content)} bytes")
            
        else:
            print(f"Error: HTTP {response.status_code}")
            print(f"Response headers: {dict(response.headers)}")
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Get URL from user
url = input("Please enter the image URL: ")

download_image(url)
