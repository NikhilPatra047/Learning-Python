import re

url = "http://twitter.com/davidjmalan"
pattern = r"^https?://(?:www\.)?twitter\.com/(.+)$"
# username = re.sub(pattern, "", url)
# print(username)
matches = re.search(pattern, url, re.IGNORECASE)
if matches:
    print(matches.group(1))

# focus on incremental developmental changes over changes all at once.
# Building one new feature at a time
