# Qasis
Created by Shlok Amin, Nikhil Pai, Nick Paras

Qasis allows a user to search for movies based on a natural language query of the plot. We use an information-retrieval algorithm by parsing keywords from the query, calculating Term-Frequency, Inverse-Document-Frequency scores for each of the movie synopses, and ranking by their relevance.

### Sample queries:
* family of superheroes fights a redheaded villain
* farm boy battles the empire
* kid from coal mining town builds a rocket

Should return:
* The Incredibles
* Star Wars
* October Sky

## Architecture:
The top 1000 movies were scraped from IMDB using kimono lab's scraping tool and OMDB. These were then loaded into a Postres database and preprocessed. An information-retrieval algorithm then parsed keywords from the query, calculated Term-Frequency, Inverse-Document-Frequency scores for each of the movie synopses, and ranked by their relevance. A jQuery interface then rendered this data for the end user.

### Technologies:
* Flask
* Postgres
* NLTK
* Kimono Labs
* SASS
* Handlebars
* jQuery
* Gulp
