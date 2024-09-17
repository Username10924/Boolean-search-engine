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
            word1 = word.split('&')[0]
            word2 = word.split('&')[1]
            results.update(index[word1].intersection(index[word2]))
        else:
            results.update(index[word])
    return list(results)

start = time.time()
print(boolean_search("china&collapse saudi", index))
end = time.time()
print((end - start)*10**6)


# alpha = {"a", "b", "c"}
# beta = {"b", "a"}
# gamma = alpha.intersection(beta)
# print(gamma)