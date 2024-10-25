file_path = 'wiki_movie_plots_deduped.csv' # Link : https://raw.githubusercontent.com/kiq005/movie-recommendation/refs/heads/master/src/dataset/wiki_movie_plots_deduped.csv

# Essential imports:
import pandas as pd
import lucene
from java.io import File

# Indexer imports:
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.analysis.en import EnglishAnalyzer
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
#from org.apache.lucene.store import SimpleFSDirectory, FSDirectory
from org.apache.lucene.store import FSDirectory
import org.apache.lucene.document as document

lucene.initVM()

indexPath = File("index-2/").toPath()
indexDir = FSDirectory.open(indexPath)

writerConfig = IndexWriterConfig(EnglishAnalyzer())
writer = IndexWriter(indexDir, writerConfig)

def indexMovie(title, plot):
    doc = document.Document()
    doc.add(document.Field("TITLE", title, document.TextField.TYPE_STORED))
    doc.add(document.Field("PLOT", plot, document.TextField.TYPE_STORED))
    writer.addDocument(doc)

def closeWriter():
    writer.close()

def makeIndex(file_path):
    df = pd.read_csv(file_path)
    
    docid = 0
    for i in df.index:
        print(docid, "-", df['Title'][i])
        indexMovie(df['Title'][i], df['Plot'][i])
        docid += 1

makeIndex(file_path)
closeWriter()

