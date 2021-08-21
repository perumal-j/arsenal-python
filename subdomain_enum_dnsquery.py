from dns.exception import DNSException
import pyfiglet
import dns.resolver

ascii_banner=pyfiglet.figlet_format("Subdomain Enumeration")
print(ascii_banner)

domain=input("Enter the domain to enumerate:")
sub_list=input("Enter the subdomain list(with path):")
list=open(sub_list).read()
content=list.splitlines()

for sub in content:
    req=f"{sub}.{domain}"
    try:
        dns.resolver.resolve(req)
    except DNSException as e:
        print("Invalid Domain")
    else:
        print("Valid Subdomain Found:",req)