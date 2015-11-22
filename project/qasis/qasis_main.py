from tfidf_scores import *
from make_corpus import *
from parse_query import *
from db_access import *


#take string query, return list of tuples
def qasis_main(q, actorList, directorList):
	#get keywords
	kw = parseQuery(q)
	#get docs (for now, ignore actors and directors)
	
	sqlQuery = """
				SELECT 
					pm.imdb_id, 
					pm.word_list,
					m.title,
					m.year,
					m.rating,
					m.released,
					m.runtime,
					m.genre,
					m.plot,
					m.language,
					m.country,
					m.awards,
					m.poster,
					m.metascore
				FROM 
					preprocessed_movies pm
					NATURAL INNER JOIN movies m
				;"""
	docs = query_db(sqlQuery)
	return rankDocs(kw, docs)