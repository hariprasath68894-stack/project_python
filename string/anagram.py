str1 = input("Enter first wrod: ")
str2 = input("Enter secondword: ")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("not Andgram")