import csv
import requests

# Read lines from a text file
def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Make a GET request and return status, response, and URL
def make_get_request(url):
    response = requests.get(url)
    return {
        'url': url,
        'status_code': response.status_code
        # 'response': response.text
    }

def add_paremeter_if_needed(url):
    # if {id} is in the URL, add a parameter
    if '{id}' in url:
        url = url.format(id=1)
    return url

# Main function
def main():
    input_file = 'urls.txt'
    output_file = 'results.csv'

    urls = read_lines_from_file(input_file)
    
    results = []


    for url in urls:
        url = add_paremeter_if_needed(url)
        result = make_get_request(url)
        results.append(result)

    # Write results to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['url', 'status_code']
        # fieldnames = ['url', 'status_code', 'response']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

if __name__ == '__main__':
    main()
