import re

text = "The quick wild fox"
pattern = r"quick"

match = re.match(pattern,text)
if match:
    print("Match found:",match.group())
else:
    print("No Match")    