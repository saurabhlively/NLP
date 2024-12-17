import re

#Load the book

with open('miracle_in_the_andes.txt','r',encoding='utf-8') as file:
    book=file.read()

# print(book)

#How many chapters
#(a) With String methods

print(book.count("Chapter"))
#Above count is not accurate

#(b) With regular expressions or regex
pattern = re.compile("Chapter [0-9]+")
findings = re.findall (pattern,book)
print(len(findings))

#Which are the sentences where love word is used
#+ -- 1 or more , * -- zero or more
pattern = re.compile("[a-zA-Z ,]* love [a-zA-Z]*")
pattern1 = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings=re.findall(pattern1,book)
print(findings)

#Most used words




