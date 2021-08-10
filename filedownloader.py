import requests
url=input("Enter the URL:")
filename=input("Enter the file name:")
r=requests.get(url,allow_redirects=True)
open(filename,'wb').write(r.content)






































#import requests   # Importing Requests library(for web operations)
#url=input("Enter the URL:") # Getting URL of file to be downloaded
#filename=input("Enter the file name:") # Give name to your downloaded file
#r=requests.get(url,allow_redirects=True) # accessing contents of given URL
#open(filename,'wb').write(r.content) # Writing the contents found in a file


