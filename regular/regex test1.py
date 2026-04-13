import re

text = "hari,hariiii"
result = re.findall("har*i", text)
print(result)