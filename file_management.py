from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import os

# Function to classify files based on content
def classify_files(file_paths):
    file_contents = []
    
    # Read the contents of each file
    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as file:
            file_contents.append(file.read())
    
    # Convert text to numerical form using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(file_contents)

    # Cluster the documents using KMeans
    model = KMeans(n_clusters=2, random_state=42)
    model.fit(X)
    
    # Return the assigned cluster labels for each file
    return model.labels_
