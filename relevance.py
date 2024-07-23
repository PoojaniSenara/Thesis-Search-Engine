from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_relevance(query, text):
    # Check the lengths of the query and text
    print(f"Query length: {len(query)}")
    print(f"Text length: {len(text)}")

    documents = [query, text]

    # Check the documents being processed
    print(f"Documents: {documents}")

    tfidf = TfidfVectorizer().fit_transform(documents)
    
    # Print TF-IDF vectors
    print(f"TF-IDF shape: {tfidf.shape}")
    print(f"TF-IDF vectors: {tfidf.toarray()}")

    cosine_sim = cosine_similarity(tfidf[0:1], tfidf[1:2])

    
    # Convert cosine similarity to percentage
    relevance_percentage = cosine_sim[0][0] * 100
    print(f"Relevance Percentage: {relevance_percentage:.2f}%")

    return relevance_percentage
