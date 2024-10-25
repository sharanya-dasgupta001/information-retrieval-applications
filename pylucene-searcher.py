# Essential imports:
import pandas as pd
import lucene
from java.io import File

lucene.initVM()


# Retriever imports:
from org.apache.lucene.analysis.en import EnglishAnalyzer
#from org.apache.lucene.store import SimpleFSDirectory, FSDirectory
from org.apache.lucene.store import FSDirectory

from org.apache.lucene.index import IndexReader
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.search.similarities import BM25Similarity

def search(index_path, q):

    print ("Searching for:", q)

    analyzer = EnglishAnalyzer()
    directory = FSDirectory.open(index_path)
    searcher = IndexSearcher(DirectoryReader.open(directory))
    
    searcher.setSimilarity(BM25Similarity(1.8, 0.3))

    query = QueryParser("PLOT", analyzer).parse(q)
    #query = QueryParser("TITLE", analyzer).parse(q)

    scoreDocs = searcher.search(query, 10).scoreDocs
    print ("%s total matching documents" % (len(scoreDocs)))

    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)
        # print (doc.get("TITLE"))

        print("Title: ")
        print (doc.get("TITLE"))
        print ("-------------------------------------------------")
        print ("########### PLOT ###############")
        print (doc.get("PLOT"))
        print(scoreDoc.score)
        # doc.get("PLOT"))

indexPath = File("index-2/").toPath()

#search(indexPath, "murder")
search(indexPath, "crime in prison")
#search(indexPath, "mute")

# search(indexPath, "MURDER")
