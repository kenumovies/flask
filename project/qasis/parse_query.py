from textblob import TextBlob as tb
from nltk import PorterStemmer
from textblob import Word

#takes a string as a query, returns list of keywords
def parseQuery(q):

	blob = tb(q.lower())
	posTags = blob.tags
	keepTags = ['NNP', 'NNPS', 'NN', 'NNS', 'JJ', 'JJR', 'JJS', 'CD']
	stems = [w[0].encode('utf-8') for w in posTags if w[1] in keepTags]
	stems = [PorterStemmer().stem_word(w[0].encode('utf-8')) for w in posTags if w[1] in keepTags]
	#stemTemp = keywords
	#add wordnet
	# for s in stemTemp:
	# 	tmpWord = Word(s)
	# 	stems.append(s)
	# 	try:
	# 		synSetTop = tmpWord.synsets[0]
	# 		if len(synSetTop) > 0:
	# 			stems.extend(synSetTop.lemma_names())
			
	# 	except:
	# 		t = 0
	
	#for i in range(len(stems)):
	#	stems[i] = PorterStemmer().stem_word(stems[i])
	return stems

