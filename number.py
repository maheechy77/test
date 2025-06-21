import requests
from bs4 import BeautifulSoup
import re

def get_google_doc_content(doc_url):
    html_response = requests.get(doc_url)
    soup = BeautifulSoup(html_response.text, 'html.parser')
    table = soup.find('table')
    return  str(table)

    # Split into lines and skip header
    lines = doc_text.split('/tr')
    for line in lines[1:]:  # skip header line
        temp = line.split('<span class="c')
        for fast in temp:
            if not fast[3].isalpha():
                grid_data.append(fast[3])    
    return grid_data

def build_and_print_grid(grid_data):
    # Convert to list of (x, y, char)
    triplets = [(int(grid_data[i]), grid_data[i+1],int(grid_data[i+2])) for i in range(0, len(grid_data), 3)]

    # Find grid size
    max_x = max(t[0] for t in triplets)
    max_y = max(t[2] for t in triplets)

    print(triplets)
    # Initialize grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    # Fill grid
    for x,char,y in triplets:
        grid[y][x] = char

    # Print grid
    for row in grid[::-1]:
        print(''.join(row))
        #print("\n")

def display_unicode_grid_from_doc(doc_url):
    doc_text = get_google_doc_content(doc_url)
    grid_data = parse_unicode_grid(doc_text)
    build_and_print_grid(grid_data)

# Example:
doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"  # Replace this with your document URL
display_unicode_grid_from_doc(doc_url)
