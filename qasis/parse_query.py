from textblob import TextBlob as tb
from nltk import PorterStemmer

#takes a string as a query, returns list of keywords
def parseQuery(q):
	blob = tb(q.lower())
	posTags = blob.tags
	keepTags = ['NNP', 'NNPS', 'NN', 'NNS', 'JJ', 'JJR', 'JJS', 'CD']
	keywords = [w[0] for w in posTags if w[1] in keepTags]
	stems = keywords
	for i in range(len(stems)):
		stems[i] = PorterStemmer().stem_word(stems[i]).encode('utf-8')
	return stems

