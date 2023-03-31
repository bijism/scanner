import dns.resolver
import requests
import urllib3
import re

# Prompt the user to enter the domain name
domain = input("Enter the domain name: ")

# Validate the domain name
if not re.match("^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
    print("Invalid domain name.")
    exit()

# Resolve the domain name to its IP addresses
ip_addresses = []
try:
    answers = dns.resolver.resolve(domain, 'A')
    for ip_address in answers:
        ip_addresses.append(str(ip_address))
except dns.resolver.NoAnswer:
    print("Couldn't get IP addresses for the specified domain.")
    exit()

# Scan open ports using nmap and get associated services for each sub-domain
open_ports = {}
for ip_address in ip_addresses:
    # use nmap to scan open ports and get associated services
    # add the results to the open_ports dictionary

# Extract web page contents using requests and Beautiful Soup
web_contents = {}
for sub_domain in open_ports.keys():
    sub_domain_url = "http://" + sub_domain
    try:
        response = requests.get(sub_domain_url)
        soup = BeautifulSoup(response.content)
        title = soup.find('title').text
        web_contents[sub_domain] = {'title': title}
    except requests.exceptions.RequestException:
        web_contents[sub_domain] = {'title': 'N/A'}

# Identify the technologies used by the website using web-scraping libraries
technologies = {}
for sub_domain in web_contents.keys():
    sub_domain_url = "http://" + sub_domain
    try:
        response = requests.get(sub_domain_url)
        wappalyzer = Wappalyzer.latest()
        site = wappalyzer.analyze_with_versions(response)
        technologies[sub_domain] = {'web-framework': ..., 'programming-languages': ..., 'web-servers': ...}  # fill in the blanks
    except requests.exceptions.RequestException:
        technologies[sub_domain] = {'web-framework': 'N/A', 'programming-languages': 'N/A', 'web-servers': 'N/A'}

# Print the results
for sub_domain in open_ports.keys():
    print(f"Sub-Domain: {sub_domain}")
    print(f"IP Address: {ip_address}")
    print(f"Open Ports: {open_ports[sub_domain]}")
    print(f"Title Page: {web_contents[sub_domain]['title']}")
    print(f"Web Servers: {technologies[sub_domain]['web-servers']}")
    print(f"Web-Framework: {technologies[sub_domain]['web-framework']}")
    print(f"Programming languages: {technologies[sub_domain]['programming-languages']}")
    print()

print("Finish - Report")
