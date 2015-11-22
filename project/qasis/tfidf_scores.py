import math
from textblob import TextBlob as tb

def tf(word, blob):
	return float(blob.words.count(word)) / len(blob.words)

def n_containing(word, bloblist):
	return float(sum(1 for blob in bloblist if word in blob))

def idf(word, bloblist):
    return float(math.log(len(bloblist) / (1 + n_containing(word, bloblist))))

def tfidf(word, blob, bloblist):
    return float(tf(word, blob) * idf(word, bloblist))

def scoreDoc(keywordList, doc, doclist):
	sum = 0
	for kw in keywordList:
		sum = sum + tfidf(kw, doc, doclist)
	return sum

def rankDocs(keywordList, doclistTuples):
	scores = {}
	docList = [tb(doc[1].decode('utf-8')) for doc in doclistTuples]
	for doc in doclistTuples:
		scores[doc[0]] = scoreDoc(keywordList, tb(doc[1].decode('utf-8')), docList)

	sortedDocs = sorted(scores.items(), key=lambda x: x[1], reverse = True)
	return sortedDocs[:10]