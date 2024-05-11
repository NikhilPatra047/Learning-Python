from requests import get
from sys import argv, exit
from json import dumps

if len(argv) != 2:
    exit("You didn't provide any terms. Please provide one.")

response = get(f"https://itunes.apple.com/search?entity=song&limit=50&term={argv[1]}")
print(dumps(response.json(), indent=4))

o = response.json()
for result in o["results"]:
    print(result["trackName"])
