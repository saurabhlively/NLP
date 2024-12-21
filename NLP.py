import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

english_stopwords=stopwords.words("english")
#print(english_stopwords)

#Load the book

with open('miracle_in_the_andes.txt','r',encoding='utf-8') as file:
    book=file.read()

# print(book)

#How many chapters
#(a) With String methods

#print(book.count("Chapter"))
#Above count is not accurate

#(b) With regular expressions or regex
pattern = re.compile("Chapter [0-9]+")
findings = re.findall (pattern,book)
#print(len(findings))

#Which are the sentences where love word is used
#+ -- 1 or more , * -- zero or more
pattern = re.compile("[a-zA-Z ,]* love [a-zA-Z]*")
pattern1 = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings=re.findall(pattern1,book)
#print(findings)

#Most used words
pattern=re.compile("[a-zA-Z]+")
findings=re.findall(pattern,book.lower())

dict={}
for word in findings:
    if word in dict.keys():
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1
#print(dict)
dict_list = [(value,key) for (key,value) in dict.items()]
sort_list = sorted(dict_list,reverse=True)
#print(sort_list[:5])

#this code will filterout most common used words via stopwords
filtered_words=[]
for count,word in sort_list:
    if word not in english_stopwords:
        filtered_words.append((word,count))

#print(filtered_words)

#Sentiment analysis of positive/negative chapters
#Most positive and most negative chapters

analyzer = SentimentIntensityAnalyzer()
scores=analyzer.polarity_scores("book")
if scores["pos"] > scores["neg"]:
    print("Its a positive text")
else:
    print("Its a negative text")

#print(scores)

#Chapter sentiment Analysis
pattern =re.compile("Chapter [0-9]+")
chapters = re.split(pattern,book)
chapters = chapters[1:]
for nr,chapter in enumerate(chapters):
    scores=analyzer.polarity_scores(chapter)
    print(nr + 1,scores)





