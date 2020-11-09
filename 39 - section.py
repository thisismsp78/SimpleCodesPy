# Regex

import re


# pattern = r'\w+\s\w+'
# pattern = r'[\w\s?\W?]+'
pattern = r'[A-Za-z0-9-]+'
# content = 'firstname lastname nick$name'
content = 'sEpeHr-akbarzadeh-abkenar-100'

res = re.search(pattern, content)

print(res.group())