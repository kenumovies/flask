from tfidf_scores import *
from make_corpus import *
from parse_query import *
from db_access import *


#take string query, return list of tuples
def qasis_main(q, actorList, directorList):
	#get keywords
	kw = parseQuery(q)
	#get docs (for now, ignore actors and directors)
	docs = query_db("SELECT imdb_id, word_list FROM preprocessed_movies;")
	return rankDocs(kw, docs)