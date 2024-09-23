import re

text = "The wild fox in the forest"
pattern = r"the"

search = re.search(pattern,text)
if search:
    print("Pattern found:",search.group())
else:
    print("Pattern not found")    