import re

text = "abc axc"
result = re.findall("a.c", text)
print(result)