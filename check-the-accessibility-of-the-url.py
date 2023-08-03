
# https://docs.python.org/3/library/itertools.html

import itertools
import requests

def generate_combinations(string_to_concat):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    combinations = list(itertools.combinations(letters, 3))
    results = []

    for combination in combinations:
        result = string_to_concat + ''.join(combination)
        results.append(result)

    return results

def check_urls(urls, output_file):
    with open(output_file, "w") as file:
        for url in urls:
            response = requests.get(url)
            if response.status_code == 404:
                file.write(f"{url} returned a 404 status code.\n")

# Generate combinations
string_to_concat = "http://github.com/"
combinations = generate_combinations(string_to_concat)

# Check URLs for 404 status code and save output to a file
output_file = "output.txt"
check_urls(combinations, output_file)

