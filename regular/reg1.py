import re

text = "hi my name is hariprasath"
pattern = "hariprasath"
result = re.search(pattern, text)

if result:
    print("match found")