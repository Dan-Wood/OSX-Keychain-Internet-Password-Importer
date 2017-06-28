import csv, os, re
#from urllib.parse import urlsplit  # Python 3
from urlparse import urlsplit  # Python 2

#Keep a count of our passwords
count = 0

#CSV file to load
csvFile = 'example_google_password_list.csv'

#Open the CSV file, loop through each line and run the add-internet-password command
with open(csvFile) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:

        url = False
        username = False
        password = False

        if row['url'] :
            website = urlsplit(row['url'])
            website = re.escape(website.netloc)

        if row['username'] : username = re.escape(row['username'])
        if row['password'] : password = re.escape(row['password'])



        if username and password and website :
            os.system("security add-internet-password -U -s " + website + " -a " + username + " -w " + password + " -T /Applications/Safari.app -r http")
            count += 1

print "Total of", count, "passwords, either inserted or updated."