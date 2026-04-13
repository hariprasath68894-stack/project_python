word=input("Entry a word: ")
reverse = ""
i = len(word) - 1
while i >=0:
    revers = reverse + word[i]
    i = i - 1
print("reversed word:" , reverse)
if word == reverse:
    print("palindrome")
else:
    print("not palindrome")