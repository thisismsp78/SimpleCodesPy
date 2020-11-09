# Regex
# REGular EXpression

import re

pattern = r'123'
content = '(123sepehr'

res = re.search(pattern, content)
print(res)
print(res.group())
