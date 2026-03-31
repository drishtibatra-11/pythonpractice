import re
pattern= r'\d+'
text ='abc123'
match = re.search(pattern, text)
print(match.group())