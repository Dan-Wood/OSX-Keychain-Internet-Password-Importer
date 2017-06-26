import csv, os

#Keep a count of our passwords
count = 0

#CSV file to load
csvFile = 'example_password_list.csv'

#Open the CSV file, loop through each line and run the add-internet-password command
with open(csvFile) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        website = row['website']
        username = row['username']
        password = row['password']

        if username and password and website :
            os.system("security add-internet-password -U -s " + website + " -a " + username + " -w " + password)
            count += 1

print "Total of", count, "passwords, either inserted or updated."