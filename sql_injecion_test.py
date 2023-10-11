import requests

# Define a function to check SQL injection vulnerabilities
def check_sql_injection_vulnerability(url):
    modified_url = url.replace("FUZZ", "FUZZ'")
    response = requests.get(modified_url)
    if "You have a syntax error" in response.text:
        return "\033[32mPotential SQL injection vulnerability found\033[0m"  # Green text
    else:
        return "No SQL injection vulnerability found"

# Specify the file containing the list of URLs
params_file = "params.txt"

# Read URLs from the file and test for vulnerabilities
with open(params_file, "r") as file:
    for line in file:
        url = line.strip()  # Remove trailing newline character
        result = check_sql_injection_vulnerability(url)
        print(f"URL: {url}\nResult: {result}\n")
