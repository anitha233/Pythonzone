import re

text = "apple,orange,banana,grapes"
pattern = r","

new_text = re.split(pattern,text)
print("Splitted text:",new_text)