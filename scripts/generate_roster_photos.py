from helpers import Student
import requests
import json
import csv
import time

cookies = []

with open("internal_data/browser_cookies.json", "r") as f:
    cookies = json.load(f)

session = requests.Session()

for cookie in cookies:
    session.cookies.set_cookie(requests.cookies.create_cookie(name=cookie['name'], value=cookie['value'], domain=cookie.get('domain')))

print(session.cookies)

stu_ids = []

with open('internal_data/roster.csv', 'r') as in_file:
    reader = csv.reader(in_file, delimiter=',')
    next(reader)
    for line in reader:
        line = Student(line)
        stu_ids.append(line.num_id)

for id in stu_ids:
    # Use the session for a request
    response = session.get(f"https://www.reg.uci.edu/perl/StuPhoto.pl?stuid={id}&coursecode=35920&termyyyyst=202492")

    if response.status_code == 200:
        # Save the image content to a file
        with open(f"internal_data/photos/id{id}.jfif", "wb") as f:
            f.write(response.content)
        print("Image downloaded successfully!")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
    
    time.sleep(1)