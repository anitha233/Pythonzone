import re

text = "The quick brown fox is tripped over white dog"
pattern = r"brown"

replacement = "red"
new_text = re.sub(pattern,replacement,text)
print("Modified text:", new_text)