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
	sumS = 0
	for kw in keywordList:
		sumS = sumS + tfidf(kw, doc, doclist)
	return sumS

def buildDict(movie):
	return {
		'imdb_id':movie[0],
		'title':movie[2],
		'year':movie[3],
		'rating':movie[4],
		'released':movie[5],
		'runtime':movie[6],
		'genre':movie[7],
		'plot':movie[8],
		'language':movie[9],
		'country':movie[10],
		'awards':movie[11],
		'poster':movie[12],
		'metascore':movie[13]
	}

def rankDocs(keywordList, doclistTuples):

	scores = {}
	docList = [tb(doc[1].decode('utf-8')) for doc in doclistTuples]
	
	kwIDFs = {}
	for w in keywordList:
		kwIDFs[w] = idf(w, docList)

	for doc in doclistTuples:
		text = tb(doc[1].decode('utf-8'))
		sumS = 0
		for w in keywordList:
			sumS = sumS + (tf(w,text)*kwIDFs[w])
		scores[doc[0]] = {'score': sumS, 'object': buildDict(doc)}

		#scores[doc[0]] = scoreDoc(keywordList, tb(doc[1].decode('utf-8')), docList)

	
	sortedDocs = sorted(scores.items(), key=lambda x: x[1]['score'], reverse = True)

	return sortedDocs[:24]