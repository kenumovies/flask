from textblob import TextBlob as tb
import psycopg2
from nltk.corpus import stopwords
from nltk import PorterStemmer

import db_access

#takes list of tuples, returns dictionary of textblobs
def preprocessAll():
	db_access.exec_db("DROP TABLE IF EXISTS preprocessed_movies;")
	db_access.exec_db("CREATE TABLE preprocessed_movies(imdb_id TEXT PRIMARY KEY,word_list TEXT);")

	sw = stopwords.words("english")
	
	docs = db_access.query_db('SELECT imdb_id, plot FROM movies;')

	ctr = 0
	for d in docs:
		cleanPlot = preprocess(d[1].decode('utf-8'),sw)
		db_access.insert_db('preprocessed_movies', [str(d[0]), cleanPlot])
		print ctr
		ctr = ctr + 1
	

def preprocess(doc, stopwordList):
	blob = tb(doc.lower())
	blobWords = blob.words
	blobNoStop = [w for w in blobWords if w not in stopwordList]
	stems = blobNoStop
	for i in range(len(stems)):
		stems[i] = PorterStemmer().stem_word(stems[i])
	clean = " ".join(stems)
	return clean

