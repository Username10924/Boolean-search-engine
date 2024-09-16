import nltk
import json
import time
news = []

# Load json into news
data = [json.loads(line) for line in open('news.json', 'r')]
for line in data:
    headline = line['headline']
    body = line['short_description']
    authors = line['authors']
    text = headline + " " + body + " " + authors
    news.append(text)

terms = dict()
def create_index(corpus):
    for doc in corpus:
        for word in nltk.word_tokenize(doc):
            if(word.lower() in terms):
                terms[word.lower()].add(doc)
            else:
                terms[word.lower()] = {doc}
create_index(news)

start = time.time()
result = terms["america"]
end = time.time()
print((end - start)*10**6)
for doc in result:
    print(doc + "\n\n")