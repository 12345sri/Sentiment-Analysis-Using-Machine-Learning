# Sentiment Analysis Using Machine Learning

# Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC

from sklearn.metrics import accuracy_score, classification_report

# Sample Dataset
data = {
    "text": [
        "I love this product",
        "This is amazing",
        "Very bad experience",
        "I hate this service",
        "Excellent quality",
        "Worst purchase ever",
        "Really satisfied",
        "Not good at all"
    ],
    
    "sentiment": [
        "Positive",
        "Positive",
        "Negative",
        "Negative",
        "Positive",
        "Negative",
        "Positive",
        "Negative"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Labels
X = df["text"]
y = df["sentiment"]

# Convert Text into Numerical Features
vectorizer = TfidfVectorizer()

X_tfidf = vectorizer.fit_transform(X)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf,
    y,
    test_size=0.2,
    random_state=42
)

# Machine Learning Models
models = {
    "Logistic Regression": LogisticRegression(),
    "Naive Bayes": MultinomialNB(),
    "KNN": KNeighborsClassifier(),
    "Linear SVC": LinearSVC()
}

# Train and Evaluate Models
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\n{name}")
    print("Accuracy:", accuracy)

    print(classification_report(y_test, predictions))

# Test Custom Sentence
sample_text = ["This product is really good"]

sample_vector = vectorizer.transform(sample_text)

best_model = LogisticRegression()

best_model.fit(X_train, y_train)

prediction = best_model.predict(sample_vector)

print("\nCustom Prediction:")
print(sample_text[0], "->", prediction[0])
