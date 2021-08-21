import pyfiglet
import requests

ascii_banner=pyfiglet.figlet_format("Subdomain Enumeration")
print(ascii_banner)

domain=input("Enter the domain to enumerate:")
sub_list=input("Enter the subdomain list(with path):")
list=open(sub_list).read()
content=list.splitlines()

for sub in content:
    req=f"https://{sub}.{domain}"
    try:
        requests.get(req)
    except requests.ConnectionError:
        print("Invalid Domain")
    else:
        print("Valid Subdomain Found:",req)


     