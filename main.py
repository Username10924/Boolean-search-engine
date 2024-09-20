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

# create inverse index using dictionary
# where every term will map to a set of documents its in
index = dict()
# --one time execution--
def create_index(corpus):
    for doc in corpus:
        for word in nltk.word_tokenize(doc):
            if(word.lower() in index):
                index[word.lower()].add(doc)
            else:
                index[word.lower()] = {doc}
create_index(news)
# all results now saved in index

def boolean_search(query, index):
    results = set()
    wordList = query.split()
    for word in wordList:
        if('&' in word):
            words = word.split('&')
            # must use format .get(word, set()) instead of .get(word) or it just returns 'set()'
            # or index[word] but this returns an exception if word is not in index
            intersectedWords = index.get(words[0], set())
            for i in words:
                intersectedWords = intersectedWords.intersection(index.get(i, set()))
            results.update(intersectedWords)
        else:
            results.update(index.get(word, set()))
    if(results):
        return list(results)
    else:
        return ["No results found!"]

def startApp():
    query = input("Search: ")
    start = time.time()
    results = boolean_search(query, index)
    end = time.time()
    i = 0
    for result in results:
        print(result)
        print()
        i += 1
    print("Time in ms: ")
    print((end - start)*10**6)
    print("Total results: ")
    print(i)

while(1):
    startApp()