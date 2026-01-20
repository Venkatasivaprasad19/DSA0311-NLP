import re
text = "my email id is student123@gmail.com"
pattern = r'\w+@\w+\.\w+'
match=re.search(pattern,text)
if match:
    print("match found:",match.group())
else:
    print("match not found")